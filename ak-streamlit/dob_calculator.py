import streamlit as st
from datetime import datetime, date
import calendar

st.title("DOB Age Calculator")

dob = st.date_input("Select your Date of Birth", min_value=date(1900, 1, 1), max_value=date.today())

def calculate_age(birth_date):
    today = date.today()
    years = today.year - birth_date.year
    months = today.month - birth_date.month
    days = today.day - birth_date.day

    if days < 0:
        months -= 1
        prev_month = (today.month - 1) if today.month > 1 else 12
        days += calendar.monthrange(today.year if prev_month != 12 else today.year - 1, prev_month)[1]
    
    if months < 0:
        years -= 1
        months += 12

    return years, months, days

if dob:
    years, months, days = calculate_age(dob)
    st.success(f"🎉 You are {years} years, {months} months, and {days} days old!")

    st.info(f"Your birthdate: {dob.strftime('%A, %B %d, %Y')}")
    st.info(f"Today's date: {date.today().strftime('%A, %B %d, %Y')}")
