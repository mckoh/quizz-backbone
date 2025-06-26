import streamlit as st


def add_session_state_key():
    if "quizzes" not in st.session_state:
        st.session_state["quizzes"] = []
    return True
