import json
import os
import re
import tkinter as tk
from tkinter import messagebox

def load_students(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

def print_students(students, title):
    print(f"\n--- {title} ---")
    for student in students:
        print(f"{student['L_Name']}, {student['F_Name']} : ID = {student['Student_ID']} , Email = {student['Email']}")

def add_student(students, first, last, student_id, email):
    new_student = {
        "F_Name": first,
        "L_Name": last,
        "Student_ID": student_id,
        "Email": email
    }
    students.append(new_student)

def save_students(filename, students):
    with open(filename, 'w') as file:
        json.dump(students, file, indent=4)
    print("\nstudent.json file has been updated.")

def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        else:
            print("Input cannot be empty. Please try again.")

def get_valid_student_id(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit():
            return int(value)
        else:
            print("Invalid ID. Please enter a number.")

def get_valid_email(prompt):
    email_pattern = r"[^@]+@[^@]+\.[^@]+"
    while True:
        email = input(prompt).strip()
        if re.match(email_pattern, email):
            return email
        else:
            print("Invalid email format. Try again.")

def collect_new_student():
    print("\nPlease enter new student information:")
    first = get_non_empty_input("First Name: ")
    last = get_non_empty_input("Last Name: ")
    student_id = get_valid_student_id("Student ID (numbers only): ")
    email = get_valid_email("Email: ")
    return first, last, student_id, email

def ask_to_add_student(filepath):
    root = tk.Tk()
    root.withdraw()
    result = messagebox.askquestion(
        "File Modified",
        f"{filepath}\n\nThis file has been modified outside. Do you want to reload it?"
    )
    root.destroy()
    return result == "yes"

def main():
    filename = 'student.json'
    students = load_students(filename)

    print_students(students, "Original Student List")

    first, last, student_id, email = collect_new_student()

    full_path = os.path.abspath(filename)
    if ask_to_add_student(full_path):
        add_student(students, first, last, student_id, email)
        save_students(filename, students)
        print_students(students, "Updated Student List")
    else:
        print("Exiting...")

if __name__ == "__main__":
    main()
