# app.py

import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Streamlit UI
st.title("MCQ Generator")

# User input for topic
topic = st.text_input("Enter a topic for MCQs:")

# Google Gemini API Key
API_KEY = st.secrets["API_KEY"]  # Store your API key in Streamlit secrets

# Function to generate MCQs
def generate_mcqs(topic):
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=API_KEY)
    messages = [
        ("system", "You are a helpful content creator assistant that generates 10 MCQs on the given topic."),
        ("human", topic),
    ]
    return llm.invoke(messages)

# Generate and display MCQs if the topic is provided
if topic:
    mcqs = generate_mcqs(topic)
    st.write("### Generated MCQs:")
    st.write(mcqs)
