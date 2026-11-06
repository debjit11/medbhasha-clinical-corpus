import argparse
import csv
from collections import Counter
from pathlib import Path

ENTITY_TYPES = {
    "DIAGNOSIS",
    "SYMPTOM",
    "MEDICATION",
    "DOSAGE",
    "TEST",
    "TEST_RESULT",
    "BODY_SITE",
    "PROCEDURE",
    "TEMPORAL",
    "NEGATION_UNCERTAINTY",
}

REQUIRED_COLUMNS = {"note_id", "token", "tag"}


def parse_tag(tag):
    """Return (prefix, entity_type) or None for an invalid tag."""
    tag = tag.strip()

    if tag == "O":
        return ("O", None)

    if "-" not in tag:
        return None

    prefix, entity_type = tag.split("-", 1)

    if prefix not in {"B", "I", "E", "S"}:
        return None

    if entity_type not in ENTITY_TYPES:
        return None

    return prefix, entity_type


def validate(input_file, scheme, report_file, separator=","):
    errors = []
    warnings = []
    entity_counts = Counter()
    tag_counts = Counter()
    note_ids = set()
    token_count = 0
    row_count = 0

    def error(message):
        errors.append(message)

    def warning(message):
        warnings.append(message)

    try:
        with open(input_file, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file, delimiter=separator)

            if reader.fieldnames is None:
                raise ValueError("The input file is empty or has no header.")

            reader.fieldnames = [
                name.strip() if name else name
                for name in reader.fieldnames
            ]

            missing = REQUIRED_COLUMNS - set(reader.fieldnames)

            if missing:
                error(
                    "Missing required columns: "
                    + ", ".join(sorted(missing))
                )
                write_report(
                    report_file, input_file, scheme, 0, 0,
                    errors, warnings, tag_counts, entity_counts
                )
                return False

            # BIOES also requires valid entity endings.
            previous_note = None
            active_entity = None
            active_start_row = None

            for row in reader:
                row_count += 1
                row_number = row_count + 1

                note_id = (row.get("note_id") or "").strip()
                token = (row.get("token") or "").strip()
                tag = (row.get("tag") or "").strip()

                token_count += 1

                if not note_id:
                    error(f"Row {row_number}: note_id is empty.")
                else:
                    note_ids.add(note_id)

                if not token:
                    warning(f"Row {row_number}: token is empty.")

                if not tag:
                    error(f"Row {row_number}: tag is empty.")
                    parsed = None
                else:
                    parsed = parse_tag(tag)

                if parsed is None and tag:
                    error(
                        f"Row {row_number}: invalid tag '{tag}'."
                    )
                    tag_counts[tag] += 1
                    continue

                if parsed is None:
                    continue

                prefix, entity_type = parsed
                tag_counts[tag] += 1

                allowed_prefixes = (
                    {"O", "B", "I"}
                    if scheme == "BIO"
                    else {"O", "B", "I", "E", "S"}
                )

                if prefix not in allowed_prefixes:
                    error(
                        f"Row {row_number}: tag '{tag}' is not "
                        f"allowed under the {scheme} scheme."
                    )
                    continue

                # Close an open entity at note boundaries.
                if note_id != previous_note:
                    if active_entity is not None:
                        if scheme == "BIOES":
                            error(
                                f"Row {active_start_row}: entity "
                                f"{active_entity} was not closed "
                                "with an E- tag before the note ended."
                            )
                        active_entity = None
                        active_start_row = None

                    previous_note = note_id

                if prefix == "O":
                    if active_entity is not None:
                        if scheme == "BIOES":
                            error(
                                f"Row {row_number}: O tag encountered "
                                f"before entity {active_entity} was closed."
                            )
                        active_entity = None
                        active_start_row = None
                    continue

                if prefix == "B":
                    if active_entity is not None and scheme == "BIOES":
                        error(
                            f"Row {row_number}: entity {active_entity} "
                            "was not closed before a new entity began."
                        )

                    active_entity = entity_type
                    active_start_row = row_number
                    entity_counts[entity_type] += 1

                elif prefix == "S":
                    if scheme != "BIOES":
                        error(
                            f"Row {row_number}: S- tag is invalid in BIO."
                        )
                        continue

                    if active_entity is not None:
                        error(
                            f"Row {row_number}: S- tag encountered "
                            f"inside unclosed entity {active_entity}."
                        )

                    entity_counts[entity_type] += 1
                    active_entity = None
                    active_start_row = None

                elif prefix == "I":
                    if active_entity != entity_type:
                        error(
                            f"Row {row_number}: {tag} does not continue "
                            "a matching entity."
                        )
                        active_entity = None
                        active_start_row = None

                elif prefix == "E":
                    if scheme != "BIOES":
                        error(
                            f"Row {row_number}: E- tag is invalid in BIO."
                        )
                        continue

                    if active_entity != entity_type:
                        error(
                            f"Row {row_number}: {tag} does not close "
                            "a matching entity."
                        )

                    active_entity = None
                    active_start_row = None

            if active_entity is not None and scheme == "BIOES":
                error(
                    f"Row {active_start_row}: entity {active_entity} "
                    "was not closed with an E- tag at end of file."
                )

    except (OSError, csv.Error, ValueError) as exc:
        error(f"Could not read input file: {exc}")

    write_report(
        report_file,
        input_file,
        scheme,
        len(note_ids),
        token_count,
        errors,
        warnings,
        tag_counts,
        entity_counts,
    )

    print(f"Notes found: {len(note_ids)}")
    print(f"Rows/tokens processed: {token_count}")
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    print(f"Report saved to: {report_file}")
    print("Result:", "PASS" if not errors else "FAIL")

    return not errors


