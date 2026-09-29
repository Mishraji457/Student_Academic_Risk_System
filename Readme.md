# Student Academic Risk System

A modular Python command-line application for identifying students who may be at academic risk based on attendance, marks, quiz performance, assignment performance, and previous results. The system calculates a weighted performance score, classifies students into Low, Medium, or High Risk, and provides a recommendation for improvement.

---

## Table of Contents

- [Problem Statement](#problem-statement)
- [Objective](#objective)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Project Architecture](#project-architecture)
- [Scoring Formula](#scoring-formula)
- [Risk Classification](#risk-classification)
- [Installation & Setup](#installation--setup)
- [Usage Guide](#usage-guide)
- [Testing](#testing)
- [Limitations](#limitations)
- [Future Enhancements](#future-enhancements)

---

## Problem Statement

A student's weak academic performance may be noticed only after examination results are declared, leaving limited time for improvement. Attendance, marks, quizzes, and assignments are often considered separately, making it difficult to view a student's overall academic condition at a glance.

The **Student Academic Risk System** addresses this problem by combining multiple academic parameters using a fixed weighted formula, identifying the student's academic risk level, and providing a recommendation based on the result.

---

## Objective

The main objectives of the project are:

- To develop a Python-based console application for student academic risk analysis.
- To apply fundamental Python concepts such as functions, loops, conditional statements, lists, dictionaries, and modules.
- To calculate a weighted performance score using five academic parameters.
- To classify students into Low, Medium, or High Risk.
- To generate a recommendation corresponding to the identified risk level.
- To provide a simple menu-driven interface for managing and analysing student records.

---

## Key Features

* **Student Record Management:** Add, display, search, and delete student records.
* **Attendance Classification:** Classifies attendance as Good Attendance or Low Attendance using a 75% threshold.
* **Marks Classification:** Classifies marks as Good Marks or Low Marks using a 50% threshold.
* **Weighted Performance Score:** Calculates an overall score from attendance, marks, quiz, assignment, and previous result percentages.
* **Academic Risk Classification:** Categorises students as Low Risk, Medium Risk, or High Risk based on their performance score.
* **Personalised Recommendation:** Provides improvement advice according to the student's risk level.
* **Class Summary:** Displays individual student scores and calculates the class average.
* **Modular Design:** Separates student management, analysis, risk classification, and recommendation logic into individual Python modules.

---

## Tech Stack

* **Programming Language:** Python 3.8 or higher
* **Application Type:** Command-line / console application
* **Libraries:** Python standard library only
* **Data Structures:** Lists and dictionaries
* **Data Storage:** In-memory storage during program execution
* **Development Environment:** VS Code, PyCharm, IDLE, or any text editor

No external Python packages are required.

---

## Project Architecture

The application follows a simple layered architecture:

```text
Student Academic Risk System
│
├── main.py
│   ├── Menu interface
│   ├── Student analysis
│   └── Class summary
│
├── student.py
│   ├── Student records
│   ├── Add student
│   ├── Show students
│   ├── Search student
│   └── Delete student
│
├── attendance.py
│   └── Attendance classification
│
├── marks.py
│   └── Marks classification
│
├── analysis.py
│   └── Weighted performance score
│
├── risk.py
│   └── Risk classification
│
└── recommendation.py
    └── Improvement recommendations
```

### Module Responsibilities

| Module | Responsibility |
|---|---|
| `main.py` | Displays the menu, handles user choices, analyses individual students, and generates the class summary. |
| `student.py` | Stores student records and provides add, show, search, and delete operations. |
| `attendance.py` | Determines whether attendance is Good or Low. |
| `marks.py` | Determines whether marks are Good or Low. |
| `analysis.py` | Calculates the weighted performance score. |
| `risk.py` | Converts the performance score into a risk level. |
| `recommendation.py` | Generates advice according to the risk level. |

---

## Scoring Formula

The system calculates the performance score using five academic parameters:

```text
Performance Score =
    0.25 × Attendance
  + 0.30 × Marks
  + 0.15 × Quiz
  + 0.15 × Assignment
  + 0.15 × Previous Result
```

### Parameter Weights

| Parameter | Weight |
|---|---:|
| Attendance | 25% |
| Marks | 30% |
| Quiz | 15% |
| Assignment | 15% |
| Previous Result | 15% |
| **Total** | **100%** |

All input values are percentages.

---

## Risk Classification

The calculated performance score is mapped to a risk level using the following rules:

| Performance Score | Risk Level | Recommendation Focus |
|---|---|---|
| `75` and above | Low Risk | Maintain attendance and consistency |
| `50` to below `75` | Medium Risk | Focus on weak subjects, marks, and assignments |
| Below `50` | High Risk | Attend regularly, improve marks, and practise quizzes |

The system also uses these status thresholds:

- **Attendance:** `75%` or above → Good Attendance
- **Marks:** `50%` or above → Good Marks

---

## Installation & Setup

### 1. Install Python

Make sure Python 3.8 or higher is installed:

```bash
python --version
```

### 2. Open the Project

Open the project folder in VS Code, PyCharm, IDLE, or another Python-compatible editor.

The seven Python files should be kept in the same folder.

### 3. Run the Application

Start the program using:

```bash
python main.py
```

No external packages or `pip install` commands are required.

---

## Usage Guide

After starting the application, the main menu provides the following options:

```text
==============================
 STUDENT ACADEMIC RISK SYSTEM
==============================
1. Add Student
2. Show Students
3. Search Student
4. Analyze Student
5. Class Summary
6. Delete Student
7. Exit
```

### 1. Add Student

Enter:

- Registration number
- Student name
- Attendance percentage
- Marks percentage
- Quiz percentage
- Assignment percentage
- Previous result percentage

The record is stored in memory.

### 2. Show Students

Displays all currently stored student records and their academic parameters.

### 3. Search Student

Enter a registration number to find and display a student's record.

### 4. Analyze Student

Enter a registration number to calculate:

- Attendance status
- Marks status
- Performance score
- Risk level
- Recommendation

### 5. Class Summary

Calculates and displays the performance score for every student and the overall class average.

### 6. Delete Student

Removes a student record using the registration number.

### 7. Exit

Terminates the application.

---

## Example

For a student with:

```text
Attendance       = 40
Marks            = 35
Quiz             = 30
Assignment       = 45
Previous Result  = 40
```

The calculated score is:

```text
0.25(40) + 0.30(35) + 0.15(30) + 0.15(45) + 0.15(40)
= 37.75
```

Therefore:

```text
Risk Level: High Risk
```

The system recommends regular attendance, improvement in marks, timely completion of assignments, and regular quiz practice.

---

## Testing

The project was tested using functional test cases covering:

- Adding and displaying student records
- Searching for an existing student
- Searching for a deleted student
- All parameters equal to `100`
- All parameters equal to `0`
- Risk boundary at score `75`
- Risk boundary at score `50`
- Score just below `50`
- Invalid menu choice
- Class summary calculation

The documented test cases passed for valid inputs.

### Known Input-Validation Issue

The current version does not validate numeric input. If text such as `abc` is entered where a percentage is expected, the program stops with a `ValueError`.

Input validation is listed as a future enhancement.

---

## Limitations

- Student records are stored only in memory and are lost when the program exits.
- Numeric input is not validated.
- Values outside the `0–100` range are currently accepted.
- Duplicate registration numbers are allowed.
- Search, analysis, and deletion operate on the first matching registration number.
- The scoring weights and risk thresholds are fixed in the program and are not based on real institutional data.
- The application currently supports a single user through a console interface.

---

## Future Enhancements

The project can be extended by:

1. Adding input validation using `try/except` and `0–100` range checks.
2. Storing records permanently using CSV, JSON, or SQLite.
3. Preventing duplicate registration numbers.
4. Building a graphical user interface using Tkinter.
5. Adding subject-wise academic records.
6. Adding class-performance charts using Matplotlib.
7. Deploying the system as a web application using Flask or Streamlit.

---

## Project Context

This project was developed as a first-year academic project to demonstrate the practical application of fundamental Python programming concepts through a small, modular, and functional academic analysis system.