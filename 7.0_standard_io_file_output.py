"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# Exercise 7.0 — Collecting data and saving it
# Name: Tingqi FENG

# 1. In:
# The user enters a first name, last name, date of birth,
# and student number.

# 2. Process:
# The program checks that names are not empty.
# It checks the birth date and rejects future dates.
# It accepts student numbers containing digits only.
# It appends one student record to a CSV file.

# 3. Out, file name and columns:
# File: 7.0_student_data.csv
# Columns: First Name, Last Name, Date of Birth, Student Number

# 4. Why these columns, and what this file is for:
# I chose these columns for a student registration list.
# Names identify students, student numbers help distinguish them,
# and birth dates can support age eligibility checks.
# With 200 records, I could search by student number
# and check eligibility for age-restricted student activities.

# First-run behaviour:
# The program creates the file if it does not exist.
# It writes a header only when the file is empty.

# Invalid-input behaviour:
# Invalid values cause the program to ask the question again.

# Check it yourself:
# Run three times with different student details.
# Check that the CSV has three records and exactly one header.
# Actual test result: complete this comment after testing.


# Your code below

import csv
from datetime import datetime, date


# Ask for a non-empty name on one line.
def ask_name(prompt):
    while True:
        name = input(prompt).strip()

        if name and "\n" not in name and "\r" not in name:
            return name

        print("Please enter a non-empty name on one line.")


# Check the birth date and return it in DD/MM/YYYY format.
def ask_birth_date():
    while True:
        value = input("Date of Birth (DD/MM/YYYY): ").strip()

        try:
            birth_date = datetime.strptime(value, "%d/%m/%Y").date()

            if birth_date > date.today():
                print("The date of birth cannot be in the future.")
                continue

            return birth_date.strftime("%d/%m/%Y")

        except ValueError:
            print("Please enter a valid date, such as 19/09/2004.")


# Keep the student number as text to preserve leading zeros.
def ask_student_number():
    while True:
        student_number = input("Student Number: ").strip()

        if student_number.isascii() and student_number.isdigit():
            return student_number

        print("Please enter a student number using digits only.")


# Append one student record with a single header for the file.
def save_student(first_name, last_name, birth, student_number):
    filename = "7.0_student_data.csv"

    with open(filename, "a+", encoding="utf-8", newline="") as file:
        file.seek(0)
        is_empty = file.read(1) == ""

        writer = csv.writer(file)

        if is_empty:
            writer.writerow([
                "First Name",
                "Last Name",
                "Date of Birth",
                "Student Number"
            ])

        writer.writerow([
            first_name,
            last_name,
            birth,
            student_number
        ])


# Collect and save one student's information.
def main():
    print("Please fill in the following details:")

    first_name = ask_name("First Name: ")
    last_name = ask_name("Last Name: ")
    birth = ask_birth_date()
    student_number = ask_student_number()

    save_student(first_name, last_name, birth, student_number)

    print("Data saved successfully!")


# Handle saving errors or cancelled input.
if __name__ == "__main__":
    try:
        main()
    except OSError as error:
        print("Could not save the student information:", error)
    except (EOFError, KeyboardInterrupt):
        print("\nRegistration cancelled.")