import streamlit as st
import pandas as pd

st.markdown("# Chai Sales Dashboard")

file = st.file_uploader("Upload your file",type=["csv"])

if file:
    df = pd.read_csv(file)
    st.subheader("Data Preview")
    st.dataframe(df)