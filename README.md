🚀 Resume Matching Engine
AI-Powered Candidate Ranking System
<div align="center">








</div>
📌 Overview

This project is a Resume Matching Engine built for the Redrob AI Campus Hackathon.

The system intelligently matches resumes with job descriptions using:

✅ Skill Normalization
✅ TF-IDF Vectorization
✅ Cosine Similarity
✅ Candidate Ranking
✅ Interactive Tkinter GUI

The engine processes resumes, cleans inconsistent skill names, computes similarity scores, and ranks candidates based on relevance to job descriptions.

🖥️ Features
✨ Core Features
🔍 Resume-to-JD Matching
🧠 TF-IDF Based Scoring
📊 Cosine Similarity Ranking
🧹 Skill Cleaning & Deduplication
🏆 Top Candidate Highlighting
📈 Skill Rarity Analysis
🎨 Modern GUI with Tkinter
⚡ Pure Python Implementation
🏗️ System Architecture
                ┌──────────────────┐
                │ Raw Resume Skills │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Skill Cleaning & │
                │ Normalization    │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ TF-IDF Vector    │
                │ Generation       │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Job Description  │
                │ Vectorization    │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Cosine Similarity│
                │ Calculation      │
                └────────┬─────────┘
                         │
                         ▼
                ┌──────────────────┐
                │ Candidate Ranking│
                └──────────────────┘
🧠 Matching Algorithm
TF-IDF Formula

TF-IDF=TF×IDF

Where:

TF  = Term Frequency
IDF = Inverse Document Frequency
Cosine Similarity

cos(θ)=
∥A∥∥B∥
A⋅B
	​


Higher cosine score ⇒ Better candidate match.

🧹 Skill Normalization

The engine automatically fixes:

Raw Skill	Normalized Skill
Pyhton	python
Reacts	react
kubernates	kubernetes
data-viz	data_visualization

This ensures consistent matching across resumes and job descriptions.

📊 GUI Tabs
📖 How It Works

Explains the complete matching pipeline.

🧹 Normalized Skills

Displays cleaned and processed candidate skills.

📈 IDF Values

Shows skill rarity and importance scores.

🏆 Results

Displays ranked candidates with similarity scores.

📂 Project Structure
Resume-Matching-Engine/
│
├── main.py
├── README.md
⚙️ Installation
1️⃣ Clone Repository
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
2️⃣ Move Into Project Directory
cd YOUR_REPO
3️⃣ Run Application
python main.py
🛠️ Built With
Technology	Purpose
Python	Core Logic
Tkinter	GUI
Regex	Skill Cleaning
Math Module	TF-IDF & Similarity
📌 Sample Job Roles
🤖 ML Engineer
⚙️ Backend Engineer
🎨 Frontend Engineer
🎯 Key Concepts Used
Information Retrieval
Vector Space Models
NLP Preprocessing
TF-IDF
Cosine Similarity
Ranking Systems
GUI Development
🚀 Future Improvements
📄 PDF Resume Parsing
🌐 Web Deployment
🤖 AI-Based Semantic Search
🧠 NLP Skill Extraction
🗄️ Database Integration
📊 Analytics Dashboard
👨‍💻 Author
Arjun Kapil

Built for the Redrob AI Campus Hackathon.

⭐ If You Like This Project

Give it a ⭐ on GitHub
