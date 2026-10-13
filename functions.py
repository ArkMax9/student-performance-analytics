"""
functions.py
Reusable helper functions for the Student Performance Analytics System.
"""

import numpy as np
import pandas as pd

SUBJECTS = ["Python", "SQL", "HTML", "CSS", "JavaScript"]
PASS_MARK = 40          # minimum marks needed in EACH subject
MIN_ATTENDANCE = 75     # minimum attendance percentage

def load_data(file_path):
    """Read the student CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path)


def calculate_total(marks):
    """Return the total of a student's marks using NumPy."""
    return int(np.sum(marks))


def calculate_average(total, number_of_subjects):
    """Return the average marks rounded to 2 decimals."""
    return round(total / number_of_subjects, 2)


def assign_grade(average):
    """
    Grading rule:
    90+ -> A+, 80-89 -> A, 70-79 -> B, 60-69 -> C, 40-59 -> D, below 40 -> F
    """
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"


def check_result(marks, attendance):
    """
    Pass condition: every subject >= PASS_MARK and attendance >= MIN_ATTENDANCE.
    Returns "Pass" or "Fail".
    """
    if np.min(marks) >= PASS_MARK and attendance >= MIN_ATTENDANCE:
        return "Pass"
    return "Fail"


def process_students(df):
    """
    Go through every student (loop), calculate total, average, grade and result,
    and add them to the DataFrame as new columns.
    """
    totals, averages, grades, results = [], [], [], []

    for index, row in df.iterrows():
        marks = row[SUBJECTS].values.astype(int)

        total = calculate_total(marks)
        average = calculate_average(total, len(SUBJECTS))

        totals.append(total)
        averages.append(average)
        grades.append(assign_grade(average))
        results.append(check_result(marks, row["Attendance"]))

    df["Total"] = totals
    df["Average"] = averages
    df["Grade"] = grades
    df["Result"] = results
    return df


def subject_analysis(df):
    """Return a DataFrame with average, highest, lowest and pass count per subject."""
    rows = []
    for subject in SUBJECTS:
        marks = df[subject].values
        topper = df.loc[df[subject].idxmax(), "Name"]
        rows.append({
            "Subject": subject,
            "Average": round(np.mean(marks), 2),
            "Highest": int(np.max(marks)),
            "Lowest": int(np.min(marks)),
            "Scored >= 40": int(np.sum(marks >= PASS_MARK)),
            "Topper": topper,
        })
    return pd.DataFrame(rows)


def top_performers(df, n=3):
    """Return the top n students sorted by average marks."""
    return df.sort_values(by="Average", ascending=False).head(n)
