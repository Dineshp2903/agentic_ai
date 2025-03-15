import streamlit as st
import os
import datetime as date

from langchain_core.messages import AIMessage,HumanMessage
from src.agentic_ai.doc_loader import PDFLoader

from src.agentic_ai.ui.uiconfigfile import Config
from src.agentic_ai.constants import RAG_CHATBOT

class LoadStreamlitUI:

    def __init__(self):
        self.config = Config()
        self.user_controls = {}


    def initialize_session(self):
        """
        Initialize the session
        """
        return {
            "current_step" : "requirements",
            "requirements":"",
            "user_stories":"",
            "po_feedback":"",
            "generated_code":"",
            "review_feedback":"",
            "decision":None

        }
    
    def load_streamlit_ui(self):
        """
        Load the Streamlit UI
        """
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.title("🤖 " + self.config.get_page_title())
        st.session_state.timeframe=""
        st.session_state.IsFetchButtonClicked = False
        st.session_state.IsSDLC = False


        with st.sidebar:
            ### LLM Option
            llm_options = self.config.get_llm_options()
            use_case_options = self.config.get_use_case_options()


            self.user_controls["selected_llm"] = st.selectbox("Select LLM",llm_options)

            if self.user_controls["selected_llm"] == "GROQ":
                
                model_options = self.config.get_groq_options()

                self.user_controls["selected_groq_model"] = st.selectbox("Select Model",model_options)


                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]= st.text_input("Enter GROQ API Key",type="password")

                # if not self.user_controls["GROQ_API_KEY"]:
                #     st.warning("⚠️ Please enter   your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys")

                self.user_controls["selected_usecase"] = st.selectbox("Select Usecases", use_case_options)
                print(self.user_controls["selected_usecase"])

                if self.user_controls["selected_usecase"] =="ChatBot With Tool":
                    # API key input
                    os.environ["TAVILY_API_KEY"] = self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("TAVILY API KEY",
                                                                                                      type="password")
                    # Validate API key
                    if not self.user_controls["TAVILY_API_KEY"]:
                        st.warning("⚠️ Please enter your TAVILY_API_KEY key to proceed. Don't have? refer : https://app.tavily.com/home")

                if self.user_controls["selected_usecase"] == RAG_CHATBOT:
                    print("RAG Chatbot")
                    
                    uploaded_file = st.file_uploader("Choose a file", type=["csv", "txt", "pdf"])

                    with open("temp.pdf", "wb") as f:
                        f.write(uploaded_file.read())
                    st.write("File Uploaded")
                    PDFLoader().load("temp.pdf")
            
            
                    
            if "state" not in st.session_state:
                st.session_state.state = self.initialize_session()
        return self.user_controls



