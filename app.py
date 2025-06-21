import streamlit as st
import pandas as pd
import joblib
import os
import tempfile
from parser import extract_pdf_text
from scorer import compute_capability_score

# Load models
clf = joblib.load("models/resume_classifier.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

st.set_page_config(page_title="AI Resume Screener", layout="wide")
st.title("📄 Resume Screener & Capability Scorer")

uploaded_files = st.file_uploader("Upload Resume PDFs", type="pdf", accept_multiple_files=True)

if uploaded_files:
    results = []

    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        # Extract resume text
        text = extract_pdf_text(tmp_path)

        # Predict category
        X_vec = vectorizer.transform([text])
        pred_category = clf.predict(X_vec)[0]

        # Capability score
        score, years = compute_capability_score(text, pred_category)
        score_percent = f"{score}%"
        experience_str = "Fresher" if years == 0 else f"{years} yrs"

        results.append({
            
            "Filename": uploaded_file.name,
            "Predicted Role": pred_category,
            "Capability (%)": score_percent,
            "Experience": experience_str,
            "ScoreForSorting": score,
            "PDF Path": tmp_path
        })

    # Sort by score (but don’t show the raw score)
    results_df = pd.DataFrame(results).sort_values(by="ScoreForSorting", ascending=False)

    # Show resultsst.subheader("🔍 Results")
    st.markdown("*Capability Score shown as a percentage out of 100*")
    st.dataframe(results_df[["Filename", "Predicted Role", "Capability (%)", "Experience"]], use_container_width=True)


    # Resume preview section
    st.subheader("📄 Preview Resume")
    selected = st.selectbox("Select a resume to preview:", results_df["Filename"].tolist())

    if selected:
        selected_path = results_df[results_df["Filename"] == selected]["PDF Path"].values[0]
        with open(selected_path, "rb") as f:
            pdf_bytes = f.read()

        st.download_button("⬇ Download Resume", data=pdf_bytes, file_name=selected, mime="application/pdf")
        st.markdown("---")
        st.components.v1.iframe(f"file://{selected_path}", height=600, scrolling=True)

