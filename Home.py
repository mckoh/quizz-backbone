import streamlit as st
from util import add_session_state_key

# Check if session variable has been already added
# If not, add it to session state
add_session_state_key()

# Set page configuration
st.set_page_config(
    page_icon="🖖",
    page_title="MCIT Sakai Quiz Backbone"
)

st.title("🖖 MCIT Sakai Quiz Backbone")
st.markdown("This is a test with new code.")
st.write(st.session_state)
