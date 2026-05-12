from __future__ import annotations

import math
from collections import Counter
from typing import Dict, List, Tuple

SKILL_ALIASES = {
"python": "python",
"pyhton": "python",
"java": "java",
"javascript": "javascript",
"javascrpit": "javascript",
"js": "javascript",
"typescript": "typescript",
"typescrpit": "typescript",
"c++": "cpp",
"cpp": "cpp",
"r": "r",
"kotlin": "kotlin",
"machinelearning": "machine_learning",
"machine learning": "machine_learning",
"ml": "machine_learning",
"sklearn": "machine_learning",
"deeplearning": "deep_learning",
"deep learning": "deep_learning",
"deep-learning": "deep_learning",
"tensorflow": "tensorflow",
"pytorch": "pytorch",
"keras": "keras",
"nlp": "nlp",
"bert": "bert",
"xgboost": "xgboost",
"feature engineering": "feature_engineering",
"statistics": "statistics",
"stats": "statistics",
"regression": "regression",
"clustering": "clustering",
"data-viz": "data_visualization",
"data visualization": "data_visualization",
"data viz": "data_visualization",
"matplotlib": "data_visualization",
"tableau": "data_visualization",
"power-bi": "data_visualization",
"power bi": "data_visualization",
"powerbi": "data_visualization",
"pandas": "pandas",
"numpy": "numpy",

"react": "react",
"reacts": "react",
"reactjs": "react",
"vue": "vue",
"vue.js": "vue",
"vuejs": "vue",
"redux": "redux",
"tailwind": "tailwind",
"html/css": "html_css",
"html css": "html_css",
"html": "html_css",
"css": "html_css",
"jest": "jest",
"graphql": "graphql",

"nodejs": "nodejs",
"node js": "nodejs",
"flask": "flask",
"spring boot": "spring_boot",
"springboot": "spring_boot",
"rest api": "rest_api",
"rest": "rest_api",
"restapi": "rest_api",
"microservices": "microservices",

"sql": "sql",
"mysql": "mysql",
"mysq": "mysql",
"postgresql": "postgresql",
"postgres": "postgresql",
"mongodb": "mongodb",
"redis": "redis",

"docker": "docker",
"kubernetes": "kubernetes",
"kubernates": "kubernetes",
"k8s": "kubernetes",
"ci/cd": "ci_cd",
"cicd": "ci_cd",
"ci cd": "ci_cd",
"aws": "aws",# Mobile
"android": "android",
"firebase": "firebase",
# CS Fundamentals
"algorithms": "algorithms",
"algoritms": "algorithms",
"data structure": "data_structures",
"data structures": "data_structures",
"competitive programming": "competitive_programming",
# Design
"ui/ux": "ui_ux",
"ui ux": "ui_ux",
"figma": "figma",
}
RESUMES = [
    {"id": "01", "name": "Arjun Sharma", "raw_skills": "Pyhton, MachineLearning, SQL, pandas, numpy, Deep-learning"},
    {"id": "02", "name": "Priya Nair", "raw_skills": "JavaScrpit, Reacts, Node.JS, MongoDb, REST api, HTML/CSS"},
    {"id": "03", "name": "Rahul Gupta", "raw_skills": "Java, Spring Boot, MySql, Microservices, Docker, kubernates"},
    {"id": "04", "name": "Sneha Patel", "raw_skills": "Python, TensorFlow, Keras, NLP, BERT, data-viz, matplotlib"},
    {"id": "05", "name": "Vikram Singh", "raw_skills": "C++, Algoritms, Data Structure, competitive programming, python"},
    {"id": "06", "name": "Ananya Krishnan", "raw_skills": "javascript, vue.js, python, flask, PostgreSQL, AWS, CI/CD"},
    {"id": "07", "name": "Karan Mehta", "raw_skills": "Python, Sklearn, Xgboost, feature engineering, SQL, tableau"},
    {"id": "08", "name": "Deepika Rao", "raw_skills": "Java, Android, Kotlin, Firebase, REST, UI/UX, figma"},
    {"id": "09", "name": "Aditya Kumar", "raw_skills": "Reactjs, TypeScrpit, GraphQL, redux, tailwind, nodejs, jest"},
    {"id": "10", "name": "Meera Iyer", "raw_skills": "python, R, statistics, ML, regression, clustering, Power-BI"},
]
JDS = [
    {
        "id": "JD-1",
        "company": "Kakao (Seoul)",
        "role": "ML Engineer",
        "required_skills": "Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, SQL, Data Visualization",
        "preferred_skills": "NLP, BERT, Feature Engineering, Statistics",
    },
    {
        "id": "JD-2",
        "company": "Naver (Seongnam)",
        "role": "Backend Engineer",
        "required_skills": "Java, Spring Boot, MySQL, PostgreSQL, Microservices, Docker, Kubernetes",
        "preferred_skills": "REST API, CI/CD, Redis",
    },
    {
        "id": "JD-3",
        "company": "Line (Seoul)",
        "role": "Frontend Engineer",
        "required_skills": "JavaScript, React, Vue, TypeScript, REST API, HTML/CSS",
        "preferred_skills": "Node.js, GraphQL, Redux, Jest, AWS",
    },
]
def normalize_token(token: str) -> str:
    """
    Lowercase and strip whitespace only.
    Keep punctuation because the alias map contains entries like:
    - node.js
    - ci/cd
    - html/css
    - deep-learning
    """
    return token.strip().lower()


