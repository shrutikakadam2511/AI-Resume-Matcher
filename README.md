# 🤖 AI-Powered Resume Scanner

An intelligent system that parses resumes in PDF format, extracts key candidate details, and ranks them based on a given job description using Natural Language Processing (NLP).

---

## 🚀 Features

- 📄 Upload and parse multiple resumes (PDFs)
- 🧠 Extract candidate information:
  - Name
  - Email
  - Skills
  - Experience
- 📝 Paste or upload a Job Description
- 🔍 Match resumes to JD using NLP (Cosine Similarity or BERT)
- 📊 Score and rank candidates by relevance
- ⚡ Clean and interactive interface with Flask or Streamlit

---
🧩 Key Functionalities
1. 📄 Resume Parsing
Use PyMuPDF or pdfminer.six to read resumes in .pdf format.

Extract text content, clean formatting.

2. 🏷️ Information Extraction
Use spaCy NER to extract:

Name

Email / Phone

Skills

Experience (years / roles / organizations)

Education (optional)

3. 📌 Job Description Input
Recruiter pastes a job description (JD).

This JD is preprocessed (stopwords removal, lowercasing, etc.)

4. 🧠 Semantic Matching
Resume content is compared with JD using:

TF-IDF + Cosine Similarity (fast, traditional)

OR

BERT / SBERT Embeddings for contextual semantic understanding

5. 📊 Ranking & Scoring
Each candidate is assigned a match percentage score (0–100%)

Resumes are ranked by relevance

Top candidates are shown first

📺 User Interface (if using Streamlit)
Upload multiple PDF resumes

Paste a job description

Click “Match”

View:

Extracted candidate details

Match percentage

Sortable table or card-style result
💡 Use Cases
HR screening large resume batches

Automated candidate shortlisting

Matching freelance profiles with projects

