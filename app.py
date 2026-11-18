import streamlit as st
from groq import Groq
import streamlit as st
st.set_page_config(page_title = "About Me", page_icon = '🫡', layout= 'centered')
st.title("Hanamantraya ")
st.caption("UNIVERSAL BOSS ")
try:
  client = Groq(api_key = st.secrets["GROQ_API_KEY"])
except (KeyError, FileNoteFound):
  st.error("API Key is missing. Add it in Advance setting")
  st.stop()
