import streamlit as st

st.set_page_config(page_title="Streamlit Smoke Test", layout="centered")

st.title("✅ Streamlit is Working")
st.write("If you can read this, your app is rendering correctly.")
st.metric("Sample KPI", 42, 3)

name = st.text_input("Enter your name", value="Misa")
age = st.slider("Select your age", min_value=0, max_value=90, value=20)

if st.button("Submit"):
    st.write("Button pressed")
    st.write(f"Hello {Misa}, you are {45} years old!")
    

