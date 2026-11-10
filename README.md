# 🎓 Smart Academic Risk Predictor

### AI-Powered Student Performance Analysis & Facial Stress Detection

An intelligent, AI-based academic monitoring system designed to identify students who may be at academic risk by analyzing their academic performance, study habits, and facial emotions.

The system combines **Machine Learning-based academic risk prediction** with **Deep Learning-based facial emotion detection** to provide a broader understanding of student performance and personalized recommendations.

---

## 📌 Project Overview

Academic performance is influenced by several factors, including attendance, internal marks, assignment completion, study hours, sleep patterns, and exam anxiety.

Traditional academic monitoring systems mainly focus on marks and attendance, which may not reveal the complete picture of a student's condition.

To address this, we developed the Smart Academic Risk Predictor. It analyzes student academic information, predicts potential academic risk, detects facial emotions through a webcam, and provides personalized recommendations to help students improve their academic performance.

## 🎯 Project Objectives

- Identify students who may be academically at risk at an early stage.
- Analyze multiple academic and behavioral parameters.
- Predict academic risk using Machine Learning.
- Detect facial emotions using webcam-based AI.
- Estimate possible stress levels from detected emotions.
- Generate personalized academic and well-being recommendations.
- Provide an interactive and user-friendly dashboard.

## ✨ Key Features

### 1. 🔐 Student Login System
- Student authentication using Student ID.
- Verifies student records against the dataset.
- Automatically retrieves the corresponding student information.
- Prevents access using an unrecognized Student ID.

### 2. 📊 Academic Information Analysis
The system analyzes multiple student-related parameters:

- Attendance percentage
- Internal examination marks
- Previous academic results
- Assignment completion rate
- Daily study hours
- Sleep hours
- Exam anxiety level
- Attendance trends
- Marks trends
- Sudden performance drops

Student information is automatically retrieved from the dataset after login.

### 3. 🤖 AI-Based Academic Risk Prediction

A trained Machine Learning model analyzes academic and behavioral features to classify students into three risk categories:

- 🟢 **Safe:** Student is maintaining satisfactory academic performance.
- 🟡 **Warning:** Student may need academic attention and improvement.
- 🔴 **Critical:** Student may require additional academic support and intervention.

The trained model is saved as `Model.pkl` and reused for predictions without retraining every time.

### 4. 🎥 Facial Emotion & Stress Analysis

The system uses a webcam to capture the student's facial image.

Using OpenCV and DeepFace, the captured image is analyzed to identify facial emotions.

The detected emotion is mapped to an estimated stress category using predefined application logic.

The analysis helps provide additional context alongside academic performance.

**Note:** Facial emotion detection is not a medical or psychological diagnosis. Facial expressions alone cannot reliably establish a person's actual stress level.

### 5. 💡 Personalized Recommendations

The recommendation module provides suggestions based on the student's academic risk and detected emotional state.

Examples include:

- Improving attendance and class participation.
- Following a consistent study timetable.
- Practicing time management.
- Maintaining healthy sleep habits.
- Taking regular breaks.
- Using relaxation techniques.
- Seeking academic guidance when required.

### 6. 📋 Final Result Dashboard

The final page presents the student's overall analysis, including academic risk, facial emotion analysis, and personalized recommendations in an organized format.

---

## 🛠️ Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Interactive web application |
| Pandas | Dataset handling and preprocessing |
| NumPy | Numerical operations |
| Scikit-learn | Machine Learning model development |
| OpenCV | Webcam access and image processing |
| DeepFace | Facial emotion recognition |
| TensorFlow / tf-keras | Deep learning framework |
| Pickle | Saving and loading the trained model |
| Matplotlib | Data visualization |

---

## 🧠 Machine Learning Implementation

The academic risk prediction component uses a supervised Machine Learning approach.

**Input:** Academic and behavioral information of students.

**Output:** Predicted academic risk category.

The model is trained using a labeled student dataset and saved as a serialized model file (`Model.pkl`).

The training workflow includes:

1. Loading the student dataset.
2. Data preprocessing and feature selection.
3. Splitting data into training and testing sets.
4. Training the classification model.
5. Evaluating model performance.
6. Saving the trained model for future predictions.

The model's performance is evaluated using classification metrics such as accuracy, precision, recall, and F1-score.

---

## 📁 Project Structure

