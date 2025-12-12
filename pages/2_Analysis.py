import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.set_page_config(page_title="Female Scientists KMeans Clustering", layout="wide")
df = pd.read_csv('umapVisual.csv')
df2 = pd.read_csv('clustered_noAmerican.csv')

st.title("Exploring the dataset")
st.markdown("Descriptions were analyzed using SentanceTransformer to generate embeddings to determine which scientists had similar descriptions and attempt to group them together in 'clusters'. This allows us to see *1)* how well the descriptions capture the work of the scientists, and *2)* what patterns emerge in the clusters.")
st.markdown("The optimal number of clusters was determined using the 'elbow method', which suggested that 50-150 clusters would be appropriate. 60 was chosen to allow for more granular clusters, while avoiding overfitting or too many small clusters.")
st.markdown("The computed cluster groups and top words for each cluster (computed using CountVectorizer) can be seen below.")

with st.expander("Show unique clusters"):
    st.table(df[['cluster','topClusterWords']].drop_duplicates().sort_values(by='cluster').reset_index(drop=True))
st.markdown("""Fascinatingly, the word 'american' appears in 47 out of 60 clusters, suggesting a __strong representation of American women.__ Inversely, however, this also means that women of other nationalities are:
             *1)* underrepresented on Wikipedia *2)* will be more likely to be found in the, say, 'african' cluster (cluster 50) rather than one that represents their occupation.
             \n To attempt to correct for this bias, which effectively groups american women on their occupations and other women on their *non-americanness*, we can remove the word 'american' from our clustering analysis. """)

with st.expander("Show unique clusters after removing 'american' from descriptions"):
    st.table(df2[['cluster','topClusterWords']].drop_duplicates().sort_values(by='cluster').reset_index(drop=True))
st.markdown("'American' is still present in 9 clusters, mostly due to hyphenated forms like 'African-American' or 'Chinese-American' that were not removed. However, this is a significant reduction from before, and now we can visually compare the difference in these!")


st.header("KMeans Clustering Visualization")
st.markdown("The clusters were generated using KMeans embeddings from SentenceTransformer, then visualized using UMAP dimensionality reduction, which transforms the 16k-dimension data (lol) into 2-dimensions.")
st.info("Zoom in on each dataset to see the clusters more clearly!")

tab1, tab2 = st.tabs(["Original Data", "Without 'American'"])

with tab1:
    fig = px.scatter(df, x='umap_x', y='umap_y', color='cluster', color_continuous_scale= 'mygbm', hover_data={'umap_x': False, 'umap_y': False, 'QID': False, 'PageTitle': True, 'description': True, 'occupation_labels':True, 'topClusterWords':True}, title="KMeans Clustering of Female Scientists on Wikipedia", opacity=0.6, width=800, height=800)
    fig.update_traces(marker=dict(size=4))
    fig.update_layout(xaxis_visible=False, yaxis_visible=False)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("silhoutte score = 0.12987")


with tab2:
    fig = px.scatter(df2, x='umap_x', y='umap_y', color='cluster', color_continuous_scale= 'mygbm', hover_data={'umap_x': False, 'umap_y': False, 'QID': False, 'PageTitle': True, 'description': True, 'occupation_labels':True, 'topClusterWords':True}, title="KMeans Clustering of Female Scientists on Wikipedia", opacity=0.6, width=800, height=800)
    fig.update_traces(marker=dict(size=4))
    fig.update_layout(xaxis_visible=False, yaxis_visible=False)
    st.plotly_chart(fig, use_container_width=True)
    st.markdown("silhoutte score = 0.0.15012 (15.58% improvement)")


with st.expander("What is the silhoutte score?"):
    st.info("the silhoutte score, ranging from -1.0 to 1.0, measures how similar an object is to its assigned cluster. Values closer to 1 indicate better-defined clusters, while values near 0 indicate overlapping clusters and that a point may be near the boundary for two different clusters.")

st.markdown("Want to explore the raw data?")
tabA, tabB = st.tabs(["Original Data", "Without 'American'"])

visCols = ['PageTitle','description','occupation_labels','cluster','topClusterWords',]
randomIndex = np.random.randint(0, df.shape[0] - 10)

with tabA:
        colSearch = st.selectbox("choose a column to search", options=visCols, key='tabA')
        search = st.text_input("Search:", "", key='tabAsearch')

        if search:
            results = df[df[colSearch].astype(str).str.contains(search, case=False, na=False)]
            st.markdown(f"Found {len(results)} results for '{search}' in column '{colSearch}':")
            st.table(results[visCols].head(10))
        else:
            st.markdown("Displaying 10 random rows of the raw data:")
            if st.button("Reshuffle random columns", key='reshuffleA'):
                randomIndex = np.random.randint(0, df.shape[0] - 10)
            st.table(df.iloc[randomIndex:randomIndex+10, 1:6])

with tabB:
        colSearch2 = st.selectbox("choose a column to search", options=visCols, key='tabB')
        search2 = st.text_input("Search:", "", key='tabBsearch')

        if search2:
            results2 = df2[df2[colSearch2].astype(str).str.contains(search2, case=False, na=False)]
            st.markdown(f"Found {len(results2)} results for '{search2}' in column '{colSearch2}':")
            st.table(results2[visCols].head(10))
        else:
            st.markdown("Displaying 10 random rows of the raw data:")
            if st.button("Reshuffle random columns", key='reshuffleB'):
                randomIndex = np.random.randint(0, df.shape[0] - 10)
            st.table(df2.iloc[randomIndex:randomIndex+10, 1:6])

