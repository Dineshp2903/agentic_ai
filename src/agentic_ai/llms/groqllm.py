import os
import streamlit as st
from langchain_groq import ChatGroq

class GroqChat:
    def __init__(self,user_controls_input):
        self.user_controls = user_controls_input
        

    def get_llm_model(self):
        """
        Get the LLM model
        """
        try:
            groq_api_key = self.user_controls["GROQ_API_KEY"]
            groq_model = self.user_controls["selected_groq_model"]
            if groq_api_key == "" and os.environ["GROQ_API_KEY"] =="":
                st.error("Please enter the GROQ API Key")

            llm = ChatGroq(groq_api_key,groq_model)
            return llm
        except Exception as e:
            raise ValueError("Error in getting the LLM model")
        return llm