import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
    #raw data preview
rawCols = ['QID', 'PageTitle', 'description', 'occupation_labels']

st.set_page_config(page_title="Mapping Wikipedia Female Scientists", layout="wide")
df = pd.read_csv('umapVisual.csv', usecols=rawCols)


st.title("Cluster Visualization of Female Scientists on Wikipedia")
    #research question
st.header(""" *Research Question:* """)
st.write("How well does unsupervised clustering work on female scientists based on short descriptions gathered from WikIData API calls? Will any biases or trends emerge?")
st.markdown("To answer this question, data was collected using the Wikimedia API client on the WikiProject Women Scientists. Out of 27k total articles, the first 16.5k articles were collected, with the rest ommitted for  being rated as 'start' or 'stub' with a rating of '???'. This was  done due to time constraints and ensuring the pages collected would have enough information.")
st.markdown("QIDs (the identifier for articles), page titles, descriptions, and occupation labels were collected and organized in a CSV file.")
st.markdown("Check out the [WikiProject Women Scientists Here!](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_Women_scientists)")


st.header("Preview or Search The Collected Raw Data!")
columnSearch = st.selectbox("choose a column to search", options=['PageTitle','description', 'occupation_labels'])
search = st.text_input("Search:", "")
if search:
    results = df[df[columnSearch].astype(str).str.contains(search, case=False, na=False)]
    st.markdown(f"Found {len(results)} results for '{search}' in column '{columnSearch}':")
    st.table(results[rawCols].head(10))
else:
    st.markdown("Displaying 10 random rows of the raw data:")
    randomIndex = np.random.randint(0, df.shape[0] - 10)
    if st.button("Reshuffle random columns"):
        randomIndex = np.random.randint(0, df.shape[0] - 10)
    st.info("Use the search box to explore the data")
    st.table(df.iloc[randomIndex:randomIndex+10, 1:6])

st.markdown("Navigate to the Analysis page in the sidebar to learn more about the data!")
