import streamlit as st
from charts import (
    load_data,
    chart1_sentiment,
    chart2_states,
    chart3_issues,
    chart4_cities,
)

# Page config
st.set_page_config(
    page_title="McDonald's Review Dashboard", page_icon="🍔", layout="wide"
)


# Load data
@st.cache_data
def get_data():
    return load_data()


df = get_data()

# Header
st.title("🍔 McDonald's Review Dashboard")
st.markdown("Analysis of **33,396 reviews** across the United States")
# st.divider()
st.markdown("----")

# Filters in sidebar
st.sidebar.header("Filters")

# state filter
all_states = ["All"] + sorted(df["state"].dropna().unique().tolist())
selected_state = st.sidebar.selectbox("Select State", all_states)

# sentiment filter
# selected_sentiment = st.sidebar.selectbox(
#     "Select Sentiment", ["All", "positive", "negative", "neutral"]
# )

# apply filters
filtered_df = df.copy()
if selected_state != "All":
    filtered_df = filtered_df[filtered_df["state"] == selected_state]
# if selected_sentiment != "All":
#     filtered_df = filtered_df[filtered_df["sentiment"] == selected_sentiment]

# KPI metrics at top
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Reviews", f"{len(filtered_df):,}")
col2.metric("Negative Reviews", f"{(filtered_df['sentiment'] == 'negative').sum():,}")
col3.metric("Positive Reviews", f"{(filtered_df['sentiment'] == 'positive').sum():,}")
col4.metric("Avg Rating", f"{filtered_df['rating'].mean():.1f} ⭐")

# st.divider()
st.markdown("----")

# Charts
col1, col2 = st.columns(2)

with col1:
    st.subheader("Sentiment Distribution")
    st.pyplot(chart1_sentiment(filtered_df))

with col2:
    st.subheader("Top 10 States by Sentiment")
    st.pyplot(chart2_states(filtered_df))

col3, col4 = st.columns(2)

with col3:
    st.subheader("Issue Breakdown (Negative Reviews)")
    st.pyplot(chart3_issues(filtered_df))

with col4:
    st.subheader("Top 10 Cities with Most Negative Reviews")
    st.pyplot(chart4_cities(filtered_df))
