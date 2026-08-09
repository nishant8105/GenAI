import streamlit as st

st.title("Welcome To streamlit")
name = st.text_input("Enter Name")
st.write(name)
btn = st.button("Greet Me")

if btn :
    st.write("Hello, !")
