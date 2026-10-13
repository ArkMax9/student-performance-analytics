"""
main.py
Student Performance Analytics System
Reads student data, processes it and prints the final analysis.
"""

import numpy as np
import pandas as pd
from functions import (load_data, process_students, subject_analysis,
                       top_performers, SUBJECTS, PASS_MARK, MIN_ATTENDANCE)

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", None)


def line(title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---- Load the data ----
df = load_data("students.csv")

line("STUDENT DATA (first 5 records)")
print(df.head().to_string(index=False))
print("\nTotal records :", len(df))
print("Columns       :", list(df.columns))
print("Missing values:", int(df.isnull().sum().sum()))

# ---- Process the data ----
df = process_students(df)

line("STUDENT PERFORMANCE")
print(df[["Student_ID", "Name", "Department", "Total", "Average",
          "Grade", "Result"]].to_string(index=False))

# ---- Overall analysis ----
line("OVERALL ANALYSIS")
best = df.loc[df["Average"].idxmax()]
worst = df.loc[df["Average"].idxmin()]
passed = int(np.sum(df["Result"] == "Pass"))
failed = len(df) - passed

print(f"Pass rule         : >= {PASS_MARK} in every subject and >= {MIN_ATTENDANCE}% attendance")
print(f"Class average     : {np.mean(df['Average']):.2f}")
print(f"Highest average   : {best['Name']} ({best['Average']})")
print(f"Lowest average    : {worst['Name']} ({worst['Average']})")
print(f"Students passed   : {passed}")
print(f"Students failed   : {failed}")
print(f"Pass percentage   : {passed / len(df) * 100:.1f}%")

# ---- Subject-wise analysis ----
line("SUBJECT-WISE ANALYSIS")
subject_table = subject_analysis(df)
print(subject_table.to_string(index=False))
best_subject = subject_table.loc[subject_table["Average"].idxmax(), "Subject"]
weak_subject = subject_table.loc[subject_table["Average"].idxmin(), "Subject"]
print(f"\nBest performing subject : {best_subject}")
print(f"Weakest subject         : {weak_subject}")

# ---- Grade distribution and department view ----
line("GRADE DISTRIBUTION")
print(df["Grade"].value_counts().sort_index().to_string())

line("DEPARTMENT-WISE AVERAGE")
print(df.groupby("Department")["Average"].mean().round(2).to_string())

# ---- Top performers ----
line("TOP 3 PERFORMERS")
rank = 1
for index, student in top_performers(df, 3).iterrows():
    print(f"{rank}. {student['Name']} - Average {student['Average']} - Grade {student['Grade']}")
    rank += 1

# ---- Students needing attention ----
line("STUDENTS WHO NEED SUPPORT")
for index, student in df[df["Result"] == "Fail"].iterrows():
    reasons = []
    low_subjects = [s for s in SUBJECTS if student[s] < PASS_MARK]
    if low_subjects:
        reasons.append("below pass mark in " + ", ".join(low_subjects))
    if student["Attendance"] < MIN_ATTENDANCE:
        reasons.append(f"attendance {student['Attendance']}%")
    print(f"- {student['Name']}: " + "; ".join(reasons))

# ---- Save the processed results ----
df.to_csv("student_results.csv", index=False)
print("\nProcessed results saved to student_results.csv")
