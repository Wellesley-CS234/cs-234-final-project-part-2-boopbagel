import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Conclusions", layout="wide")
df = pd.read_csv('umapVisual.csv')


st.title("Conclusions")