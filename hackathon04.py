import math
import re
import tkinter as tk
from tkinter import ttk

# ── skill alias map ───────────────────────────────────────────
skill_map = {
    "python":"python","pyhton":"python","java":"java","javascript":"javascript",
    "javascrpit":"javascript","js":"javascript","typescript":"typescript",
    "typescrpit":"typescript","c++":"cpp","cpp":"cpp","r":"r","kotlin":"kotlin",
    "machinelearning":"machine_learning","machine learning":"machine_learning",
    "ml":"machine_learning","sklearn":"machine_learning","deeplearning":"deep_learning",
    "deep learning":"deep_learning","deep-learning":"deep_learning",
    "tensorflow":"tensorflow","pytorch":"pytorch","keras":"keras","nlp":"nlp",
    "bert":"bert","xgboost":"xgboost","feature engineering":"feature_engineering",
    "statistics":"statistics","stats":"statistics","regression":"regression",
    "clustering":"clustering","data-viz":"data_visualization",
    "data visualization":"data_visualization","data viz":"data_visualization",
    "matplotlib":"data_visualization","tableau":"data_visualization",
    "power-bi":"data_visualization","power bi":"data_visualization",
    "powerbi":"data_visualization","pandas":"pandas","numpy":"numpy",
    "react":"react","reacts":"react","reactjs":"react","vue":"vue",
    "vue.js":"vue","vuejs":"vue","redux":"redux","tailwind":"tailwind",
    "html/css":"html_css","html css":"html_css","html":"html_css","css":"html_css",
    "jest":"jest","graphql":"graphql","node.js":"nodejs","nodejs":"nodejs",
    "node js":"nodejs","flask":"flask","spring boot":"spring_boot",
    "springboot":"spring_boot","rest api":"rest_api","rest":"rest_api",
    "restapi":"rest_api","microservices":"microservices","sql":"sql",
    "mysql":"mysql","mysq":"mysql","postgresql":"postgresql","postgres":"postgresql",
    "mongodb":"mongodb","redis":"redis","docker":"docker","kubernetes":"kubernetes",
    "kubernates":"kubernetes","k8s":"kubernetes","ci/cd":"ci_cd","cicd":"ci_cd",
    "ci cd":"ci_cd","aws":"aws","android":"android","firebase":"firebase",
    "algorithms":"algorithms","algoritms":"algorithms",
    "data structure":"data_structures","data structures":"data_structures",
    "competitive programming":"competitive_programming","ui/ux":"ui_ux",
    "ui ux":"ui_ux","figma":"figma",
}

candidate_data = [
    ("Arjun Sharma",    "Pyhton, MachineLearning, SQL, pandas, numpy, Deep-learning"),
    ("Priya Nair",      "JavaScrpit, Reacts, Node.JS, MongoDb, REST api, HTML/CSS"),
    ("Rahul Gupta",     "Java, Spring Boot, MySql, Microservices, Docker, kubernates"),
    ("Sneha Patel",     "Python, TensorFlow, Keras, NLP, BERT, data-viz, matplotlib"),
    ("Vikram Singh",    "C++, Algoritms, Data Structure, competitive programming, python"),
    ("Ananya Krishnan", "javascript, vue.js, python, flask, PostgreSQL, AWS, CI/CD"),
    ("Karan Mehta",     "Python, Sklearn, XGboost, feature engineering, SQL, tableau"),
    ("Deepika Rao",     "Java, Android, Kotlin, Firebase, REST, UI/UX, figma"),
    ("Aditya Kumar",    "Reactjs, TypeScrpit, GraphQL, redux, tailwind, nodejs, jest"),
    ("Meera Iyer",      "python, R, statistics, ML, regression, clustering, Power-BI"),
]

job_data = [
    ("JD-1", "Kakao (ML Engineer)",
     "Python, Machine Learning, Deep Learning, TensorFlow, PyTorch, SQL, Data Visualization, NLP, BERT, Feature Engineering, Statistics"),
    ("JD-2", "Naver (Backend Engineer)",
     "Java, Spring Boot, MySQL, PostgreSQL, Microservices, Docker, Kubernetes, REST API, CI/CD, Redis"),
    ("JD-3", "Line (Frontend Engineer)",
     "JavaScript, React, Vue, TypeScript, REST API, HTML/CSS, Node.js, GraphQL, Redux, Jest, AWS"),
]

# ── core logic ────────────────────────────────────────────────
def clean_skills(raw_text):
    tokens = re.split(r',\s*', raw_text.strip())
    already_added = set()
    found = []
    for token in tokens:
        token = token.lower()
        if token in skill_map:
            clean = skill_map[token]
            if clean not in already_added:
                already_added.add(clean)
                found.append(clean)
    return found

