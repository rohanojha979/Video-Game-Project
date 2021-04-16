import streamlit as st
import pandas as pd

df = pd.read_csv("vgsales.csv")

st.title("Video Game Sales Analysis")
st.markdown("![alt text] (https://img.etimg.com/thumb/msid-79058608,width-640,resizemode-4,imgsize-107012/the-journey-of-video-games.jpg)")

st.dataframe(df)

sidebar = st.sidebar

sidebar.header("choose your action")
