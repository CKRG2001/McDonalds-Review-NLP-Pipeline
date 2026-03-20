from transformers import pipeline
from clean import clean_text
import os

sentiment_pipeline = pipeline("sentiment-analysis", model=os.getenv("model"))


def get_senti_batch(texts, batch_size=64, threshold=0.75):
    cleaned = [clean_text(x) for x in texts]
    results = ["na"] * len(cleaned)
    valid_indices = [i for i, t in enumerate(cleaned) if t]
    valid_texts = [cleaned[i] for i in valid_indices]
    if valid_texts:
        predictions = sentiment_pipeline(
            valid_texts, truncation=True, batch_size=batch_size
        )
        for i, pred in zip(valid_indices, predictions):
            print(i)
            if pred["label"] == "POSITIVE":
                results[i] = "positive" if pred["score"] > threshold else "neutral"
            else:
                results[i] = "negative" if pred["score"] > threshold else "neutral"
    return results