resumes = [(name, clean_skills(raw)) for name, raw in candidate_data]

all_skills = set()
for _, skill_list in resumes:
    all_skills.update(skill_list)
word_list = sorted(all_skills)
word_pos  = {word_list[i]: i for i in range(len(word_list))}

doc_freq = {}
for s in word_list:
    count = 0
    for _, skill_list in resumes:
        if s in skill_list:
            count += 1
    doc_freq[s] = count

idf_scores = {s: math.log(10 / doc_freq[s]) for s in word_list}

def make_resume_vec(skill_list):
    n = len(skill_list)
    vec = [0.0] * len(word_list)
    for s in skill_list:
        vec[word_pos[s]] = (1.0 / n) * idf_scores[s]
    return vec

def make_jd_vec(raw_text):
    vec = [0.0] * len(word_list)
    for s in clean_skills(raw_text):
        if s in word_pos:
            vec[word_pos[s]] = 1.0
    return vec

def get_cosine(v1, v2):
    top  = sum(v1[i] * v2[i] for i in range(len(v1)))
    mag1 = math.sqrt(sum(x*x for x in v1))
    mag2 = math.sqrt(sum(x*x for x in v2))
    if mag1 == 0 or mag2 == 0:
        return 0.0
    return top / (mag1 * mag2)

resume_vecs = [(name, make_resume_vec(skills)) for name, skills in resumes]

def run_matching():
    all_results = []
    for jd_id, jd_label, jd_raw in job_data:
        jv = make_jd_vec(jd_raw)
        scores = [(name, round(get_cosine(rv, jv), 4)) for name, rv in resume_vecs]
        scores.sort(key=lambda x: (-x[1], x[0]))
        all_results.append((jd_id, jd_label, scores))
    return all_results

# ── helpers ───────────────────────────────────────────────────
BG      = "#f4f6f9"
DARK    = "#1a1a2e"
BLUE    = "#4a90d9"
GREEN   = "#22c55e"
WHITE   = "#ffffff"
GREY    = "#888888"
MEDALS  = ["🥇", "🥈", "🥉"]

def scrollable_frame(parent):
    """Returns (outer_frame, inner_frame) where inner_frame is scrollable."""
    outer = tk.Frame(parent, bg=BG)
    canvas = tk.Canvas(outer, bg=BG, highlightthickness=0)
    scrollbar = ttk.Scrollbar(outer, orient="vertical", command=canvas.yview)
    inner = tk.Frame(canvas, bg=BG)
    inner.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=inner, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)
    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")
    # mouse-wheel scroll
    canvas.bind_all("<MouseWheel>", lambda e: canvas.yview_scroll(int(-1*(e.delta/120)), "units"))
    return outer, inner

def section_label(parent, text):
    tk.Label(parent, text=text, font=("Arial", 12, "bold"),
             bg=BG, fg=DARK).pack(anchor="w", padx=24, pady=(20, 6))
    tk.Frame(parent, height=2, bg=DARK).pack(fill="x", padx=24, pady=(0, 10))

def card(parent, padx=24, pady=6):
    f = tk.Frame(parent, bg=WHITE, relief="solid", bd=1)
    f.pack(fill="x", padx=padx, pady=pady)
    return f

# ── TAB 1: How it works ───────────────────────────────────────
def build_how_it_works(parent):
    outer, inner = scrollable_frame(parent)

    section_label(inner, "How the Matching Engine Works")

    steps = [
        ("1. Skill Normalization",
         "Raw skills are split on commas using re.split(), lowercased, and looked up in\n"
         "skill_map. Typos are fixed (e.g. Pyhton → python) and aliases are resolved\n"
         "(e.g. matplotlib → data_visualization). Unknown tokens are discarded."),
        ("2. Deduplication",
         "After normalization, if two raw tokens map to the same canonical skill\n"
         "(e.g. data-viz AND matplotlib both → data_visualization), only one copy\n"
         "is kept. Each skill appears at most once per resume."),
        ("3. Vocabulary Building",
         "All unique canonical skills across all 10 resumes are collected and sorted\n"
         f"alphabetically. This gives a shared vocabulary of {len(word_list)} skills.\n"
         "Both resume vectors and JD vectors use this same ordering."),
        ("4. TF-IDF Vectors for Resumes",
         "TF = 1 / N  where N = number of unique skills in the resume\n"
         "IDF = ln(10 / df)  where df = how many resumes contain that skill\n"
         "TF-IDF = TF × IDF\n\n"
         "Rare skills get a higher IDF score, meaning they carry more weight.\n"
         "E.g. python appears in 6 resumes → IDF ≈ 0.51 (low weight)\n"
         "     bert appears in 1 resume  → IDF ≈ 2.30 (high weight)"),
        ("5. JD Binary Vectors",
         "JD skills are normalized using the same skill_map. Then a binary vector\n"
         "is built: 1 if the skill is in the JD, 0 otherwise. Skills not present\n"
         "in the vocabulary (e.g. pytorch, redis) contribute 0."),
        ("6. Cosine Similarity & Ranking",
         "Cosine(A, B) = dot(A, B) / (||A|| × ||B||)\n"
         "A = Resume TF-IDF vector, B = JD binary vector\n\n"
         "Score close to 1.0 = strong match, close to 0.0 = no overlap.\n"
         "Top 3 candidates per JD are selected. Ties broken alphabetically."),
    ]

    for title, body in steps:
        f = card(inner, pady=5)
        tk.Label(f, text=title, font=("Arial", 10, "bold"),
                 bg=WHITE, fg=BLUE).pack(anchor="w", padx=14, pady=(10, 3))
        tk.Label(f, text=body, font=("Courier", 9),
                 bg=WHITE, fg="#333", justify="left").pack(anchor="w", padx=14, pady=(0, 10))

    outer.pack(fill="both", expand=True)

