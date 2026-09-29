import json
import os

DATA_FILE = "students_data.json"

students = []
# ---------- helper functions (fix: crash-proof input) ----------

def get_valid_percentage(prompt):
    """Keep asking until the user enters a number between 0 and 100."""
    while True:
        value = input(prompt)
        try:
            value = float(value)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if value < 0 or value > 100:
            print("Please enter a value between 0 and 100.")
            continue

        return value


def get_non_empty_text(prompt):
    """Keep asking until the user enters something other than blank text."""
    while True:
        value = input(prompt).strip()
        if value == "":
            print("This field cannot be empty.")
            continue
        return value


def find_student_by_reg(reg_no):
    for student in students:
        if student["reg_no"] == reg_no:
            return student
    return None


# ---------- persistence (fix: no persistence) ----------

def save_students():
    with open(DATA_FILE, "w") as f:
        json.dump(students, f, indent=4)


def load_students():
    if not os.path.exists(DATA_FILE):
        return

    try:
        with open(DATA_FILE, "r") as f:
            data = json.load(f)
        students.clear()
        students.extend(data)
    except (json.JSONDecodeError, OSError):
        print("Warning: could not read saved student data. Starting fresh.")


# ---------- core features ----------

def add_student():
    print("\n--- Add Student ---")

    reg_no = get_non_empty_text("Enter registration number: ")

    # fix: reject duplicate registration numbers
    if find_student_by_reg(reg_no) is not None:
        print("A student with this registration number already exists.")
        return

    name = get_non_empty_text("Enter student name: ")

    attendance = get_valid_percentage("Enter attendance percentage: ")
    marks = get_valid_percentage("Enter marks percentage: ")
    quiz = get_valid_percentage("Enter quiz percentage: ")
    assignment = get_valid_percentage("Enter assignment percentage: ")
    previous_result = get_valid_percentage("Enter previous result percentage: ")

    student = {
        "reg_no": reg_no,
        "name": name,
        "attendance": attendance,
        "marks": marks,
        "quiz": quiz,
        "assignment": assignment,
        "previous_result": previous_result
    }
    students.append(student)
    save_students()
    print("Student added successfully.")

def show_students():
    print("\n--- Student List ---")
    if len(students) == 0:
        print("No students found.")
        return
    for student in students:
        print("Registration No:", student["reg_no"])
        print("Name:", student["name"])
        print("Attendance:", student["attendance"])
        print("Marks:", student["marks"])
        print("Quiz:", student["quiz"])
        print("Assignment:", student["assignment"])
        print("Previous Result:", student["previous_result"])
        print("------------------------")

def search_student():
    print("\n--- Search Student ---")
    reg_no = input("Enter registration number: ").strip()
    student = find_student_by_reg(reg_no)
    if student is not None:
        print("\nStudent Found")
        print("Name:", student["name"])
        print("Attendance:", student["attendance"])
        print("Marks:", student["marks"])
        print("Quiz:", student["quiz"])
        print("Assignment:", student["assignment"])
        print("Previous Result:", student["previous_result"])
        return
    print("Student not found.")

def delete_student():
    print("\n--- Delete Student ---")
    reg_no = input("Enter registration number: ").strip()
    student = find_student_by_reg(reg_no)
    if student is not None:
        students.remove(student)
        save_students()
        print("Student deleted.")
        return
    print("Student not found.")