def write_report(
    report_file,
    input_file,
    scheme,
    note_count,
    token_count,
    errors,
    warnings,
    tag_counts,
    entity_counts,
):
    lines = [
        "MedBhasha Annotation Validation Report",
        "=" * 45,
        f"Input file: {input_file}",
        f"Annotation scheme: {scheme}",
        f"Notes: {note_count}",
        f"Tokens/rows: {token_count}",
        f"Errors: {len(errors)}",
        f"Warnings: {len(warnings)}",
        "",
        "TAG COUNTS",
        "-" * 30,
    ]

    lines.extend(
        f"{tag}: {count}"
        for tag, count in sorted(tag_counts.items())
    )

    lines.extend(["", "ENTITY COUNTS", "-" * 30])
    lines.extend(
        f"{entity}: {count}"
        for entity, count in sorted(entity_counts.items())
    )

    lines.extend(["", "ERRORS", "-" * 30])
    lines.extend(errors if errors else ["No errors found."])

    lines.extend(["", "WARNINGS", "-" * 30])
    lines.extend(warnings if warnings else ["No warnings found."])

    lines.extend([
        "",
        "FINAL RESULT",
        "-" * 30,
        "PASS" if not errors else "FAIL",
        
        
    ])

    Path(report_file).write_text(
        "\n".join(lines) + "\n",
        encoding="utf-8",
    )


def main():
    parser = argparse.ArgumentParser(
        description="Validate a MedBhasha annotated CSV corpus."
    )
    parser.add_argument("--input", required=True, help="Input CSV file")
    parser.add_argument(
        "--scheme",
        choices=["BIO", "BIOES"],
        default="BIO",
        help="Annotation scheme (default: BIO)",
    )
    parser.add_argument(
        "--sep",
        default=",",
        help="CSV delimiter (default: comma)",
    )
    parser.add_argument(
        "--report",
        default="validation_report.txt",
        help="Output report filename",
    )

    args = parser.parse_args()

    success = validate(
        args.input,
        args.scheme,
        args.report,
        args.sep,
    )

    raise SystemExit(0 if success else 1)


if __name__ == "__main__":
    main()
