# MedBhasha: Bengali Clinical NLP Corpus Validation

A Python-based validation tool for checking the structural consistency of an annotated Bengali clinical Natural Language Processing (NLP) corpus using BIO or BIOES tagging schemes.

## 📌 Project Overview

MedBhasha focuses on Bengali clinical text annotation and Named Entity Recognition (NER). This project provides a validation script to check whether an annotated corpus follows the expected CSV structure, uses valid entity tags, and maintains consistent annotation sequences.

The validator processes an annotated CSV file and generates a `validation_report.txt` file containing corpus statistics, tag counts, entity counts, validation errors, warnings, and the final validation result.

## 🎯 Objectives

- Validate the structure of an annotated clinical corpus.
- Check the presence of required CSV columns.
- Identify invalid entity tags.
- Detect inconsistent BIO or BIOES annotation sequences.
- Count annotated notes, tokens, tags, and entity beginnings.
- Generate a validation report automatically.
- Support corpus quality checks before submission.

## 🛠️ Technologies Used

- **Python 3**
- CSV processing
- `argparse` for command-line arguments
- `collections.Counter` for counting tags and entities
- `pathlib` for file handling

The validation script uses Python's standard library, so no third-party packages are required.

## 📂 Project Structure

```text
MedBhasha/
│
├── validate.py
├── Annotated_corpus.csv
├── validation_report.txt
└── README.md
```

| File | Description |
|---|---|
| `validate.py` | Python script for corpus validation |
| `Annotated_corpus.csv` | Annotated clinical text dataset |
| `validation_report.txt` | Automatically generated validation report |
| `README.md` | Project documentation |

## 📊 Dataset Format

The input CSV file must contain the following columns:

| Column | Description |
|---|---|
| `note_id` | Identifier of the clinical note |
| `token` | Individual word or token from the clinical text |
| `tag` | Annotation label assigned to the token |

### Example

```csv
note_id,token,tag
N001,রোগী,O
N001,জ্বরে,B-SYMPTOM
N001,ভুগছেন,O
N002,প্যারাসিটামল,B-MEDICATION
N002,খাবেন,O
```

The example is illustrative. Actual annotations should follow the project's annotation guidelines.

## 🏷️ Supported Entity Categories

The validator recognizes the following entity types:

- `DIAGNOSIS` — Medical diagnoses
- `SYMPTOM` — Patient symptoms
- `MEDICATION` — Medicines and drugs
- `DOSAGE` — Medication dosage information
- `TEST` — Medical tests and investigations
- `TEST_RESULT` — Results of medical tests
- `BODY_SITE` — Body parts or anatomical locations
- `PROCEDURE` — Medical procedures
- `TEMPORAL` — Time-related expressions
- `NEGATION_UNCERTAINTY` — Negation or uncertainty expressions

## 🔖 Annotation Schemes

### BIO Scheme

The BIO scheme uses three tag prefixes:

- `B-` — Beginning of an entity
- `I-` — Inside or continuation of an entity
- `O` — Outside any entity

Example:

```text
প্যারাসিটামল  B-MEDICATION
খাবেন          O
```

### BIOES Scheme

The BIOES scheme uses five tag prefixes:

- `B-` — Beginning of an entity
- `I-` — Inside an entity
- `E-` — End of an entity
- `S-` — A single-token entity
- `O` — Outside any entity

Choose the scheme that matches the annotations in your dataset.

## ⚙️ Installation and Setup

### 1. Install Python

Install Python 3 if it is not already installed.

Check your Python version:

```bash
python --version
```

### 2. Clone or Download the Project

Download the project files and open the project folder in VS Code.

### 3. Set Up a Virtual Environment (Optional)

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

No additional Python packages are required for the custom validator described in this project.

## ▶️ Usage

Open the VS Code terminal in the project directory.

### Validate Using BIO

```bash
python validate.py --input Annotated_corpus.csv --scheme BIO
```

### Validate Using BIOES

```bash
python validate.py --input Annotated_corpus.csv --scheme BIOES
```

### Specify a Custom Report Filename

```bash
python validate.py --input Annotated_corpus.csv --scheme BIO --report my_report.txt
```

### Specify a CSV Delimiter

For a semicolon-separated file:

```bash
python validate.py --input Annotated_corpus.csv --scheme BIO --sep ";"
```

## 📄 Validation Report

The script generates a text report containing:

- Input filename and annotation scheme
- Number of unique clinical notes
- Number of processed rows or tokens
- Tag frequency counts
- Entity counts
- Validation errors
- Validation warnings
- Final validation status

The report is saved as `validation_report.txt` by default.

### Understanding the Result

**PASS:** No errors were detected by the checks implemented in the validator.

**FAIL:** One or more validation errors were detected and should be reviewed.

Warnings should also be reviewed, even when the final result is PASS.

## 🔍 Validation Checks

The custom validator checks:

1. Required CSV columns are present.
2. Note identifiers are not empty.
3. Empty tokens are reported as warnings.
4. Annotation tags use recognized entity types and prefixes.
5. BIO or BIOES tag usage matches the selected scheme.
6. Entity continuation and ending sequences are checked.
7. Tag and entity counts are included in the report.

The precise checks depend on the implementation of `validate.py`. Structural validation alone does not establish that clinical annotations are medically correct.

## ⚠️ Limitations


- The validator checks annotation structure, not the medical correctness of each label.
- It does not train or evaluate an NLP model.
- It does not automatically correct invalid annotations.
- It does not establish data privacy, consent, licensing, or source permissions.
- A PASS result does not guarantee complete compliance with all dataset or hackathon requirements.
- If the hackathon organizers require their official validator, use that version for the final submission.

## 📚 Official Resources

- [MedBhasha Resources](https://github.com/pabitracsers/COMSYS-Hackathon-8/tree/main/MedBhasha-Resources)
- [Official Validation Script](https://github.com/pabitracsers/COMSYS-Hackathon-8/blob/main/MedBhasha-Resources/validate.py)
- [Entity Schema](https://github.com/pabitracsers/COMSYS-Hackathon-8/blob/main/MedBhasha-Resources/entity_schema.md)
- [Data Collection Rules](https://github.com/pabitracsers/COMSYS-Hackathon-8/blob/main/MedBhasha-Resources/data_collection_rules.md)
- [Worked Examples](https://github.com/pabitracsers/COMSYS-Hackathon-8/tree/main/MedBhasha-Resources/worked_example)

## 🚀 Future Improvements

- Add more comprehensive BIOES sequence validation.
- Provide machine-readable JSON validation reports.
- Add automated suggestions for common annotation errors.
- Integrate corpus validation into an NLP data preparation pipeline.
- Develop annotation quality metrics and dataset statistics.


