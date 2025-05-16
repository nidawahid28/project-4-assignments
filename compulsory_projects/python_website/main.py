import streamlit as st

st.set_page_config(page_title="My First Website", page_icon="🌐", layout="centered")
st.title("Welcome to My First Python Website")

st.sidebar.title("Navigation")
page=st.sidebar.radio("Go to", ["Home", "About", "Contact"])

if page == "Home":
    st.header("Home")
    st.write("This is the home page of my first website.")
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Hello {name}! Thank you for visiting my website.")
elif page == "About":
    st.header("About")
    st.write("This website is built using Streamlit, a Python library for creating web applications.")
elif page == "Contact":
    st.header("Contact Us")
    email = st.text_input("Enter your email:")
    message = st.text_area("Enter your message:")
    if st.button("Send"):
        if email and message:
            st.success("Your message has been sent!")
        else:
            st.error("Please fill in all fields.")
        
    
