import streamlit as st
import time

def show():
    st.title('Please Login In')

    passwd = st.text_input('**Input Your PassWord**', type='password')

    if passwd == '':
        st.stop()

    if passwd != 'qyj' and passwd != 'qyjwyq':
        st.error('Passwd Error❗')
    else:
        st.session_state.passwd = passwd
        st.success('Login Succeess')
        time.sleep(1)
        st.experimental_rerun()
