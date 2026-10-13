# Student Performance Analytics System

**Name:** Arnav Kumar Malkani
**Course:** Python with AI, EWB Courses

## 1. Objective
To build a python-based Student Performance Analytics System that reads student data, processes and analyzes it using NumPy 
and Pandas, and produces meaningful results such as marks summary, averages, grades, pass/fail statistics, subject-wise 
performance, and top performers. 

## 2. Technologies Used
- Python 3
- NumPy (sums, averages, min/max, comparisons)
- Pandas (loading the CSV, DataFrame operations, groupby, sorting)
- Git and GitHub for version control

## 3. Dataset
`students.csv` has **18 students** with these columns: Student_ID, Name,
Department (CSE / IT / ECE), marks in Python, SQL, HTML, CSS and JavaScript,
and Attendance (%). I made the data up, but kept the values realistic, with a
few weak students so the pass/fail logic actually gets tested.

## 4. How It Works
1. `load_data()` reads the CSV into a DataFrame, then `main.py` checks the shape,
   columns and missing values.
2. `process_students()` loops over every student. For each one it calls
   `calculate_total()` and `calculate_average()` (NumPy), `assign_grade()` and `check_result()`.
3. The new columns (Total, Average, Grade, Result) are added to the DataFrame.
4. `subject_analysis()` loops over the five subjects and finds the average,
   highest, lowest and topper of each.
5. `main.py` then prints the class average, pass percentage, grade distribution,
   department averages, top 3 students and the students who failed (with reasons).

**Grading rule:** 90+ = A+, 80-89 = A, 70-79 = B, 60-69 = C, 40-59 = D, below 40 = F

**Pass rule:** at least 40 in every subject AND at least 75% attendance.

## 5. Key Features
- Total and average marks per student
- Grades and pass/fail based on clearly defined rules
- Highest, lowest and class average
- Subject-wise analysis with subject toppers
- Department-wise averages
- Top performers list
- Reasons shown for each failed student
- Results saved to `student_results.csv`

## 6. Project Structure
```
student-performance-analytics/
├── main.py            # runs the project and prints the analysis
├── functions.py       # reusable calculation functions
├── students.csv       # input data
├── student_results.csv# generated output
├── sample_output.txt  # copy of the program output
├── screenshots/       # output screenshots
└── README.md
```

## 7. How to Run
```
pip install numpy pandas
python main.py
```

## 8. Output
![Student Data and Performance](screenshots/output1.png)
![Overall Analysis](screenshots/output2.png)
![Department-Wise Average](screenshots/output3.png)

## 9. Final Outcome
The program runs without errors and gives a full analysis of the 18 students:
14 passed, 4 failed, and the class average is 72.01. It also shows that Python
is the weakest subject and CSE has the highest department average.

## 10. Challenges and Learning
**Challenges I faced**
- **Understanding the loop over the DataFrame:** I wasn't sure how to go
  through each student row by row. I learned that `iterrows()` gives the
  row index and the row data, which let me calculate each student's total,
  grade and result.

**What I learned**
- How to load and organise data with Pandas, and how NumPy functions like
  `np.sum`, `np.mean` and `np.min` make calculations simpler.
- Why keeping reusable code in a separate `functions.py` makes `main.py`
  shorter and easier to read.

## 11. GitHub Repository
[PASTE YOUR REPO LINK HERE]
