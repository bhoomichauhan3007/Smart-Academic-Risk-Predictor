import streamlit as st
import pandas as pd

st.title("🎓 Smart Academic Risk Predictor")
st.subheader("🔐 Student Login")

data = pd.read_csv("Dataset/student_dataset.csv")

# Clean column names
data.columns = data.columns.str.strip().str.lower()

student_id = st.text_input("Enter Student ID")
name = st.text_input("Enter Student Name")

if st.button("Login"):

    if student_id == "" or name == "":
        st.warning("Please enter both fields")

    else:

        student = data[
            (data["student_id"].astype(str) == student_id) &
            (data["name"].str.lower() == name.lower())
        ]

        if not student.empty:

            st.session_state.student_logged = True

            st.success("Login Successful")

            st.switch_page("pages/1_Welcome_Dashboard.py")

        else:
            st.error("Invalid Student ID or Name")