import streamlit as st
import cv2
from deepface import DeepFace

st.title("🎥 Facial Stress Detection")

st.write("Click below to capture your face and detect stress level.")

if st.button("📷 Capture & Analyze"):

    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()

    if ret:
        st.image(frame, channels="BGR", caption="Captured Image")

        result = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)

        emotion = result[0]['dominant_emotion']
        scores = result[0]['emotion']

        st.subheader(f"🙂 Emotion: {emotion}")

        # Simple stress logic
        sad = float(scores.get("sad", 0))
        angry = float(scores.get("angry", 0))
        fear = float(scores.get("fear", 0))

        stress_score = sad + angry + fear

        if stress_score > 50:
            st.error("🔴 High Stress")
        elif stress_score > 25:
            st.warning("🟡 Moderate Stress")
        else:
            st.success("🟢 Low Stress")

    else:
        st.error("Camera not working")

    cap.release()

st.markdown("---")

if st.button("➡ Next: Recommendations"):
    st.switch_page("pages/5_Recommendations.py")