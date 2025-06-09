import streamlit as st
import requests

st.markdown("Currency Converter")
amount = st.number_input("Enter the Amount in INR", min_value = 1)
currency = st.selectbox("Convert to: ",["USD", "EUR", "GBP"])
if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        rate = data["rates"][currency]
        converted = rate * amount
        st.success(f"{amount} INR = {converted:.2f}{currency}")
    else:
        st.error("Failed to fetch conversion rate.")