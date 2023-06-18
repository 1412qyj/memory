import streamlit as st

passwd = 'qyj'

def show():
    st.title('Local File Reload')

    if 'file_block' not in st.session_state:
        st.session_state.file_block = ['Path1', 'Path2', 'Path3']

