# 🍔 McDonald's Review NLP Pipeline

An end-to-end NLP pipeline that processes 33,000+ McDonald's customer reviews — cleaning, classifying sentiment, labeling negative reviews by issue type, and visualizing insights through an interactive Streamlit dashboard.

---

## 📌 Project Overview

This project takes raw McDonald's customer reviews and runs them through a full NLP pipeline:

1. **Data Cleaning** — removes encoding corruption, normalizes whitespace, parses store addresses
2. **Sentiment Classification** — classifies each review as `positive`, `negative`, or `neutral` using DistilBERT
3. **Issue Labeling** — labels negative reviews by complaint category using Zero Shot Classification
4. **Interactive Dashboard** — visualizes insights through a Streamlit web app

---

## 🌐 Live Dashboard

👉 [View Live Dashboard](https://ckrg2001-mcdonalds-review-nlp-pipeline.streamlit.app)

---

## 🗂️ Project Structure

```
McDonalds-Review-NLP-Pipeline/
│
├── Data/
│   └── McDonald_s_Reviews.csv           # Raw input data
│
├── Output/
│   └── McDonald_s_Reviews_sentiment.csv # Processed output
│
├── main.py                              # Runs full pipeline (sentiment + labeling)
├── sentiment.py                         # Batch sentiment classification
├── classification.py                    # Zero shot issue labeling
├── clean.py                             # Text cleaning + address parsing
├── charts.py                            # Chart generation functions
├── app.py                               # Streamlit dashboard
├── requirements.txt
├── .env                                 # Model config (not pushed to GitHub)
├── .gitignore
└── README.md
```

---

## 🧠 Models Used

| Task | Model | Type |
|---|---|---|
| Sentiment Analysis | `distilbert-base-uncased-finetuned-sst-2-english` | Fine-tuned DistilBERT |
| Issue Labeling | `facebook/bart-large-mnli` | Zero Shot Classification |

---

## 📊 Dashboard Features

| Chart | Description |
|---|---|
| Sentiment Distribution | Overall breakdown of positive, negative, neutral |
| Top 10 States by Sentiment % | Stacked % bar chart per state |
| Issue Breakdown | Most common complaint categories in negative reviews |
| Top 10 Cities | Cities with most negative reviews |

**Sidebar filters:**
- Filter by State — all charts update dynamically
- KPI metrics — total reviews, negative count, positive count, avg rating

---

## 🔍 Key Findings

- **49%** of reviews are negative — significant dissatisfaction across locations
- **Wrong or missing orders** is the #1 complaint category
- **FL, TX, CA, NY** have the highest review volume
- **Dirty or unhygienic** conditions are the 2nd most common complaint

---

## ⚙️ Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/CKRG2001/McDonalds-Review-NLP-Pipeline.git
cd McDonalds-Review-NLP-Pipeline
```

**2. Create a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```


---

## 🚀 How to Run

**Run the full NLP pipeline:**
```bash
python main.py
```

**Launch the dashboard:**
```bash
streamlit run app.py
```

---

## 🛠️ Tech Stack

- **Python 3.12**
- **HuggingFace Transformers** — DistilBERT + BART
- **Pandas** — data manipulation
- **Matplotlib / Seaborn** — chart generation
- **Streamlit** — interactive dashboard
- **PyTorch (MPS)** — Apple M1 GPU acceleration
- **python-dotenv** — environment config

---

## 🔄 Pipeline Flow

```
Raw CSV
   ↓
clean.py          → removes encoding issues, parses addresses
   ↓
sentiment.py      → batch sentiment classification (DistilBERT)
   ↓
classification.py → zero shot issue labeling (BART) on negative reviews only
   ↓
Output CSV
   ↓
charts.py         → generates 4 analysis charts
   ↓
app.py            → Streamlit interactive dashboard
```

---

## 👤 Author

**Chaitanya Kumar Reddy Goukanapalli**
[GitHub](https://github.com/CKRG2001)
