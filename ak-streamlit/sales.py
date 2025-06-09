import streamlit as st
import pandas as pd

st.markdown("# Chai Sales Dashboard")

file = st.file_uploader("Upload your file",type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)

if file:
    st.subheader("Summary stats")
    st.write(df.describe())

if file:
    cities = df["City"].unique()
    sel_city = st.selectbox("Filter by City", cities)
    filtered_data = df[df["City"] == sel_city]
    st.dataframe(filtered_data)