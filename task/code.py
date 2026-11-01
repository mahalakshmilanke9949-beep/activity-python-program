# University Scholarship Allocation System Using Python

## 1\. Problem Statement

Design and develop a Python program to allocate university scholarships to students based on their academic performance, attendance, and family income.

The system evaluates students using the following criteria:

1. **Aggregate Marks:** Students must score a minimum of 75% aggregate marks.
2. **Subject-wise Minimum Marks:** Students must score at least 50 marks in each subject.
3. **Attendance:** Students must have a minimum of 75% attendance.
4. **Family Income:** Annual family income must not exceed ₹2,50,000.

The system identifies eligible students, ranks them based on their academic performance, and allocates scholarships according to their rank.

**Tie-breaking rules:**

- First priority: Higher aggregate marks.
- Second priority: Higher attendance percentage.
- Third priority: Lower family income.
- Fourth priority: Lower registration number.

---

## 2\. Algorithm

**Step 1:** Start the program.

**Step 2:** Get the number of students.

**Step 3:** For each student, input:

- Student name
- Registration number
- Subject marks
- Attendance percentage
- Annual family income

**Step 4:** Calculate the aggregate percentage of each student.

**Step 5:** Check eligibility conditions:

- Aggregate marks ≥ 75%.
- Each subject mark ≥ 50.
- Attendance ≥ 75%.
- Annual family income ≤ ₹2,50,000.

**Step 6:** If all conditions are satisfied, declare the student eligible.

**Step 7:** Store all eligible students.

**Step 8:** Sort eligible students based on:

1. Higher aggregate percentage.
2. Higher attendance.
3. Lower family income.
4. Lower registration number.

**Step 9:** Display the ranked list of eligible students.

**Step 10:** Allocate scholarships according to their ranks.

**Step 11:** Stop the program.

---

## 3\. Flowchart (Mermaid Code)

Copy the following code into the Mermaid Live Editor to generate the flowchart.

