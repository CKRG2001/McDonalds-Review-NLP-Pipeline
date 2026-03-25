import re
import pandas as pd


def clean_text(text):
    try:
        text = str(text)
        text = re.sub(r"ï¿½+", " ", text)
        text = re.sub(r"\s+", " ", text)
        return text.strip()
    except Exception as e:
        print(f"Cleaning error: {e}")
        return ""


# funtion to parse address
def parse_address(address):
    try:
        parts = [i.strip() for i in address.split(",")]
        street = ", ".join(parts[:-3])
        city = parts[-3]
        state = parts[-2].split(" ")[0]
        zipcode = parts[-2].split(" ")[1]

        return pd.Series(
            {"street": street, "city": city, "state": state, "zipcode": zipcode}
        )
    except Exception as e:
        print(f"Error parsing address {e}")
        return pd.Series(
            {"street": "None", "city": "None", "state": "None", "zipcode": "None"}
        )
