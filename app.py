import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

st.title("Sentiment Analysis of Tweets about US Airlines")
st.sidebar.title("Sentiment Analysis of Tweets about US Airlines")

st.markdown("This application is a Streamlit dashboard to analyze the sentiment of Tweets 😃")
st.sidebar.markdown("This application is a Streamlit dashboard to analyze the sentiment of Tweets 😃")

DATA_URL = r'C:\Users\91995\OneDrive\Documents\Create-Interactive-Dashboards-with-Streamlit-and-Python\Tweets.csv'

@st.cache_data
def load_data():
    data = pd.read_csv(DATA_URL)
    data['tweet_created'] = pd.to_datetime(data['tweet_created'])
    return data

data = load_data()

# Random tweet
st.sidebar.subheader("Show random tweet")
random_tweet = st.sidebar.radio('Sentiment', ('positive', 'neutral', 'negative'))
st.sidebar.markdown(
    data.query('airline_sentiment == @random_tweet')[['text']].sample(n=1).iat[0, 0]
)

# Sentiment count visualization
st.sidebar.markdown("### Number of Tweets by Sentiment")
select = st.sidebar.selectbox(
    "Visualization type",
    ['Histogram', 'Pie chart'],
    key='vis_type'
)

sentiment_count = data['airline_sentiment'].value_counts()
sentiment_count = pd.DataFrame({
    'Sentiment': sentiment_count.index,
    'Tweets': sentiment_count.values
})

if not st.sidebar.checkbox("Hide", True, key='hide_chart'):
    st.markdown("### Number of Tweets by sentiment")

    if select == "Histogram":
        fig = px.bar(sentiment_count, x='Sentiment', y='Tweets', color='Tweets', height=500)
        st.plotly_chart(fig)
    else:
        fig = px.pie(sentiment_count, values='Tweets', names='Sentiment')
        st.plotly_chart(fig)

# Map visualization
st.sidebar.subheader("When and where are users tweeting from?")
hour = st.sidebar.slider("Hour of day", 0, 23, key='hour_slider')
modified_data = data[data['tweet_created'].dt.hour == hour]

if not st.sidebar.checkbox("Close", True, key='map_close'):
    st.markdown("### Tweets locations based on the time of day")
    st.markdown("%i tweets between %i:00 and %i:00" % (len(modified_data), hour, (hour + 1) % 24))

    # Only works if lat/lon columns exist
    if 'lat' in modified_data.columns and 'lon' in modified_data.columns:
        st.map(modified_data[['lat', 'lon']])
    else:
        st.warning("Map cannot be displayed because 'lat' and 'lon' columns are missing.")

    if st.sidebar.checkbox("Show raw data", False, key='show_raw'):
        st.write(modified_data)

# Breakdown by airline sentiment
st.sidebar.subheader("Breakdown airline tweets by sentiment")
choice = st.sidebar.multiselect(
    "Pick airlines",
    ('US Airways', 'United', 'American', 'Southwest', 'Delta', 'Virgin America'),
    key='airline_choice'
)

if len(choice) > 0:
    choice_data = data[data.airline.isin(choice)]
    fig_choice = px.histogram(
        choice_data,
        x='airline',
        y='airline_sentiment',
        histfunc='count',
        color='airline_sentiment',
        facet_col='airline_sentiment',
        labels={'airline_sentiment': 'tweets'},
        height=600,
        width=800
    )
    st.plotly_chart(fig_choice)

# Word cloud
st.sidebar.header("Word Cloud")
word_sentiment = st.sidebar.radio(
    'Display word cloud for what sentiment?',
    ('positive', 'neutral', 'negative'),
    key='word_sentiment'
)

if not st.sidebar.checkbox("Close", True, key='wordcloud_close'):
    st.header('Word cloud for %s sentiment' % (word_sentiment))
    df = data[data['airline_sentiment'] == word_sentiment]
    words = ' '.join(df['text'])

    processed_words = ' '.join(
        [word for word in words.split()
         if 'http' not in word
         and not word.startswith('@')
         and word != 'RT']
    )

    wordcloud = WordCloud(
        stopwords=STOPWORDS,
        background_color='white',
        height=640,
        width=800
    ).generate(processed_words)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot(plt)