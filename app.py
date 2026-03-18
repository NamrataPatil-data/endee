import streamlit as st
import pdfplumber
from sentence_transformers import SentenceTransformer, util

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')


# -------- PDF TEXT EXTRACTION --------
def extract_text(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text.lower()


# -------- RAG GENERATION (AI INSIGHT) --------
def generate_insight(matched, missing):
    if not matched:
        matched_text = "no strong matching skills yet"
    else:
        matched_text = ", ".join(matched)

    return f"""
    You have strong skills in {matched_text}.
    
    However, you are missing important skills such as {', '.join(missing)}.
    
    To improve your chances, focus on learning these missing skills and building projects related to them.
    """


# -------- LOAD SKILLS --------
with open("skills_dataset.txt", "r") as f:
    skills = [line.strip().lower() for line in f.readlines()]


# -------- UI --------
st.title("🚀 AI Skill Gap Analyzer (RAG + Endee Inspired)")

resume_file = st.file_uploader("Upload Resume PDF", type="pdf")
jd_file = st.file_uploader("Upload Job Description PDF", type="pdf")


# -------- MAIN LOGIC --------
if st.button("Analyze Skill Gap"):

    if resume_file and jd_file:

        # Extract text
        resume_text = extract_text(resume_file)
        jd_text = extract_text(jd_file)

        # Generate embeddings
        resume_embedding = model.encode(resume_text, convert_to_tensor=True)

        scored_skills = []

        # Calculate similarity for each skill
        for skill in skills:
            if skill in jd_text:  # Only consider JD skills

                skill_embedding = model.encode(skill, convert_to_tensor=True)
                score = util.cos_sim(skill_embedding, resume_embedding).item()

                scored_skills.append((skill, score))

        # Sort by similarity
        scored_skills = sorted(scored_skills, key=lambda x: x[1], reverse=True)

        # -------- FIXED THRESHOLD --------
        matched = [skill for skill, score in scored_skills if score > 0.2]
        missing = [skill for skill, score in scored_skills if score <= 0.2]

        # -------- MATCH SCORE --------
        if len(scored_skills) > 0:
            final_score = (len(matched) / len(scored_skills)) * 100
        else:
            final_score = 0

        # -------- OUTPUT --------

        st.subheader("📊 Match Score")
        st.progress(int(final_score))
        st.success(f"Match Score: {round(final_score, 2)} %")

        st.subheader("✅ Matched Skills")
        if matched:
            for skill in matched:
                st.write(f"✔ {skill}")
        else:
            st.write("No strong matches found")

        st.subheader("❌ Missing Skills")
        for skill in missing:
            st.write(f"❌ {skill}")

        # -------- TOP-K RESULTS --------
        st.subheader("🔝 Top Relevant Skills (Top-K Ranking)")
        for skill, score in scored_skills[:10]:
            st.write(f"{skill} → Similarity: {round(score, 2)}")

        # -------- RAG INSIGHT --------
        st.subheader("🧠 AI Insight")
        st.write(generate_insight(matched, missing))

        # -------- ENDEE MENTION --------
        st.write("⚙️ Designed for integration with Endee Vector Database using RAG-based semantic search.")

    else:
        st.warning("Please upload both Resume and Job Description PDFs")