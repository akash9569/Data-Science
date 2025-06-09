import streamlit as st
st.title("Chai Maker")

add = st.checkbox("Add Masala")

if add:
    st.write("Masala added to your Chai")

tea_type = st.radio("Pick your chai base: ", ["Milk", "Water", "Honey"])
st.write(f"selected base {tea_type}")

flavour = st.selectbox("Choose flavour: ", ["Adrak", "Kesar", "Tulsi"])
st.write(f"selected base {flavour}")

sugar = st.slider("Sugar Spoon",0,5,4)
st.write(f"Selected Sugar Spoon {sugar}")

cup = st.number_input("How many Cups", min_value=1, max_value=10, step=1)
st.write(f"Selected {cup} Cups of Tea")

name = st.text_input("Enter Your Name")
if name:
    st.write(f"Wrlcome, {name} ! Your chai is on the way.")

dob = st.date_input("Select your Date of Birth")
st.write(f"Wrlcome, {dob} ! Your chai is on the way.")



if st.button("Make Chai"):
    st.success("Your Chai is being brewed")