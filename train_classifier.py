import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
import os

def train_classifier(data_csv="data/extracted_texts.csv"):
    df = pd.read_csv(data_csv)

    # Drop empty or very short texts
    df = df[df["text"].str.len() > 100]

    X = df["text"]
    y = df["category"]

    # Split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # TF-IDF
    vectorizer = TfidfVectorizer(max_features=3000, stop_words='english')
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)

    # Model
    clf = LogisticRegression(max_iter=1000)
    clf.fit(X_train_vec, y_train)

    # Evaluate
    y_pred = clf.predict(X_test_vec)
    print("📊 Classification Report:")
    print(classification_report(y_test, y_pred))

    # Save
    os.makedirs("models", exist_ok=True)
    joblib.dump(clf, "models/resume_classifier.pkl")
    joblib.dump(vectorizer, "models/vectorizer.pkl")
    print("✅ Model and vectorizer saved to 'models/' folder.")

if __name__ == "__main__":
    train_classifier()
