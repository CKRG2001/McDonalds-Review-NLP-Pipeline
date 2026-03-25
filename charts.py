# charts.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from clean import parse_address


def load_data():
    df = pd.read_csv("Output/McDonald_s_Reviews_sentiment.csv", encoding="latin-1")
    df[["street", "city", "state", "zipcode"]] = df["store_address"].apply(
        parse_address
    )
    df["state"] = df["state"].replace("Las", "LA")
    df["rating"] = (
        df["rating"]
        .str.replace(" stars", "")
        .str.replace(" star", "")
        .str.strip()
        .astype(int)
    )
    return df


def chart1_sentiment(df):
    fig, ax = plt.subplots(figsize=(8, 5))
    colors = {"positive": "#2ecc71", "negative": "#e74c3c", "neutral": "#95a5a6"}
    sentiment_counts = df["sentiment"].value_counts()
    bars = ax.bar(
        sentiment_counts.index,
        sentiment_counts.values,
        color=[colors[s] for s in sentiment_counts.index],
    )
    for bar in bars:
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            bar.get_height() + 100,
            f"{int(bar.get_height()):,}",
            ha="center",
            fontsize=11,
        )
    ax.set_title(
        "Sentiment Distribution of McDonald's Reviews", fontsize=14, fontweight="bold"
    )
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Number of Reviews")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    return fig


def chart2_states(df):
    top10_states = df["state"].value_counts().head(10).index
    state_sentiment = (
        df[df["state"].isin(top10_states)]
        .groupby(["state", "sentiment"])
        .size()
        .unstack(fill_value=0)
    )
    state_sentiment["total"] = state_sentiment.sum(axis=1)
    state_sentiment = state_sentiment.sort_values("total", ascending=False).drop(
        columns="total"
    )
    state_sentiment = state_sentiment[["negative", "neutral", "positive"]]
    state_sentiment_pct = state_sentiment.div(state_sentiment.sum(axis=1), axis=0) * 100

    fig, ax = plt.subplots(figsize=(12, 6))
    colors = ["#e74c3c", "#95a5a6", "#2ecc71"]
    state_sentiment_pct.plot(kind="bar", stacked=True, color=colors, ax=ax, width=0.7)

    for i, state in enumerate(state_sentiment_pct.index):
        cumulative = 0
        for sentiment in ["negative", "neutral", "positive"]:
            value = state_sentiment_pct.loc[state, sentiment]
            if value > 3:
                ax.text(
                    i,
                    cumulative + value / 2,
                    f"{value:.1f}%",
                    ha="center",
                    va="center",
                    fontsize=8,
                    fontweight="bold",
                    color="white",
                )
            cumulative += value

    ax.set_title("Top 10 States by Sentiment %", fontsize=14, fontweight="bold")
    ax.set_xlabel("State")
    ax.set_ylabel("Percentage of Reviews")
    ax.legend(title="Sentiment", bbox_to_anchor=(1.05, 1))
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f"{x:.0f}%"))
    plt.xticks(rotation=45)
    plt.tight_layout()
    return fig


def chart3_issues(df):
    issue_df = df[df["sentiment"] == "negative"].dropna(subset=["issue_label"])
    issue_counts = issue_df["issue_label"].value_counts()

    fig, ax = plt.subplots(figsize=(10, 6))
    colors = sns.color_palette("Reds_r", len(issue_counts))
    bars = ax.barh(issue_counts.index, issue_counts.values, color=colors)

    for bar in bars:
        ax.text(
            bar.get_width() + 30,
            bar.get_y() + bar.get_height() / 2,
            f"{int(bar.get_width()):,}",
            va="center",
            fontsize=10,
        )

    ax.set_title(
        "Most Common Issues in Negative Reviews", fontsize=14, fontweight="bold"
    )
    ax.set_xlabel("Number of Reviews")
    ax.set_ylabel("Issue Category")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    return fig


def chart4_cities(df):
    negative_cities = df[df["sentiment"] == "negative"]["city"].value_counts().head(10)

    fig, ax = plt.subplots(figsize=(10, 6))
    colors = sns.color_palette("Reds_r", len(negative_cities))
    bars = ax.barh(negative_cities.index, negative_cities.values, color=colors)

    for bar in bars:
        ax.text(
            bar.get_width() + 10,
            bar.get_y() + bar.get_height() / 2,
            f"{int(bar.get_width()):,}",
            va="center",
            fontsize=10,
        )

    ax.set_title(
        "Top 10 Cities with Most Negative Reviews", fontsize=14, fontweight="bold"
    )
    ax.set_xlabel("Number of Negative Reviews")
    ax.set_ylabel("City")
    ax.invert_yaxis()
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    plt.tight_layout()
    return fig
