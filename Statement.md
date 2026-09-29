# Project Statement & Scope

## 1. Problem Statement

Students may not always have a clear overall view of their academic performance because attendance, marks, quizzes, assignments, and previous results are often considered separately. Specifically:

- **Multiple Academic Parameters:** Reviewing attendance, marks, quiz performance, assignment performance, and previous results separately makes it difficult to understand a student's overall academic condition.
- **Manual Performance Calculation:** Combining different academic parameters manually using different weights can be time-consuming and may lead to calculation errors.
- **Early Risk Identification:** Weak academic performance may be noticed only after examination results, leaving less time for improvement.
- **Lack of Actionable Feedback:** Students may know their marks but still lack a simple indication of their overall risk level and the areas they should focus on.

This project addresses these challenges by providing a lightweight, modular, and offline-capable Python command-line application that calculates a weighted performance score, identifies the student's academic risk level, and provides a recommendation.

---

## 2. Scope of the Project

### In-Scope:

- **Student Record Management:** Adding, displaying, searching, and deleting student records using registration numbers.
- **Weighted Performance Calculation:** Computing an overall performance score using attendance, marks, quiz, assignment, and previous result percentages.
- **Attendance Classification:** Identifying attendance as Good Attendance or Low Attendance using a 75% threshold.
- **Marks Classification:** Identifying marks as Good Marks or Low Marks using a 50% threshold.
- **Academic Risk Classification:** Classifying students as Low Risk, Medium Risk, or High Risk based on the calculated performance score.
- **Recommendation Generation:** Providing improvement advice according to the student's identified risk level.
- **Class Summary:** Displaying individual student scores and calculating the class average.
- **Modular Python Design:** Separating student management, attendance, marks, analysis, risk classification, and recommendation functionality into different Python modules.

### Out-of-Scope:

- Permanent storage using databases or external files.
- Graphical User Interface (GUI) or mobile application.
- Web-based deployment and multi-user access.
- Integration with institutional academic portals or external APIs.
- Machine-learning-based prediction or training on historical student datasets.
- Automated input validation for invalid or out-of-range percentage values in the current version.

---

## 3. Target Users

- **Students:** Students who want a simple way to view their academic performance score, risk level, and recommended improvement areas.
- **Faculty / Academic Mentors:** Faculty members or mentors who want a basic tool for reviewing student academic performance and identifying students who may require additional attention.
- **Academic Project Users:** Users learning fundamental Python programming concepts through a practical student-performance application.

---

## 4. High-Level Features

- **Student Management:** Add, show, search, and delete student records through a menu-driven console interface.
- **Performance Analysis Engine:** Calculates a weighted performance score from five academic parameters.
- **Attendance & Marks Status:** Classifies attendance and marks according to predefined thresholds.
- **Risk Classification Engine:** Maps the performance score to Low Risk, Medium Risk, or High Risk.
- **Recommendation Engine:** Generates advice corresponding to the student's risk level.
- **Class Summary:** Calculates individual performance scores and the overall class average.
- **Modular Architecture:** Uses seven Python modules to separate application responsibilities and keep the code organised.