import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib

# Load dataset (Excel file)

data = pd.read_csv("Dataset/student_dataset.csv", sep=",")

# agar poora row ek hi column me read ho raha hai to usko split kar do
if len(data.columns) == 1:
    data = data[data.columns[0]].str.split(",", expand=True)

# column names set kar do
data.columns = [
"student_id","name","attendance","internal_marks","previous_result",
"assignment_rate","study_hours","sleep_hours","exam_anxiety",
"attendance_trend","marks_trend","sudden_performance_drop","risk"
]

# Convert risk labels into numbers
risk_map = {
    "Safe": 0,
    "Warning": 1,
    "Critical": 2
}

data["risk"] = data["risk"].map(risk_map)

# Select features
X = data[[
    "attendance",
    "internal_marks",
    "previous_result",
    "assignment_rate",
    "study_hours",
    "sleep_hours",
    "exam_anxiety",
    "attendance_trend",
    "marks_trend",
    "sudden_performance_drop"
]]

# Target column
y = data["risk"]

# Split dataset into training and testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create model
model = RandomForestClassifier()

# Train model
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Check accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Model Accuracy:", accuracy)

# Save trained model
joblib.dump(model, "Model/Model.pkl")

print("Model Saved Successfully")