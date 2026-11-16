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

# 1. In:
# The user enters a student's name, age, course, and marks.

# 2. Process:
# The program collects the information and saves it in a CSV file.
# If the file does not exist, it creates one with a header.
# If it already exists, it adds another row.
# Invalid values are rejected and the user is asked again.

# 3. Out, file name and columns:
# File name: student_records.csv
# Columns: Name, Age, Course, Marks

# 4. Why these columns, and what this file is for:
# I chose these columns to record student information.
# With 200 rows, I could compare marks and calculate averages.


# Your code below

import csv
import os


filename = "7.0_student_data.csv"


name = input("Enter student name: ").strip()
while name == "":
    name = input("Please enter a name: ").strip()

while True:
    try:
        age = int(input("Enter student age: "))
        if age > 0:
            break
        print("Please enter a positive age.")
    except ValueError:
        print("Please enter a valid number.")

course = input("Enter course: ").strip()
while course == "":
    course = input("Please enter a course: ").strip()

while True:
    try:
        marks = float(input("Enter marks (0-100): "))
        if 0 <= marks <= 100:
            break
        print("Marks must be between 0 and 100.")
    except ValueError:
        print("Please enter valid marks.")

file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0

with open(filename, "a", newline="") as file:
    writer = csv.writer(file)

    if not file_exists:
        writer.writerow(["Name", "Age", "Course", "Marks"])

    writer.writerow([name, age, course, marks])

print("Student information saved successfully!")
print("File created:", os.path.abspath(filename))
