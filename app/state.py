# --- state.py ---
import streamlit as st
from app.controller import AgentController
from app.config import AgentConfig

def init_session():
    if "agent" not in st.session_state:
        st.session_state.agent = AgentController(user_language=AgentConfig.DEFAULT_LANGUAGE)
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

def reset_session():
    st.session_state.agent.reset_conversation()
    st.session_state.chat_history = []