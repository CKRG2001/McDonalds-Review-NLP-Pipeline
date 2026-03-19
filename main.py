import pandas as pd
import os
import re
import time
from transformers import pipeline
from dotenv import load_dotenv

load_dotenv()
# ----------------------------------------
# get model name from .env file and load model
# ----------------------------------------
model = os.getenv("model")
sentiment_pipeline = pipeline("sentiment-analysis", model=model)


# ----------------------------------------
# clean text function
# ----------------------------------------
def clean_text(text):
    try:
        text = str(text)
        text = re.sub(r"ï¿½+", " ", text)  # target corruption only
        text = re.sub(r"\s+", " ", text)
        return text.strip()
    except Exception as e:
        print(f"Cleaning error: {e}")
        return " "


# ----------------------------------------
# Sentiment classification funtion
# ----------------------------------------
def get_senti_batch(texts, batch_size=64, threshold=0.75):

    cleaned = [clean_text(x) for x in texts]

    results = ["na"] * len(cleaned)

    valid_indices = [i for i, t in enumerate(cleaned) if t]
    valid_texts = [cleaned[i] for i in valid_indices]

    if valid_texts:
        predictions = sentiment_pipeline(
            valid_texts,
            truncation=True,
            batch_size=batch_size,
        )
        for i, pred in zip(valid_indices, predictions):
            if pred["label"] == "POSITIVE":
                results[i] = "positive" if pred["score"] > threshold else "neutral"
            else:
                results[i] = "negative" if pred["score"] > threshold else "neutral"
    return results


# ----------------------------------------
# Reading the pandas file
# ----------------------------------------
df = pd.read_csv("Data/McDonald_s_Reviews.csv", encoding="latin-1")
start = time.time()
print(start)
df["sentiment"] = get_senti_batch(df["review"].tolist())
print(time.time() - start)
print(df.sentiment.value_counts())
# ----------------------------------------
# Savig the results into CSV
# ----------------------------------------
os.makedirs("Output", exist_ok=True)
df.to_csv("Output/McDonald_s_Reviews_sentiment.csv", index=False)
