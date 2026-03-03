# Resume Screening AI

A Python-based Resume Screening AI that compares a candidate's resume with a job description and calculates a match percentage using basic NLP techniques.

## 📌 Project Overview

This project helps in filtering resumes by matching keywords from a resume with the job description. It calculates a match score and categorizes it as Low, Moderate, or Strong match.

## 🚀 Features

- Accepts Resume text input
- Accepts Job Description input
- Keyword matching logic
- Calculates Match Percentage
- Categorizes result:
  - Strong Match (Above 70%)
  - Moderate Match (40% - 70%)
  - Low Match (Below 40%)

## 🛠️ Technologies Used

- Python
- Basic NLP (Text Processing)
- String Matching
- CLI (Command Line Interface)

## 📊 How It Works

1. Converts text to lowercase
2. Splits text into keywords
3. Finds common words between resume and job description
4. Calculates match percentage
5. Displays match category

## ▶️ How to Run the Project

1. Make sure Python is installed.
2. Open terminal in project folder.
3. Run:

   python main.py

## 🎯 Future Improvements

- Remove stopwords (like "the", "and")
- Use advanced NLP libraries (NLTK / spaCy)
- Add GUI interface
- Upload resume as PDF input

---

### 👩‍💻 Created by Srabana
