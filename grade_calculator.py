# Grades Calculator Program

# -------------------------------
# Step 1: Initialize Data
# -------------------------------
student_grades = {
    "Abby": [88, 94, 79],
    "Jordan": [72, 85, 90],
    "Timothy": [95, 91, 87]
}
# -------------------------------
# Step 2: Calculate Average Grades
# -------------------------------
student_averages = {}
for student, grades in student_grades.items():
    avg = sum(grades) / len(grades)
    student_averages[student] = avg

# -------------------------------
# Step 3: Determine Letter Grades
# -------------------------------
student_letter_grades = {}
for student, avg in student_averages.items():
    if avg >= 90:
        letter = "A"
    elif avg >= 80:
        letter = "B"
    elif avg >= 70:
        letter = "C"
    elif avg >= 60:
        letter = "D"
    else:
        letter = "F"
    student_letter_grades[student] = letter

# -------------------------------
# Step 4: Find the Top Performer
# -------------------------------
top_student = None
top_average = 0
for student, avg in student_averages.items():
    if avg > top_average:
        top_student = student
        top_average = avg

# -------------------------------
# Step 5: Class Statistics
# -------------------------------
# Overall class average
overall_class_average = sum(student_averages.values()) / len(student_averages)

# Count passing students (C or better)
passing_count = 0
for grade in student_letter_grades.values():
    if grade in ["A", "B", "C"]:
        passing_count += 1

# -------------------------------
# Step 6: Display Results
# -------------------------------
print("---- Student Averages ----")
for student, avg in student_averages.items():
    print(f"{student}: {avg:.2f} ({student_letter_grades[student]})")

print("\n---- Top Performer ----")
print(f"{top_student} with an average of {top_average:.2f}")

print("\n---- Class Statistics ----")
print(f"Overall Class Average: {overall_class_average:.2f}")
print(f"Number of Students Passing (C or better): {passing_count}")