```text
Smart-Academic-Risk-Predictor/
│
├── Assets/
│   ├── background.png
│   └── logo.png
│
├── Dataset/
│   ├── dataset.py
│   └── student_dataset.csv
│
├── Model/
│   ├── Model.pkl
│   ├── Train_model.py
│   └── Predict_model.py
│
├── Pages/
│   ├── 0_Login.py
│   ├── 1_Welcome_Dashboard.py
│   ├── 2_Academic_Questions.py
│   ├── 3_Risk_Prediction.py
│   ├── 4_Facial_Stress_Check.py
│   ├── 5_Recommendations.py
│   └── 6_Final_Result.py
│
├── Recommendation/
│   └── Recommendation_engine.py
│
├── Stress_detection/
│   ├── emotion_detector.py
│   └── stress_logic.py
│
├── Utils/
│   ├── data_loader.py
│   └── helpers.py
│
├── App.py
├── README.md
└── Requirements.txt
```

---

## ⚙️ Installation & Setup

Follow these steps to run the project locally.

### Step 1: Clone the Repository

```bash
git clone https://github.com//bhoomichauhan3007/Smart-Academic-Risk-Predictor.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Smart-Academic-Risk-Predictor
```

### Step 3: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
pip install -r Requirements.txt
```

If DeepFace dependencies are not included in the requirements file:

```bash
pip install opencv-python deepface tf-keras
```

### Step 5: Generate or Prepare the Dataset

If using the included dataset generator:

```bash
python Dataset/dataset.py
```

Ensure that `student_dataset.csv` is available inside the Dataset folder.

### Step 6: Train the Machine Learning Model

```bash
python Model/Train_model.py
```

Ensure the trained model is saved at:

```text
Model/Model.pkl
```

### Step 7: Run the Application

```bash
streamlit run App.py
```

The application will open in your default browser.

---

## 🔄 Application Workflow

```text
       Student Login
             |
             ▼
    Student Data Retrieval
             |
             ▼
   Academic Information Analysis
             |
             ▼
      Academic Risk Prediction
             |
             ▼
    Webcam-Based Face Capture
             |
             ▼
     Facial Emotion Detection
             |
             ▼
       Stress Estimation
             |
             ▼
   Personalized Recommendations
             |
             ▼
        Final Result
```

---

## 📊 Dataset Information

The project uses a dataset containing 500 student records.

Each record includes academic and behavioral attributes required for risk prediction.

The dataset includes the following features:

- Student ID
- Student Name
- Attendance
- Internal Marks
- Previous Result
- Assignment Rate
- Study Hours
- Sleep Hours
- Exam Anxiety
- Attendance Trend
- Marks Trend
- Sudden Performance Drop
- Risk Category

**Dataset Note:** The generated dataset contains simulated student records for development and demonstration. It should not be treated as actual institutional student data.

---

## 🔒 Privacy & Ethical Considerations

- Student records should only be accessible to authorized users.
- Webcam access should require explicit user permission.
- Facial images should not be stored or shared without informed consent.
- Emotion detection should be treated as an approximate indicator, not a mental health diagnosis.
- Academic risk predictions should support human decision-making rather than automatically determine a student's academic status.
- Real-world deployment requires appropriate data protection and institutional approval.

---

## 🚀 Future Enhancements

Some planned improvements include:

- Real-time facial emotion monitoring.
- Improved stress estimation using more comprehensive models.
- Integration with institutional student databases.
- Teacher and administrator dashboards.
- Advanced performance analytics and visual reports.
- Cloud deployment and secure authentication.
- Larger and more diverse real-world datasets.
- Improved model explainability and fairness evaluation.

---

## 🎯 Expected Impact

The Smart Academic Risk Predictor aims to support educational institutions in identifying students who may need additional attention.

By combining academic analysis with facial emotion recognition, the project explores a more comprehensive approach to student monitoring.

It encourages early intervention, personalized academic support, and better awareness of student well-being.

---

## 👩‍💻 Project Information

**Project Name:** Smart Academic Risk Predictor

**Domain:** Artificial Intelligence & Machine Learning

**Core Technologies:** Python, Machine Learning, Deep Learning, OpenCV, DeepFace, Streamlit

**Developed By:** Bhoomi Chauhan

**University:** Bennett University

---

## ⭐ Conclusion

The Smart Academic Risk Predictor is an AI-powered approach to understanding student performance beyond traditional academic evaluation.

By integrating Machine Learning, facial emotion recognition, and personalized recommendations, the system aims to make academic monitoring more intelligent, supportive, and student-centered.

**Early Identification. Smarter Insights. Better Academic Support.** 🎓
