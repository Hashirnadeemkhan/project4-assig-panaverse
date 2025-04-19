import streamlit as st
import pandas as pd

st.set_page_config(page_title="Streamlit Website", layout="centered")

# Title
st.title("My Streamlit Web App 🚀")
st.write("Welcome to my awesome web app built with Python and Streamlit!")

# Sidebar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Upload CSV", "About"])

# Home Page
if page == "Home":
    st.header("📍 Home Page")
    st.write("This is the home page of the application.")
    name = st.text_input("Enter your name:")
    if name:
        st.success(f"Hello, {name}! Welcome to my app.")

# Upload CSV Page
elif page == "Upload CSV":
    st.header("📁 Upload Your CSV File")
    file = st.file_uploader("Choose a CSV file", type=["csv"])
    if file is not None:
        df = pd.read_csv(file)
        st.write("### 📊 Data Preview")
        st.dataframe(df)
        st.write("### 📈 Basic Statistics")
        st.write(df.describe())

# About Page
elif page == "About":
    st.header("👨‍💻 About")
    st.write("This web app is built using [Streamlit](https://streamlit.io/).")
    st.write("Created by: Your Name Here")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by [Hashir](https://github.com/Hashirnadeemkhan)")
