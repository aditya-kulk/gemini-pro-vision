import os
from dotenv import load_dotenv

load_dotenv()   #loading all env variables
import streamlit as st
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(question):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content(question)
    return response.text


st.set_page_config(page_title="Q&A demo")
st.header("Gemini Application")
input=st.text_input("Input: ", key=input)
submit=st.button("Ask question")

if submit:
    response=get_gemini_response(input)
    st.subheader("The response is")
    st.write(response)