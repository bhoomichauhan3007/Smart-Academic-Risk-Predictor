import pandas as pd
import random

names = [
"Nihal","Aachal","Netra","Manthan","Nidra","Yoshita","Krishna","Qushi","Riya","Arjun",
"Rahul","Aman","Sneha","Priya","Karan","Ananya","Rohit","Aditi","Kabir","Simran",
"Meera","Varun","Tanya","Ishaan","Pooja","Ritika","Dev","Sanya","Harsh","Isha"
]

rows = []

for i in range(1,501):

    name = random.choice(names)

    attendance = random.randint(40,100)
    internal_marks = random.randint(20,100)
    previous_result = random.randint(30,100)
    assignment_rate = random.randint(40,100)
    study_hours = random.randint(1,8)
    sleep_hours = random.randint(4,9)
    exam_anxiety = random.randint(1,10)
    attendance_trend = random.randint(0,1)
    marks_trend = random.randint(0,1)
    sudden_drop = random.randint(0,1)

    if attendance > 75 and internal_marks > 60:
        risk = "Safe"
    elif attendance > 55:
        risk = "Warning"
    else:
        risk = "Critical"

    rows.append([
        i,name,attendance,internal_marks,previous_result,
        assignment_rate,study_hours,sleep_hours,exam_anxiety,
        attendance_trend,marks_trend,sudden_drop,risk
    ])

columns = [
"student_id","name","attendance","internal_marks","previous_result",
"assignment_rate","study_hours","sleep_hours","exam_anxiety",
"attendance_trend","marks_trend","sudden_performance_drop","risk"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv("Dataset/student_dataset.csv", index=False)

print("✔ student dataset created")


