import streamlit as st

st.title("🎓 Final Academic Assessment")

st.success("The academic risk analysis has been completed successfully.")

st.write("""
Thank you for using the **Smart Academic Risk Predictor System**.

This system helps identify students who may face academic difficulties and provides recommendations to improve their performance.
""")

from fpdf import FPDF

if st.button("Download Risk Report"):

    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", size=14)

    pdf.cell(200,10,txt="Smart Academic Risk Predictor Report",ln=True)

    pdf.cell(200,10,txt=f"Risk Level: {prediction}",ln=True)

    pdf.cell(200,10,txt="Recommendation: Improve study habits and maintain attendance.",ln=True)

    pdf.output("risk_report.pdf")

    with open("risk_report.pdf","rb") as file:
        st.download_button("Download PDF",file,"risk_report.pdf")
        
st.balloons()