# ── TAB 2: Normalized Skills ──────────────────────────────────
def build_skills_tab(parent):
    outer, inner = scrollable_frame(parent)
    section_label(inner, "Candidate Skills — After Normalization & Deduplication")

    # header row
    hdr = tk.Frame(inner, bg=DARK)
    hdr.pack(fill="x", padx=24, pady=(0, 2))
    for col, w in [("#", 4), ("Candidate", 18), ("Normalized Skills", 55), ("N", 5)]:
        tk.Label(hdr, text=col, font=("Arial", 9, "bold"),
                 bg=DARK, fg=WHITE, width=w, anchor="w").pack(side="left", padx=4, pady=6)

    for i, (name, skills) in enumerate(resumes):
        row_bg = WHITE if i % 2 == 0 else "#f8f9ff"
        row = tk.Frame(inner, bg=row_bg, relief="flat", bd=0)
        row.pack(fill="x", padx=24)
        tk.Frame(inner, height=1, bg="#eee").pack(fill="x", padx=24)

        tk.Label(row, text=f"{i+1:02d}", font=("Arial", 9),
                 bg=row_bg, fg=GREY, width=4, anchor="w").pack(side="left", padx=4, pady=7)
        tk.Label(row, text=name, font=("Arial", 9, "bold"),
                 bg=row_bg, width=18, anchor="w").pack(side="left", padx=4)
        tk.Label(row, text=", ".join(skills), font=("Arial", 9),
                 bg=row_bg, fg="#2563eb", anchor="w", wraplength=480, justify="left").pack(side="left", padx=4, fill="x", expand=True)
        tk.Label(row, text=str(len(skills)), font=("Arial", 9, "bold"),
                 bg=row_bg, fg=DARK, width=5).pack(side="left", padx=4)

    outer.pack(fill="both", expand=True)

# ── TAB 3: IDF Values ────────────────────────────────────────
def build_idf_tab(parent):
    outer, inner = scrollable_frame(parent)
    section_label(inner, "IDF Values — Skill Rarity Across All Resumes")

    tk.Label(inner,
             text="IDF = ln(10 / df)   |   Higher IDF = rarer skill = more discriminating",
             font=("Arial", 9, "italic"), bg=BG, fg=GREY).pack(anchor="w", padx=24, pady=(0, 8))

    hdr = tk.Frame(inner, bg=DARK)
    hdr.pack(fill="x", padx=24, pady=(0, 2))
    for col, w in [("Skill", 28), ("df (resumes)", 14), ("IDF Score", 12), ("Rarity", 20)]:
        tk.Label(hdr, text=col, font=("Arial", 9, "bold"),
                 bg=DARK, fg=WHITE, width=w, anchor="w").pack(side="left", padx=4, pady=6)

    rarity_label = {1: "Very rare ↑ high weight", 2: "Uncommon",
                    3: "Moderately common", 6: "Very common ↓ low weight"}

    for i, s in enumerate(word_list):
        df_val  = doc_freq[s]
        idf_val = idf_scores[s]
        row_bg  = WHITE if i % 2 == 0 else "#f8f9ff"
        row = tk.Frame(inner, bg=row_bg)
        row.pack(fill="x", padx=24)
        tk.Frame(inner, height=1, bg="#eee").pack(fill="x", padx=24)

        rarity = rarity_label.get(df_val, "Common")
        color  = "#16a34a" if df_val == 1 else ("#ca8a04" if df_val <= 3 else "#dc2626")

        tk.Label(row, text=s, font=("Arial", 9), bg=row_bg,
                 fg="#2563eb", width=28, anchor="w").pack(side="left", padx=4, pady=5)
        tk.Label(row, text=str(df_val), font=("Arial", 9),
                 bg=row_bg, width=14, anchor="w").pack(side="left", padx=4)
        tk.Label(row, text=f"{idf_val:.4f}", font=("Courier", 9, "bold"),
                 bg=row_bg, fg=DARK, width=12, anchor="w").pack(side="left", padx=4)
        tk.Label(row, text=rarity, font=("Arial", 9),
                 bg=row_bg, fg=color, width=20, anchor="w").pack(side="left", padx=4)

    outer.pack(fill="both", expand=True)

