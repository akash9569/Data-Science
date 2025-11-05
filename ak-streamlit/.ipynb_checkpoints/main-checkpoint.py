import streamlit as st
st.title("Akash")
st.subheader("Brewed with streamlit")
st.text("Welcome to your first interactive app")
st.write("choose your fav. variety of chai")

chai=st.selectbox("Your fav chai: ",["Masala Chai", "Lemon Tea", "Adrak Chai", "Kesar Chai"])

st.write(f"You choose {chai}. Excellent Choice.")
st.success("Your Chai has been Brewed.")