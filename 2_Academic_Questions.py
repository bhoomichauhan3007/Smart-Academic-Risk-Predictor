import streamlit as st

st.set_page_config(page_title="Academic Questions", layout="wide")

st.title("📚 Student Academic Information")

st.markdown("---")

st.subheader("Please enter the student's academic details")

col1, col2 = st.columns(2)

with col1:

    attendance = st.slider("📅 Attendance (%)",40,100)

    internal_marks = st.slider("📝 Internal Marks",30,100)

    previous_result = st.slider("📊 Previous Result",30,100)

    assignment_rate = st.slider("📂 Assignment Submission (%)",40,100)

with col2:

    study_hours = st.slider("📖 Study Hours per Day",1,8)

    sleep_hours = st.slider("😴 Sleep Hours",4,9)

    exam_anxiety = st.slider("😟 Exam Anxiety Level (1-5)",1,5)

    attendance_trend = st.selectbox("📉 Attendance Trend",[-1,0,1])

    marks_trend = st.selectbox("📈 Marks Trend",[-1,0,1])

    sudden_drop = st.selectbox("⚠ Sudden Performance Drop",[0,1])

st.markdown("---")

if st.button("🚀 Submit & Predict Risk"):

    st.session_state.student_data = [
        attendance,
        internal_marks,
        previous_result,
        assignment_rate,
        study_hours,
        sleep_hours,
        exam_anxiety,
        attendance_trend,
        marks_trend,
        sudden_drop
    ]

    st.switch_page("pages/3_Risk_Prediction.py")


