
import streamlit as st

passwd = 'qyjwyq'

url = r'memory.mp4'

@st.cache_data
def read_video():
    with open(url, 'rb') as fp:
        return fp.read()

def show():
    st.title('QYJ&WYQ1 の Memory')
    st.video(read_video())
