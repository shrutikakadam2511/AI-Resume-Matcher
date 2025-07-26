import streamlit as st
from utils import extract_text_from_pdf, extract_text_from_docx, clean_text, get_similarity_score

st.set_page_config(page_title="Resume Scanner", layout="centered")
st.title("📄 AI Resume Matcher")

uploaded_resume = st.file_uploader("Upload Resume (PDF or DOCX)", type=["pdf", "docx"])
jd_input = st.text_area("Paste the Job Description", height=200)

if st.button("Match Resume"):
    if uploaded_resume and jd_input:
        if uploaded_resume.name.endswith(".pdf"):
            resume_text = extract_text_from_pdf(uploaded_resume)
        else:
            resume_text = extract_text_from_docx(uploaded_resume)
        
        cleaned_resume = clean_text(resume_text)
        cleaned_jd = clean_text(jd_input)

        score = get_similarity_score(cleaned_resume, cleaned_jd)
        st.success(f"🧠 Resume Match Score: **{score}%**")

        if score >= 70:
            st.balloons()
            st.markdown("✅ Good Match!")
        elif score >= 40:
            st.markdown("⚠️ Decent Match, needs improvement.")
        else:
            st.markdown("❌ Poor Match. Consider editing your resume.")
    else:
        st.error("Please upload a resume and paste the job description.")
