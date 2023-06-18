
import streamlit as st

passwd = 'qyjwyq'

@st.cache_data
def get_video(video):
    with open(video, 'rb') as fp:
        return fp.read()

def show():
    st.title('QYJ&WYQ の Memory')
    st.video(get_video(r'res/first_video.mp4'))
