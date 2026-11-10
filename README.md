# 🎓 Smart Academic Risk Predictor

### AI-Powered Academic Risk Analysis & Facial Stress Detection

## 📌 About the Project

Smart Academic Risk Predictor is an AI-powered web application designed to identify students who may be at academic risk by analyzing their academic performance, study habits, and facial emotions.

It combines Machine Learning-based risk prediction with webcam-based facial emotion detection to provide personalized recommendations and support better academic outcomes.

## ✨ Key Features

- **Student Login:** Login using Student ID with dataset verification.
- **Academic Analysis:** Analyzes attendance, marks, assignments, study hours, sleep patterns, and exam anxiety.
- **Risk Prediction:** Uses Machine Learning to classify students into Safe, Warning, and Critical categories.
- **Facial Emotion Detection:** Uses a webcam, OpenCV, and DeepFace to recognize facial emotions and estimate stress levels.
- **Personalized Recommendations:** Provides suggestions based on academic risk and emotional analysis.
- **Final Dashboard:** Displays student analysis and recommendations.

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas & NumPy
- Scikit-learn
- OpenCV
- DeepFace
- TensorFlow / tf-keras
- Pickle

## 📁 Project Structure

```text
Smart-Academic-Risk-Predictor/
│
├── Assets/
├── Dataset/
├── Model/
├── Pages/
├── Recommendation/
├── Stress_detection/
├── Utils/
├── App.py
├── Requirements.txt
└── README.md
```

## 🔄 Project Workflow

```text
Student Login
     ↓
Academic Data Analysis
     ↓
ML-Based Risk Prediction
     ↓
Webcam-Based Emotion Detection
     ↓
Stress Estimation
     ↓
Personalized Recommendations
     ↓
Final Result
```

## ⚙️ Installation & Execution

**1. Clone the repository**

```bash
git clone https://github.com/bhoomichauhan3007/Smart-Academic-Risk-Predictor.git
```

**2. Install dependencies**

```bash
pip install -r Requirements.txt
```

**3. Generate the dataset (if required)**

```bash
python Dataset/dataset.py
```

**4. Train the model (if required)**

```bash
python Model/Train_model.py
```

**5. Run the application**

```bash
streamlit run App.py
```

## 📊 Dataset

The project uses a dataset of **500 simulated student records** containing academic and behavioral attributes such as attendance, internal marks, study hours, sleep hours, assignment completion, and risk categories.

## 🔮 Future Scope

- Real-time emotion monitoring.
- Improved stress estimation models.
- Teacher and administrator dashboards.
- Integration with institutional databases.
- Cloud deployment and advanced analytics.

## 🔒 Privacy & Ethics

Student data and webcam access should be handled with user consent and appropriate privacy safeguards. Facial emotion detection provides an estimate, not a medical diagnosis.

## 👩‍💻 Project Information

**Developer:** Bhoomi Chauhan  
**University:** Bennett University  
**Domain:** Artificial Intelligence & Machine Learning

---

⭐ **Early Identification | Smarter Insights | Better Academic Support**
