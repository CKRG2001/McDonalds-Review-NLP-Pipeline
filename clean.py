import re


def clean_text(text):
    try:
        text = str(text)
        text = re.sub(r"ï¿½+", " ", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()
    except Exception as e:
        print(f"Cleaning error: {e}")
        return ""
