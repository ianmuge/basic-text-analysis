import streamlit as st
import numpy as np
import pandas as pd
import re


def extract_hashtags(tweet):
    return re.findall(r"#\w+", tweet)
def extract_mentions(tweet):
    return re.findall(r"@\w+", tweet)


st.title('My first app')
df = pd.read_csv("./data/sample.csv")
st.dataframe(df)
st.write(df.columns)
tweets = df["Tweet Content"]
st.write(tweets.head())
st.write(extract_hashtags(tweets[0]))
st.write(extract_mentions(tweets[2]))
