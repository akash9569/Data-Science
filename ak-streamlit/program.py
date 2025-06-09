import streamlit as st

st.title("Hello Programming App")
st.subheader("Brewed with streamlit")
st.text("Welcome to your second Interactive app.")
st.write("Choose your fav Programming Language.")

lang=st.selectbox("Your fav Language: ", ["Java", "Python", "PHP", "JavaScript", "C++"])

st.write(f"Your Fav Language {lang}, Excellent Choice.")
st.success("You Choose Your Fav Language Successfully.")