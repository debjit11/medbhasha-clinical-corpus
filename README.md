# MedBhasha: Bengali Clinical NLP

**An Integrated Bengali Clinical Natural Language Processing Pipeline for Named Entity Recognition, Clinical Text Clustering, Healthcare Analytics, and Retrieval-Augmented Generation.**

## 📌 Project Overview

MedBhasha is a Bengali Clinical NLP project designed to process, analyze, and extract meaningful medical information from Bengali clinical text.

The project focuses on building an NLP pipeline using an annotated Bengali clinical corpus. It combines Named Entity Recognition (NER), unsupervised text clustering, clinical data analytics, and Retrieval-Augmented Generation (RAG) to explore how NLP and AI can support structured understanding of Bengali healthcare documentation.

The project also includes a corpus validation module to ensure annotation consistency and data quality.

## 🎯 Project Objectives

- Develop a Bengali clinical Named Entity Recognition system.
- Identify important medical entities from Bengali clinical text.
- Group similar clinical notes using text embeddings and clustering.
- Generate useful statistics and insights from the clinical corpus.
- Build a corpus-grounded RAG system for answering clinical questions.
- Validate annotated data using BIO/BIOES tagging schemes.
- Explore NLP-based approaches for Bengali healthcare information processing.

## 🚀 Key Features

### 1. Named Entity Recognition (NER)

A token-classification-based NER system designed to identify medical entities from Bengali clinical text.

**Key capabilities:**
- Bengali clinical entity extraction.
- BIO-based token classification.
- Pretrained BanglaBERT model fine-tuning.
- Training and validation workflow.
- Model evaluation and prediction.
- Saving trained model checkpoints.
- Extracting entity predictions with confidence scores.

**Supported entity categories:**

| Entity | Description |
|---|---|
| DIAGNOSIS | Medical diagnoses |
| SYMPTOM | Patient symptoms |
| MEDICATION | Medicines and drugs |
| DOSAGE | Medication dosage information |
| TEST | Medical tests and investigations |
| TEST_RESULT | Medical test results |
| BODY_SITE | Anatomical locations |
| PROCEDURE | Medical procedures |
| TEMPORAL | Time-related expressions |
| NEGATION_UNCERTAINTY | Negation or uncertainty expressions |

**Base model:** `csebuetnlp/banglabert`

### 2. Clinical Text Clustering

An unsupervised machine learning module that groups similar Bengali clinical notes based on their semantic content.

**Key capabilities:**
- Generate multilingual sentence embeddings.
- Apply K-Means clustering.
- Calculate silhouette scores.
- Extract important cluster keywords using TF-IDF.
- Visualize clusters using dimensionality reduction.
- Generate cluster summaries.

**Technologies:**
- Sentence Transformers
- Scikit-learn
- K-Means
- TF-IDF
- PCA
- Matplotlib

**Embedding model:** `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`

### 3. Clinical Data Analytics

A data analysis module that explores the annotated clinical corpus and generates useful statistical insights.

**Key capabilities:**
- Total clinical notes and token counts.
- Entity distribution and frequency analysis.
- BIO tag distribution.
- Most frequently occurring clinical terms.
- Entity co-occurrence analysis.
- Clinical corpus statistics.
- Visualization of entity distributions and patterns.
- Analysis of clustering results when available.

**Technologies:**
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

### 4. Retrieval-Augmented Generation (RAG)

A corpus-grounded retrieval system designed to retrieve relevant clinical information from the project's own Bengali annotated corpus.

The system uses semantic embeddings to identify relevant clinical notes and provide evidence-based responses to queries.

**Key capabilities:**
- Semantic search across clinical notes.
- Retrieve relevant passages using sentence embeddings.
- Similarity-based document retrieval.
- Preserve original note IDs for traceability.
- Extract relevant clinical entities from retrieved evidence.
- Generate evidence-grounded answers.
- Export retrieval results in CSV and JSONL formats.

**Technologies:**
- Sentence Transformers
- Scikit-learn
- Cosine Similarity
- Pandas

**Important:** The default RAG workflow uses the project's own corpus for retrieval and evidence-based answer construction. It does not depend on general web search or external document retrieval.

An optional local LLM integration may be used only where permitted by the competition rules.

### 5. Corpus Validation

A Python-based validation module that checks the structural consistency of the annotated Bengali clinical dataset.

**Key capabilities:**
- Validate required CSV columns.
- Identify invalid entity tags.
- Check BIO/BIOES annotation sequences.
- Count unique clinical notes and tokens.
- Generate tag and entity statistics.
- Identify annotation errors and warnings.
- Automatically generate validation reports.

**Supported annotation schemes:**
- BIO
- BIOES

## 🛠️ Technologies Used

