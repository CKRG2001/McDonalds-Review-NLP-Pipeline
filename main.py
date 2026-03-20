import pandas as pd
import time
import os
from dotenv import load_dotenv

load_dotenv()
from sentiment import get_senti_batch
from classification import get_label_batch


# load data
df = pd.read_csv("Data/McDonald_s_Reviews.csv", encoding="latin-1")

# sentiment
print("Sentiment Started")
start = time.time()
df["sentiment"] = get_senti_batch(df["review"].tolist())
print(f"Sentiment done in {time.time() - start:.2f}s")

# label only negative reviews
negative_mask = df["sentiment"] == "negative"
df.loc[negative_mask, "issue_label"] = get_label_batch(
    df[negative_mask]["review"].tolist()
)

# save
os.makedirs("Output", exist_ok=True)
df.to_csv("Output/McDonald_s_Reviews_sentiment.csv", index=False)
print("Done!")
