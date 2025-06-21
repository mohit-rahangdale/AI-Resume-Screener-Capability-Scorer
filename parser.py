from pdfminer.high_level import extract_text
from tqdm import tqdm
import pandas as pd
import os

def extract_pdf_text(pdf_path):
    try:
        text = extract_text(pdf_path)
        return text.strip().replace("\n", " ").replace("  ", " ")
    except Exception as e:
        print(f"❌ Error reading {pdf_path}: {e}")
        return ""

# Extract all PDFs with progress bar
def extract_all_texts(label_csv="data/labels.csv", base_path="data"):
    df = pd.read_csv(label_csv)
    results = []

    for i, row in tqdm(df.iterrows(), total=len(df), desc="🔍 Extracting Resumes"):
        pdf_path = os.path.join(base_path, row["path"])
        text = extract_pdf_text(pdf_path)
        results.append({
            "path": row["path"],
            "category": row["category"],
            "text": text
        })

    df_out = pd.DataFrame(results)
    df_out.to_csv("data/extracted_texts.csv", index=False)
    print(f"\n✅ Extracted text for {len(df_out)} resumes.")

if __name__ == "__main__":
    extract_all_texts()


