# AI Resume Screener & Capability Scorer

An intelligent system to automate resume screening using AI.  
It analyzes multiple resume PDFs, predicts the most suitable job role, and scores each candidate’s capability — including identifying freshers.

---

## Features

- Upload multiple resumes at once (PDF)
- Predicts the most suitable job role using a trained ML model
- Calculates a capability score out of 100, displayed as a percentage
- Automatically ranks resumes based on capability
- Preview and download individual resumes inside the app
- Identifies "Fresher" if no experience is found

---


### 📤 Resume Upload and Scoring
![Resume Upload UI](assets/interface_upload.png)

### 📊 Ranked Resume Results
![Resume Ranking UI](assets/interface_results.png)


## Folder Structure
```

resume_matcher/
├── app.py
├── parser.py
├── scorer.py
├── train_classifier.py
├── generate_labels.py
├── requirements.txt
├── README.md
├── models/
│ ├── resume_classifier.pkl
│ └── vectorizer.pkl
├── data/
│ ├── labels.csv
│ ├── extracted_texts.csv
│ └── <CATEGORY_NAME>/*.pdf


---

##  Setup Instructions

### 1. Clone the repository and install dependencies
```bash
pip install -r requirements.txt
python generate_labels.py
python parser.py
python train_classifier.py
streamlit run app.py


#Author
Mohit Rahangdale – B-tech (AI) student

# Future Improvements
JD Matching Module (paste JD → get best-fit resumes)

Resume shortlisting & export

Embedding-based scoring using Sentence Transformers