| Category | Technologies |
|---|---|
| Programming Language | Python |
| NLP | Hugging Face Transformers |
| Bengali Language Model | BanglaBERT |
| Deep Learning | PyTorch |
| Sentence Embeddings | Sentence Transformers |
| Machine Learning | Scikit-learn |
| Clustering | K-Means |
| Text Analysis | TF-IDF |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Retrieval | Cosine Similarity |
| Data Format | CSV, JSONL |
| Development Environment | VS Code, Jupyter Notebook |


```

## 📊 Dataset Format

The annotated corpus is stored in CSV format.

The dataset contains the following required columns:

| Column | Description |
|---|---|
| `note_id` | Unique identifier of a clinical note |
| `token` | Individual word or token |
| `tag` | Annotation label assigned to the token |

**Example:**

```csv
note_id,token,tag
N001,রোগী,O
N001,জ্বর,B-SYMPTOM
N001,ও,O
N001,কাশি,B-SYMPTOM
N002,প্যারাসিটামল,B-MEDICATION
N002,৫০০,B-DOSAGE
N002,mg,I-DOSAGE
```

The example is illustrative. Actual annotations should follow the project's annotation guidelines.

## ⚙️ Installation and Setup

### 1. Clone the Repository


```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd Outliers_MedBhasha
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

For notebook execution:

```bash
pip install jupyter ipykernel
```

**Note:** Model training may require downloading pretrained model weights and access to sufficient GPU or CPU resources. The actual dependencies should be maintained in `requirements.txt`.

## ▶️ Project Workflow

The project follows this general workflow:

```text
       Bengali Clinical Corpus
                  |
                  v
          Corpus Validation
                  |
                  v
          Annotated Dataset
                  |
       +----------+----------+
       |          |          |
       v          v          v
      NER     Clustering  Analytics
       |          |          |
       v          v          v
 Entity       Similar      Clinical
Extraction     Notes       Insights
       |
       +----------+
                  |
                  v
             RAG System
                  |
                  v
       Relevant Clinical Evidence
                  |
                  v
          Grounded Answers
```

## 📓 Running the Notebooks

Open the project in VS Code and launch Jupyter notebooks.

```bash
jupyter notebook
```

Run the notebooks in the following order, depending on the task:

1. **Corpus Validation** – Check annotation quality and dataset structure.
2. **NER** – Train the Bengali clinical NER model and generate predictions.
3. **Clustering** – Generate embeddings and group similar clinical notes.
4. **Analytics** – Explore corpus statistics and entity distributions.
5. **RAG** – Retrieve relevant clinical evidence and generate grounded answers.

Make sure the dataset paths and output directories are correctly configured before running each notebook.

## 📄 Expected Outputs

| Component | Output |
|---|---|
| NER | Trained model, tokenizer, and `ner_predictions.csv` |
| Clustering | `clinical_note_clusters.csv` and `cluster_summary.csv` |
| Analytics | Corpus statistics, entity frequency tables, and visualizations |
| RAG | Retrieved passages and evidence-grounded answers in CSV/JSONL |
| Validation | `validation_report.txt` |

## ⚠️ Limitations

- Model performance depends on the quality and size of the annotated corpus.
- Bengali clinical terminology and spelling variations can affect entity recognition.
- Subword tokenization can affect entity boundary predictions.
- Clustering quality depends on embedding quality and the selected number of clusters.
- RAG answers are limited by the information available in the project's corpus.
- Retrieved information should not be treated as a substitute for professional medical advice.
- Corpus validation checks structural consistency, not medical correctness.
- Model performance must be evaluated using appropriate test data before making accuracy claims.

## 📚 Official Resources

- [MedBhasha Resources](https://github.com/pabitracsers/COMSYS-Hackathon-8/tree/main/MedBhasha-Resources)
- [Official Validation Script](https://github.com/pabitracsers/COMSYS-Hackathon-8/blob/main/MedBhasha-Resources/validate.py)
- [Entity Schema](https://github.com/pabitracsers/COMSYS-Hackathon-8/blob/main/MedBhasha-Resources/entity_schema.md)
- [Data Collection Rules](https://github.com/pabitracsers/COMSYS-Hackathon-8/blob/main/MedBhasha-Resources/data_collection_rules.md)
- [Worked Examples](https://github.com/pabitracsers/COMSYS-Hackathon-8/tree/main/MedBhasha-Resources/worked_example)

## 🔮 Future Improvements

- Improve Bengali clinical NER performance.
- Explore additional transformer-based architectures.
- Improve entity boundary detection and token alignment.
- Experiment with alternative clustering algorithms.
- Develop interactive clinical analytics dashboards.
- Improve semantic retrieval and RAG evaluation.
- Explore local LLM-based Bengali clinical question answering.
- Build a user-friendly interface for clinical text processing.

## 👨‍💻 Contributors

**Team Outliers – MedBhasha**

Developed as part of the MedBhasha Bengali Clinical NLP hackathon initiative.

---

**MedBhasha – Exploring AI and NLP for Bengali Clinical Text Understanding.**