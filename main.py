import streamlit as st
from askql import query_database

st.title("AskQL: Intelligent Database Queries with Generative AI")

question = st.text_input("Question: ")
url = st.text_input("Database URL: ", "sqlite:///./chinook.db")

if question and url:
    response = query_database(question, url)
    
    st.header("Answer")
    st.write(response)