# ── TAB 4: Results ───────────────────────────────────────────
def build_results_tab(parent):
    outer, inner = scrollable_frame(parent)
    section_label(inner, "Matching Results — Cosine Similarity Scores")

    results = run_matching()

    for jd_id, jd_label, scores in results:
        # JD header card
        hdr_card = card(inner, pady=8)
        top_bar = tk.Frame(hdr_card, bg=DARK)
        top_bar.pack(fill="x")
        tk.Label(top_bar, text=f"  {jd_id}  —  {jd_label}",
                 font=("Arial", 11, "bold"), bg=DARK, fg=WHITE).pack(side="left", pady=8)

        # score rows
        max_score = scores[0][1] if scores[0][1] > 0 else 1
        for i, (name, score) in enumerate(scores):
            is_top = i < 3
            row_bg = "#f0fdf4" if is_top else WHITE
            row = tk.Frame(hdr_card, bg=row_bg)
            row.pack(fill="x", padx=2)
            tk.Frame(hdr_card, height=1, bg="#eee").pack(fill="x")

            medal = MEDALS[i] if is_top else "  "
            tk.Label(row, text=f" {i+1:2d}  {medal}", font=("Arial", 9),
                     bg=row_bg, width=8).pack(side="left", pady=6)
            tk.Label(row, text=name, font=("Arial", 9, "bold" if is_top else "normal"),
                     bg=row_bg, width=18, anchor="w").pack(side="left")

            # bar
            bar_outer = tk.Frame(row, bg="#e0e7ff", height=10, width=300)
            bar_outer.pack(side="left", padx=8, pady=8)
            bar_outer.pack_propagate(False)
            bar_w = int((score / max_score) * 300) if max_score > 0 else 0
            bar_color = GREEN if is_top else BLUE
            tk.Frame(bar_outer, bg=bar_color, width=bar_w, height=10).pack(side="left")

            tk.Label(row, text=f"{score:.4f}", font=("Courier", 9, "bold" if is_top else "normal"),
                     bg=row_bg, fg=DARK if is_top else GREY, width=8).pack(side="left")

        # top 3 summary
        top3_line = ",  ".join(f"{n} ({s:.2f})" for n, s in scores[:3])
        summary = tk.Frame(hdr_card, bg="#dcfce7")
        summary.pack(fill="x", padx=2, pady=(4, 0))
        tk.Label(summary, text=f"  ✅ Top 3:  {top3_line}",
                 font=("Arial", 9, "bold"), bg="#dcfce7", fg="#166534").pack(anchor="w", pady=6)

    outer.pack(fill="both", expand=True)

# ── MAIN WINDOW ───────────────────────────────────────────────
def main():
    root = tk.Tk()
    root.title("Resume Matching Engine — Redrob AI Campus Hackathon")
    root.geometry("860x640")
    root.configure(bg=DARK)

    # title bar
    title_bar = tk.Frame(root, bg=DARK, pady=14)
    title_bar.pack(fill="x")
    tk.Label(title_bar, text="Resume Matching Engine",
             font=("Arial", 16, "bold"), bg=DARK, fg=WHITE).pack()
    tk.Label(title_bar, text="TF-IDF Cosine Similarity  ·  10 Candidates  ·  3 Job Descriptions",
             font=("Arial", 9), bg=DARK, fg="#aab").pack()

    # notebook tabs
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TNotebook",        background=DARK, borderwidth=0)
    style.configure("TNotebook.Tab",    background="#2a2a4a", foreground=WHITE,
                    padding=[14, 7], font=("Arial", 9, "bold"))
    style.map("TNotebook.Tab",
              background=[("selected", BLUE)],
              foreground=[("selected", WHITE)])

    notebook = ttk.Notebook(root)
    notebook.pack(fill="both", expand=True, padx=0, pady=0)

    tabs = [
        ("📖  How It Works",    build_how_it_works),
        ("🧹  Normalized Skills", build_skills_tab),
        ("📊  IDF Values",       build_idf_tab),
        ("🏆  Results",          build_results_tab),
    ]

    for tab_name, builder in tabs:
        frame = tk.Frame(notebook, bg=BG)
        notebook.add(frame, text=tab_name)
        builder(frame)

    root.mainloop()

main()