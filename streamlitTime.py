import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Female Scientists KMeans Clustering", layout="wide")

st.title("Cluster Visualization of Female Scientists on Wikipedia")
st.markdown(""" ###Research Question:
            How well does unsupervised clustering work on female scientists based on short descriptions gathered from WikIData API calls?""")

df = pd.read_csv('umapVisual.csv')
fig = px.scatter(df, x='umap_x', y='umap_y', color='cluster', color_continuous_scale='mygbm', hover_data={'umap_x': False, 'umap_y': False, 'QID': False, 'PageTitle': True, 'description': True, 'occupation_labels':True, 'topClusterWords':True}, title="KMeans Clustering of Female Scientists on Wikipedia", opacity=0.6)
fig.update_traces(marker=dict(size=4))
fig.update_layout(xaxis_visible=False, yaxis_visible=False)
st.plotly_chart(fig, use_container_width=True)