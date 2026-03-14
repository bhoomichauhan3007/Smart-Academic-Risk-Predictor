import streamlit as st

st.set_page_config(page_title="Smart Academic Risk Predictor",layout="wide")

st.title("🎓 Smart Academic Risk Predictor")

st.markdown("---")

st.subheader("📊 About the System")

st.write("""
The **Smart Academic Risk Predictor** is an intelligent system designed to identify students who may be at academic risk.

The system analyzes several academic and behavioral factors to determine whether a student is likely to face academic difficulties.
""")

st.markdown("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📅 **Attendance Analysis**\n\nLow attendance can indicate academic risk.")

with col2:
    st.info("📝 **Academic Performance**\n\nInternal marks and previous results help measure student performance.")

with col3:
    st.info("🧠 **Behavioral Factors**\n\nStudy hours, sleep patterns and exam anxiety are also considered.")

st.markdown("---")

st.subheader("⚙️ System Workflow")

st.write("""
1️⃣ Enter student academic details  
2️⃣ Machine Learning model predicts risk level  
3️⃣ Facial emotion detection checks stress level  
4️⃣ System suggests recommendations to improve performance
""")

st.success("⬅️ Use the menu on the left to start the academic assessment.")


if st.button("➡ View next page Result"):
    st.switch_page("pages/2_Academic_Questions.py")