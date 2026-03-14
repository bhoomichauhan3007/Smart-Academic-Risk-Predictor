import streamlit as st
import joblib

st.set_page_config(page_title="Risk Prediction", layout="wide")

st.title("📊 Academic Risk Analysis")

st.markdown("---")

# Check if student data exists
if "student_data" not in st.session_state:

    st.warning("⚠ Please fill the Academic Questions page first.")
    st.stop()

# Load model
model = joblib.load("Model/Model.pkl")

data = st.session_state.student_data

prediction = model.predict([data])[0]

st.subheader("🔍 Prediction Result")

col1, col2 = st.columns(2)

if prediction == 0:

    with col1:
        st.success("🟢 Student is in SAFE Zone")

    with col2:
        st.info("""
        The student currently shows **low academic risk**.

        ✔ Good attendance  
        ✔ Stable academic performance  
        ✔ Healthy study habits  
        """)

elif prediction == 1:

    with col1:
        st.warning("🟡 Student is in WARNING Zone")

    with col2:
        st.info("""
        The student may face **moderate academic difficulties**.

        Possible reasons:

        • Declining attendance trend  
        • Moderate exam anxiety  
        • Slight drop in academic performance
        """)

else:

    with col1:
        st.error("🔴 Student is in CRITICAL Risk Zone")

    with col2:
        st.info("""
        The student is **highly likely to face academic problems**.

        Possible reasons:

        • Very low attendance  
        • Poor internal marks  
        • High exam anxiety  
        • Sudden performance drop
        """)

st.markdown("---")

import matplotlib.pyplot as plt

st.subheader("📈 Academic Performance Visualization")

attendance = data[0]
internal_marks = data[1]
study_hours = data[4]

labels = ["Attendance", "Internal Marks", "Study Hours"]
values = [attendance, internal_marks, study_hours]

fig, ax = plt.subplots()
ax.bar(labels, values)

st.pyplot(fig)

import plotly.graph_objects as go

risk_value = prediction

fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = risk_value,
    title = {'text': "Academic Risk Level"},
    gauge = {
        'axis': {'range': [0,2]},
        'steps': [
            {'range': [0,0.5], 'color': "green"},
            {'range': [0.5,1.5], 'color': "yellow"},
            {'range': [1.5,2], 'color': "red"}
        ]
    }
))

st.plotly_chart(fig)

st.subheader("📈 Model Explanation")

st.write("""
This prediction is generated using a **Machine Learning Random Forest Model** trained on student academic performance data.

The model analyzes multiple academic and behavioral features such as attendance, internal marks, study hours and exam anxiety to estimate the student's academic risk level.
""")

st.markdown("---")

if st.button("➡ Next: Stress Detection"):

    st.switch_page("pages/4_Facial_Stress_Check.py")