def canonicalize_skill(token: str) -> str | None:
    """
    Exact phrase match first, then discard if unknown.
    This follows the sheet's rule to match multi-word phrases before
    token-level processing and to discard unknown tokens.
    """
    token = normalize_token(token)

    if token in SKILL_ALIASES:
        return SKILL_ALIASES[token]

    # Fallback for tokens with extra internal spacing.
    compact = " ".join(token.split())
    if compact in SKILL_ALIASES:
        return SKILL_ALIASES[compact]

    return None


def extract_skills(raw_skills: str) -> List[str]:
    """
    1) Split on commas
    2) Lowercase
    3) Alias map
    4) Discard unknown tokens
    5) Deduplicate
    """
    raw_parts = [part.strip() for part in raw_skills.split(",")]
    canonical: List[str] = []

    for part in raw_parts:
        if not part:
            continue
        skill = canonicalize_skill(part)
        if skill is not None:
            canonical.append(skill)

    # Deduplicate while preserving order
    seen = set()
    deduped = []
    for skill in canonical:
        if skill not in seen:
            seen.add(skill)
            deduped.append(skill)

        return deduped
    def build_vocabulary(resume_skills: List[List[str]]) -> List[str]:
    vocab = sorted({skill for skills in resume_skills for skill in skills})
    return vocab


# ------------------------------------------------------------
# 5) TF-IDF for resumes
#    TF = 1 / N after deduplication
#    IDF = ln(10 / df(skill))
# ------------------------------------------------------------
def compute_idf(resume_skills: List[List[str]], vocab: List[str]) -> Dict[str, float]:
    df = Counter()
    for skills in resume_skills:
        for skill in set(skills):
            df[skill] += 1

    idf = {}
    for skill in vocab:
        # No smoothing, exactly as the sheet says
        idf[skill] = math.log(10 / df[skill])

    return idf


def build_resume_vectors(resume_skills: List[List[str]], vocab: List[str]) -> List[List[float]]:
    idf = compute_idf(resume_skills, vocab)
    index = {skill: i for i, skill in enumerate(vocab)}

    vectors: List[List[float]] = []
    for skills in resume_skills:
        n = len(skills)
        tf = 1 / n if n > 0 else 0.0

        vec = [0.0] * len(vocab)
        for skill in skills:
            vec[index[skill]] = tf * idf[skill]
        vectors.append(vec)

    return vectors
def build_jd_vectors(jd_skills: List[List[str]], vocab: List[str]) -> List[List[int]]:
    index = {skill: i for i, skill in enumerate(vocab)}

    vectors: List[List[int]] = []
    for skills in jd_skills:
        vec = [0] * len(vocab)
        for skill in set(skills):
            if skill in index:
                vec[index[skill]] = 1
        vectors.append(vec)

    return vectors
def cosine_similarity(a: List[float], b: List[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(y * y for y in b))

    if norm_a == 0 or norm_b == 0:
        return 0.0

    return dot / (norm_a * norm_b)
def rank_candidates(
    resume_names: List[str],
    resume_vectors: List[List[float]],
    jd_vectors: List[List[int]],
) -> List[List[Tuple[str, float]]]:
    all_rankings = []

    for jd_vec in jd_vectors:
        scores = []
        for name, rvec in zip(resume_names, resume_vectors):
            score = cosine_similarity(rvec, jd_vec)
            scores.append((name, score))

        # Sort by:
        # 1) score descending
        # 2) candidate name alphabetically
        scores.sort(key=lambda x: (-x[1], x[0]))
        all_rankings.append(scores[:3])

    return all_rankings
def print_results(rankings: List[List[Tuple[str, float]]]) -> None:
    for i, top3 in enumerate(rankings, start=1):
        print(f"JD-{i} — {JDS[i-1]['company']} ({JDS[i-1]['role']})")
        print(", ".join(f"{name}({score:.2f})" for name, score in top3))
        if i != len(rankings):
            print()
def main() -> None:
    resume_names = [r["name"] for r in RESUMES]
    resume_skills = [extract_skills(r["raw_skills"]) for r in RESUMES]

    jd_skills = [
        extract_skills(jd["required_skills"] + ", " + jd["preferred_skills"])
        for jd in JDS
    ]

    vocab = build_vocabulary(resume_skills)
    resume_vectors = build_resume_vectors(resume_skills, vocab)
    jd_vectors = build_jd_vectors(jd_skills, vocab)

    rankings = rank_candidates(resume_names, resume_vectors, jd_vectors)
    print_results(rankings)


if __name__ == "__main__":
    main()