[Mermaid Live Editor](<https://mermaid.live/?utm_source=chatgpt.com>)
```
mermaid
flowchart TD
    A([Start]) --> B[/Enter Number of Students/]
    B --> C[/Enter Student Details/]
    C --> D[Calculate Aggregate Marks]
    D --> E{Aggregate >= 75%?}
    E -- No --> K[Declare Not Eligible]
    E -- Yes --> F{All Subject Marks >= 50?}
    F -- No --> K
    F -- Yes --> G{Attendance >= 75%?}
    G -- No --> K
    G -- Yes --> H{Income <= 250000?}
    H -- No --> K
    H -- Yes --> I[Declare Eligible]
    I --> J[Store Eligible Students]
    K --> L{More Students?}
    J --> L
    L -- Yes --> C
    L -- No --> M[Sort Eligible Students]
    M --> N[Apply Tie-Breaking Rules]
    N --> O[Display Scholarship Ranking]
    O --> P([Stop])
---

## 4\. Python Source Code

python

```python
# University Scholarship Allocation System

students = []
eligible_students = []

# Scholarship Eligibility Criteria
MIN_AGGREGATE = 75
MIN_SUBJECT_MARK = 50
MIN_ATTENDANCE = 75
MAX_INCOME = 250000

# Get number of students
n = int(input("Enter number of students: "))

# Collect student details
for i in range(n):

    print("\nEnter details of Student", i + 1)

    name = input("Enter Student Name: ")
    reg_no = int(input("Enter Registration Number: "))

    subjects = int(input("Enter Number of Subjects: "))

    marks = []

    for j in range(subjects):
        mark = float(input(f"Enter marks in Subject {j+1}: "))
        marks.append(mark)

    attendance = float(input("Enter Attendance Percentage: "))
    income = float(input("Enter Annual Family Income: "))

    # Calculate aggregate percentage
    aggregate = sum(marks) / subjects

    # Store student information
    student = {
        "name": name,
        "reg_no": reg_no,
        "aggregate": aggregate,
        "attendance": attendance,
        "income": income,
        "marks": marks
    }

    students.append(student)

    # Check eligibility
    if (aggregate >= MIN_AGGREGATE and
        all(mark >= MIN_SUBJECT_MARK for mark in marks) and
        attendance >= MIN_ATTENDANCE and
        income <= MAX_INCOME):

        eligible_students.append(student)

        print("Status: Eligible for Scholarship")

    else:
        print("Status: Not Eligible for Scholarship")


# Sort eligible students
# Tie-breaking rules:
# 1. Higher aggregate marks
# 2. Higher attendance
# 3. Lower family income
# 4. Lower registration number

eligible_students.sort(
    key=lambda s: (
        -s["aggregate"],
        -s["attendance"],
        s["income"],
        s["reg_no"]
    )
)

# Display scholarship ranking
print("\n======================================")
print(" UNIVERSITY SCHOLARSHIP RANKING")
print("======================================")

if len(eligible_students) == 0:

    print("No students are eligible for scholarships.")

else:

    print("Total Eligible Students:", len(eligible_students))

    print("\nRank  Name       Reg No   Aggregate   Attendance   Income")

    for rank, student in enumerate(eligible_students, start=1):

        print(
            rank,
            student["name"],
            student["reg_no"],
            f"{student['aggregate']:.2f}%",
            f"{student['attendance']}%",
            f"Rs.{student['income']}"
        )

    print("\nScholarship Allocation Completed!")
```

---

## 5\. Sample Source Input

text

```text
Enter number of students: 4

Enter details of Student 1
Enter Student Name: Arun
Enter Registration Number: 101
Enter Number of Subjects: 3
Enter marks in Subject 1: 85
Enter marks in Subject 2: 90
Enter marks in Subject 3: 88
Enter Attendance Percentage: 92
Enter Annual Family Income: 180000

Enter details of Student 2
Enter Student Name: Priya
Enter Registration Number: 102
Enter Number of Subjects: 3
Enter marks in Subject 1: 80
Enter marks in Subject 2: 85
Enter marks in Subject 3: 82
Enter Attendance Percentage: 90
Enter Annual Family Income: 200000

Enter details of Student 3
Enter Student Name: Ravi
Enter Registration Number: 103
Enter Number of Subjects: 3
Enter marks in Subject 1: 70
Enter marks in Subject 2: 80
Enter marks in Subject 3: 75
Enter Attendance Percentage: 85
Enter Annual Family Income: 150000

Enter details of Student 4
Enter Student Name: Divya
Enter Registration Number: 104
Enter Number of Subjects: 3
Enter marks in Subject 1: 90
Enter marks in Subject 2: 95
Enter marks in Subject 3: 92
Enter Attendance Percentage: 95
Enter Annual Family Income: 220000
```

---

## 6\. Sample Source Output

text

```text
Status: Eligible for Scholarship

Status: Eligible for Scholarship

Status: Not Eligible for Scholarship

Status: Eligible for Scholarship

======================================
 UNIVERSITY SCHOLARSHIP RANKING
======================================

Total Eligible Students: 3

Rank  Name       Reg No   Aggregate   Attendance   Income

1     Divya      104      92.33%      95%          Rs.220000
2     Arun       101      87.67%      92%          Rs.180000
3     Priya      102      82.33%      90%          Rs.200000

Scholarship Allocation Completed!
```

---

## 7\. Expected Result

The University Scholarship Allocation System was successfully developed using Python.

The program:

- Accepts student academic and personal details.
- Calculates aggregate marks.
- Checks subject-wise minimum marks.
- Verifies attendance and family income criteria.
- Identifies eligible students.
- Ranks eligible students based on predefined rules.
- Resolves ties using attendance, family income, and registration number.

**Thus, the University Scholarship Allocation System successfully evaluates students and generates a merit-based scholarship ranking.**Here you have to write the code
