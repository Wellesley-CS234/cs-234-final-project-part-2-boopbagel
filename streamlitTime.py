import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Female Scientists KMeans Clustering", layout="wide")
df = pd.read_csv('umapVisual.csv')

st.title("Cluster Visualization of Female Scientists on Wikipedia")
#research question
st.header(""" ###Research Question: ### \n
            How well does unsupervised clustering work on female scientists based on short descriptions gathered from WikIData API calls?""")

#raw data preview
rawCols = ['QID', 'PageTitle', 'description', 'occupation_labels']

st.header("Preview or Search The Collected Raw Data:")
columnSearch = st.selectbox("choose a column to search", options=rawCols)
search = st.text_input("Search:", "")
if search:
    results = df[df[columnSearch].astype(str).str.contains(search, case=False, na=False)]
    st.markdown(f"Found {len(results)} results for '{search}' in column '{columnSearch}':")
    st.dataframe(results[[rawCols]])
else:
    st.markdown("Displaying the first 25 rows of the raw data:")
    st.info("Use the search box to look through the data!")
    st.table(df.head(25)[[rawCols]])

fig = px.scatter(df, x='umap_x', y='umap_y', color='cluster', hover_data={'umap_x': False, 'umap_y': False, 'QID': False, 'PageTitle': True, 'description': True, 'occupation_labels':True, 'topClusterWords':True}, title="KMeans Clustering of Female Scientists on Wikipedia", opacity=0.6, width=800, height=800)
fig.update_traces(marker=dict(size=4))
fig.update_layout(xaxis_visible=False, yaxis_visible=False)
st.plotly_chart(fig, use_container_width=True)