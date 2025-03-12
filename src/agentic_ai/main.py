import streamlit as st
import json
from src.agentic_ai.ui.streamlitui.loadui import LoadStreamlitUI
from src.agentic_ai.ui.streamlitui.display_result import DisplayResultStreamlit
from src.agentic_ai.llms.groqllm import GroqChat
from src.agentic_ai.graph.graph_builder import GraphBuilder



# main Function Start


def load_agenticai_app():
    """
    Load the Agentic AI App
    """

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe

    else:
        user_message = st.chat_input("Enter Your Message")

    if user_message:
        try:
            obj_llm_config = GroqChat(user_controls_input=user_input)
            model = obj_llm_config.get_llm_model()

            if not model:
                st.error("Error in getting the LLM model")
                return
            
            use_case = user_input.get("selected_usecase")
            if not use_case:
                st.error("Error in getting the use case")
                return



