import streamlit as st

st.set_page_config(page_title="Recommendations", layout="wide")

st.title("📋 Personalized Recommendations")

st.markdown("Based on the academic risk analysis and stress level, the following suggestions can help improve student performance.")

st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📚 Academic Improvement")

    st.markdown("""
    • Maintain **attendance above 75%** to stay consistent with lectures.  
    • Study **3–4 focused hours daily** instead of last-minute preparation.  
    • Revise **class notes regularly** to strengthen understanding.  
    • Complete **assignments before deadlines** to avoid backlog.  
    • Solve **previous year question papers** for exam preparation.  
    """)

with col2:
    st.subheader("🧠 Stress Management")

    st.markdown("""
    • Maintain a **balanced sleep schedule (6–8 hours)**.  
    • Take **short breaks during study sessions** to avoid burnout.  
    • Practice **deep breathing or meditation** for stress reduction.  
    • Avoid excessive screen time before sleeping.  
    • Maintain a **healthy daily routine** with exercise.
    """)

st.markdown("---")

col3, col4 = st.columns(2)

with col3:
    st.subheader("⏰ Time Management Tips")

    st.markdown("""
    • Create a **daily study timetable**.  
    • Break large topics into **smaller manageable tasks**.  
    • Use **Pomodoro technique (25 min focus + 5 min break)**.  
    • Track progress using a **study checklist**.
    """)

with col4:
    st.subheader("🤝 Support & Guidance")

    st.markdown("""
    • Discuss difficult topics with **teachers or mentors**.  
    • Form **small study groups** for collaborative learning.  
    • Seek **academic counseling** if performance declines.  
    • Stay motivated by setting **small achievable goals**.
    """)

st.markdown("---")

st.success("Following these strategies can significantly improve academic performance and reduce stress.")

if st.button("➡ View Final Result"):
    st.switch_page("pages/6_Final_Result.py")