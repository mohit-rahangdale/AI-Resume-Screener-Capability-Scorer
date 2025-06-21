import os
import pandas as pd

def generate_labels(data_dir="data", output_csv="data/labels.csv"):
    entries = []
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith(".pdf"):
                full_path = os.path.join(root, file)
                relative_path = os.path.relpath(full_path, data_dir)
                category = os.path.basename(os.path.dirname(full_path))
                entries.append({
                    "path": relative_path.replace("\\", "/"),
                    "category": category
                })

    df = pd.DataFrame(entries)
    df.to_csv(output_csv, index=False)
    print(f"✅ Saved {len(df)} entries to {output_csv}")

if __name__ == "__main__":
    generate_labels()
