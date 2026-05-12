# 🚀 Resume Matching Engine

### AI-Powered Candidate Ranking System

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge\&logo=python)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-green?style=for-the-badge)
![TF-IDF](https://img.shields.io/badge/Algorithm-TF--IDF-orange?style=for-the-badge)
![Cosine Similarity](https://img.shields.io/badge/Matching-Cosine%20Similarity-red?style=for-the-badge)

---

# 📌 Overview

This project is a **Resume Matching Engine** built for the **Redrob AI Campus Hackathon**.

The system intelligently matches resumes with job descriptions using:

* ✅ Skill Normalization
* ✅ TF-IDF Vectorization
* ✅ Cosine Similarity
* ✅ Candidate Ranking
* ✅ Interactive Tkinter GUI

---

# ✨ Features

* 🔍 Resume-to-JD Matching
* 🧠 TF-IDF Based Scoring
* 📊 Cosine Similarity Ranking
* 🧹 Skill Cleaning & Deduplication
* 🏆 Top Candidate Highlighting
* 📈 Skill Rarity Analysis
* 🎨 Interactive GUI
* ⚡ Pure Python Implementation

---

# 🏗️ System Architecture

```text
Raw Resume Skills
        ↓
Skill Cleaning & Normalization
        ↓
TF-IDF Vector Generation
        ↓
Job Description Vectorization
        ↓
Cosine Similarity Calculation
        ↓
Candidate Ranking
```

---

# 🧠 Matching Formula

## TF-IDF

```text
TF-IDF = TF × IDF
```

Where:

```text
TF  = Term Frequency
IDF = Inverse Document Frequency
```

---

## Cosine Similarity

```text
Cosine(A, B) = (A · B) / (||A|| × ||B||)
```

Higher cosine score = Better candidate match.

---

# 🧹 Skill Normalization

The engine automatically fixes typos and aliases.

| Raw Skill  | Normalized Skill   |
| ---------- | ------------------ |
| Pyhton     | python             |
| Reacts     | react              |
| kubernates | kubernetes         |
| data-viz   | data_visualization |

---

# 📊 GUI Tabs

| Tab                  | Purpose                        |
| -------------------- | ------------------------------ |
| 📖 How It Works      | Explains the complete pipeline |
| 🧹 Normalized Skills | Shows cleaned skills           |
| 📈 IDF Values        | Displays skill rarity          |
| 🏆 Results           | Shows ranked candidates        |

---

# 📂 Project Structure

```bash
Resume-Matching-Engine/
│
├── main.py
├── README.md
```

---

# ⚙️ Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
```

## Move Into Directory

```bash
cd YOUR_REPO
```

## Run Project

```bash
python main.py
```

---

# 🛠️ Built With

| Technology  | Purpose                |
| ----------- | ---------------------- |
| Python      | Core Logic             |
| Tkinter     | GUI                    |
| Regex       | Skill Cleaning         |
| Math Module | Similarity Calculation |

---

# 📌 Sample Job Roles

* 🤖 ML Engineer
* ⚙️ Backend Engineer
* 🎨 Frontend Engineer

---

# 🚀 Future Improvements

* 📄 PDF Resume Parsing
* 🌐 Web Deployment
* 🤖 NLP Semantic Matching
* 🗄️ Database Integration
* 📊 Analytics Dashboard

---

# 👨‍💻 Author

## Arjun Kapil

Built for the **Redrob AI Campus Hackathon**

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub.
