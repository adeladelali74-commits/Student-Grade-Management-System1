SUBJECTS = ["Math", "Physics", "Programming", "English"]

MIN_GRADE = 0
MAX_GRADE = 100
PASS_MARK = 60

def is_valid_grade(value):
    if value < MIN_GRADE:
        return False
    if value > MAX_GRADE:
        return False
    return True


def read_grade(subject):
    while True:
        grade = float(input(f"Grade for {subject} (0-100): "))
        if is_valid_grade(grade):
            return grade
        print("Invalid grade. Please enter a value between 0 and 100.")


def read_attendance():
    while True:
        attendance = float(input("Attendance percentage (0-100): "))
        if is_valid_grade(attendance):
            return attendance
        print("Invalid value. Please enter a percentage between 0 and 100.")

def calculate_total(grades):
    return sum(grades.values())


def calculate_average(grades):
    return calculate_total(grades) / 4


def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


def calculate_status(average):
    if average >= PASS_MARK:
        return "Pass"
    else:
        return "Fail"


def highest_grade(grades):
    highest = grades[SUBJECTS[0]]
    for subject in SUBJECTS:
        if grades[subject] > highest:
            highest = grades[subject]
    return highest


def lowest_grade(grades):
    lowest = grades[SUBJECTS[0]]
    for subject in SUBJECTS:
        if grades[subject] < lowest:
            lowest = grades[subject]
    return lowest

def add_student(students):
    print("\n----- Add a new student -----")

    name = input("Student name: ")

    grades = {}
    for subject in SUBJECTS:
        grades[subject] = read_grade(subject)

    attendance = read_attendance()

    student_id = len(students) + 1
    student = {
        "id": student_id,
        "name": name,
        "grades": grades,
        "attendance": attendance,
    }

    students.append(student)
    print(f"Student added successfully. ID = {student_id}")
    return student


def find_student(students, keyword):
    matches = []

    for student in students:
        if keyword.isdigit():
            if student["id"] == int(keyword):
                matches.append(student)
        else:
            if keyword.lower() in student["name"].lower():
                matches.append(student)

    return matches


def update_grades(students):
    print("\n----- Update grades -----")

    keyword = input("Enter student ID or name: ")
    matches = find_student(students, keyword)

    if len(matches) == 0:
        print("No student found.")
        return

    student = matches[0]
    print(f"Updating grades for {student['name']} (ID {student['id']})")

    for subject in SUBJECTS:
        print(f"Current {subject}: {student['grades'][subject]}")
        student["grades"][subject] = read_grade(subject)

    print("Grades updated successfully.")


def update_attendance(students):
    print("\n----- Update attendance -----")

    keyword = input("Enter student ID or name: ")
    matches = find_student(students, keyword)

    if len(matches) == 0:
        print("No student found.")
        return

    student = matches[0]
    student["attendance"] = read_attendance()
    print("Attendance updated successfully.")

def display_student(student):
    average = calculate_average(student["grades"])

    print()
    print(f"ID       : {student['id']}")
    print(f"Name     : {student['name']}")
    print("------------------------------")

    for subject in SUBJECTS:
        print(f"{subject}: {student['grades'][subject]}")

    print("------------------------------")
    print(f"Total    : {calculate_total(student['grades'])}")
    print(f"Average  : {average}")
    print(f"Highest  : {highest_grade(student['grades'])}")
    print(f"Lowest   : {lowest_grade(student['grades'])}")
    print(f"Grade    : {calculate_grade(average)}")
    print(f"Status   : {calculate_status(average)}")
    print(f"Attendance: {student['attendance']}%")


def display_all(students, title):
    print(f"\n----- {title} -----")

    if len(students) == 0:
        print("No students to show.")
        return

    for student in students:
        average = calculate_average(student["grades"])
        grade = calculate_grade(average)
        status = calculate_status(average)
        print(f"ID {student['id']} - {student['name']} - Average: {average} - Grade: {grade} - Status: {status}")

def class_statistics(students):
    
    if len(students) == 0:
        return 0, 0, "No students", "No students", 0

    total = 0
    passing = 0
    best_student = students[0]
    worst_student = students[0]

    for student in students:
        average = calculate_average(student["grades"])
        total = total + average

        if average > calculate_average(best_student["grades"]):
            best_student = student

        if average < calculate_average(worst_student["grades"]):
            worst_student = student

        if calculate_status(average) == "Pass":
            passing = passing + 1

    class_average = total / len(students)
    return len(students), class_average, best_student["name"], worst_student["name"], passing


def display_statistics(students):
    print("\n----- Class statistics -----")

    count, class_average, best_name, worst_name, passing = class_statistics(students)

    if count == 0:
        print("There are no students yet.")
        return

    print(f"Number of students : {count}")
    print(f"Class average      : {class_average}")
    print(f"Best student       : {best_name}")
    print(f"Lowest student     : {worst_name}")
    print(f"Students passing   : {passing} / {count}")

def search_and_show(students):
    print("\n----- Search for a student -----")

    keyword = input("Enter student ID or name: ")
    matches = find_student(students, keyword)

    if len(matches) == 0:
        print("No student found.")
        return

    for student in matches:
        display_student(student)

def print_menu():
    print("\n==============================")
    print(" Student Grade Management System")
    print("==============================")
    print(" 1. Add a student")
    print(" 2. Update grades")
    print(" 3. Update attendance")
    print(" 4. Search for a student")
    print(" 5. Display all students")
    print(" 6. Class statistics")
    print(" 0. Exit")   


def run_grade_manager():
    students = []

    while True:
        print_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_student(students)

        elif choice == "2":
            update_grades(students)

        elif choice == "3":
            update_attendance(students)

        elif choice == "4":
            search_and_show(students)

        elif choice == "5":
            display_all(students, "All students")

        elif choice == "6":
           display_statistics(students)
       
        elif choice == "0":
            print("Goodbye!")
            break
        
        else:
            print("Invalid option. Please choose a number from the menu.")


run_grade_manager()