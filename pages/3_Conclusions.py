import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Conclusions", layout="wide")
df = pd.read_csv('umapVisual.csv')


st.title("Conclusions")
st.markdown("""All in all, the short descriptions gathered from articles in WikiProject Women Scientists are brief and helpful to humans to gain a surface-level understanding,
            but can be poor indicators of women’s work and achievements when attempting to gain a broader understanding of the community of women scientists making up this project from a data science standpoint.
            A major bias favoring American women was uncovered– which is understandable, considering the majority of wikipedia users are English-speaking Americans, but highlights a noticeable disparity,
            particularly when it comes to honoring the achievements of women of color in science. The silhouette score results of the kmeans clustering were only slightly in the positive range,
            indicating it isnt *terrible*, but not quite ‘good’, which makes sense considering the size of the sample and the diversity between brief descriptions. It did increase by ~15% when removing the word ‘american’,
            but that isn’t truly a fix for the American bias and only serves to group these women more effectively.""")