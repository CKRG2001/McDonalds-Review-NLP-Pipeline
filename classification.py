from transformers import pipeline

classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

labels = [
    "cold or bad food",
    "wrong or missing order",
    "rude or slow staff",
    "long wait time",
    "dirty or unhygienic",
    "overpriced",
    "app or ordering issue",
    "management problem",
]


def get_label_batch(texts, batch_size=16):
    results = []
    for text in texts:
        result = classifier(text, candidate_labels=labels, multi_label=True)
        results.append(result["labels"][0])
    return results
