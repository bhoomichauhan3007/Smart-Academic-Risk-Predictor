import streamlit as st

if "student_logged" not in st.session_state:
    st.switch_page("pages/0_Login.py")