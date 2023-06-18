import streamlit as st
import pandas as pd
import login
import business
import memory

st.set_page_config(
    page_title="Local File Reload",
    page_icon="🧊",
    layout="wide",
)

if 'passwd' not in st.session_state:
    st.session_state.passwd =  ''


if st.session_state.passwd == business.passwd:
    business.show()
elif st.session_state.passwd == memory.passwd:
    memory.show()
else:
    login.show()