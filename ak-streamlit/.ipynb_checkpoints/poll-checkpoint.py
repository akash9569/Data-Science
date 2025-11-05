import streamlit as st

st.markdown("# Programming Language Poll")

col1, col2, col3 = st.columns(3)

with col1:
    st.header("Python")
    st.image("https://images.pexels.com/photos/11035474/pexels-photo-11035474.jpeg?auto=compress&cs=tinysrgb&w=1200", width=200)
    vote1 = st.button("Vote for Python")

with col2:
    st.header("Java")
    st.image("https://images.pexels.com/photos/11035360/pexels-photo-11035360.jpeg?auto=compress&cs=tinysrgb&w=1200", width=200)
    vote2 = st.button("Vote for Java")

with col3: 
    st.header("PHP")
    st.image("https://images.pexels.com/photos/11035390/pexels-photo-11035390.jpeg?auto=compress&cs=tinysrgb&w=1200", width=200)
    vote3 = st.button("Vote for PHP")


if vote1:
    st.success("Thanks for voting Python.")
elif vote2:
    st.success("Thanks for voting Java.")
elif vote3:
    st.success("Thanks for voting PHP.")


name = st.sidebar.text_input("Enter your Name")
lang = st.sidebar.selectbox("Choose your Programming Langguage",["Python", "Java", "PHP"])

st.write(f"Hello {name}, Your Favourite Programming Language is {lang}.")

with st.expander("Show Roadmap of Learning Any Programming Language"):
    st.write("""
    1. Understand Basic of any Programming Language
    2. Learn Variables, Datatypes, Conditional Statement, Loops
    3. Learn OOPs Concept
    4. Move Advance Level of any Language
    """)

