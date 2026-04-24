import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# load data
base_path = os.path.dirname(__file__)
file_path = os.path.join(base_path, 'spotify.csv')

def load_data():
    df = pd.read_csv("spotify.csv")
    df = df.dropna()
    return df

df = load_data()


# title
st.title("Spotify Data Dashboard")
st.write("Analisis data musik pada spotify")

# logo
LOGO = "logo.png"

# sidebar
st.sidebar.image("logo.png", width=1000)
st.sidebar.header("Filter Tipe Album") 
tipe_album = st.sidebar.selectbox("Pilih tipe album", df['album_type'].unique())

# filter
df_filtered = df[df['album_type'] == tipe_album]

# preview data 10 rows
st.subheader("Data Preview")
st.dataframe(df_filtered.head(10))

# distribusi top 10 artist
st.subheader("Distribusi Top 10 Artist")
top_artist = df_filtered['artist_name'].value_counts().head(10)
fig1, ax1 = plt.subplots()
sns.barplot(x=top_artist.values, y=top_artist.index, ax=ax1)
st.pyplot(fig1)


# proporsi lagu explicit vs non explicit
st.subheader("Proporsi Lagu Explicit VS Non Explicit")
fig2, ax2 = plt.subplots()
df_filtered['explicit'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax2)
st.pyplot(fig2)

# history popularity
st.subheader("History Lagu Popular")
fig3, ax3 = plt.subplots()
sns.histplot(df_filtered['track_popularity'], bins=10, ax=ax3)
st.pyplot(fig3)

# top 10 genree
st.subheader("Distribusi Top 10 Genres")
top_genre = df_filtered['artist_genres'].value_counts().head(10)
fig4, ax4 = plt.subplots()
sns.barplot(x=top_genre.values, y=top_genre.index, ax=ax4)
st.pyplot(fig4)
