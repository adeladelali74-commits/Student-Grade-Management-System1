def get_valid_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter {subject} grade : ")) 
            if 0<=grade<=100 :
               return grade
            else: 
                print("Invalid grade! Please enter a grade between 0 and 100")
        except ValueError:
            print("Please enter a number !")
       
def calculate_average(math,english,science,programming):
    total=math + english + science + programming
    average=total / 4
    return average

def calculate_grade(average):
    if average >= 90 :
     return "A"

    elif average >= 80 :
        return "B"
        
    elif average >= 70 :
        return "C"
    
    elif average >= 60 :
        return "D"
    else :
        return "F"
students = []
def add_student():
    id =input("Please Enter Your ID : ")
    name =input("Please Enter Your name : ")  
    math =get_valid_grade("math")
    english =get_valid_grade("english")
    science=get_valid_grade("science")
    programming=get_valid_grade("programming")
    average=calculate_average (
        math,
        english,
        science,
        programming )
    grade=calculate_grade(average)
    print("Student Average:", average)
    print("Student Grade:", grade)
    print ("Student added successfuly")
    student = {
        "id":id,
        "name":name,
        "math":math,
        "english":english,
        "science":science,
        "programming":programming,
        "average":average,
        "grade":grade }
    return student
def loop():
    while True:
        answer=input("Do you want to add another student ( yes/no) ? ")
        if answer == "yes" :
            student=add_student()
            students.append(student)
        else:
            print("**With my best wishes**")  
            break
def display_student():
     for student in students :
        print("ID : " , student["id"])
        print("NAME : " ,student["name"])
        print("AVERAGE : ",student["average"])
        print("GRADE : " ,student["grade"])
def find_student():
    while True:
        found = False
        search_type=input("search by id or name ? ")
        if search_type == "id":
            find_id=input("Please enter your id : ")
        elif search_type=="name":
            find_name=input("Please enter your name : ")
        for student in students:
            if search_type == "id":
                if find_id==student["id"]:
                    print(student)
                    found=True
            elif search_type=="name":
                if find_name==student["name"]:
                    print (student)
                    found=True      
        if found == False:
            print ("Student not found")
        
        assign = input("Do you want to search for another student ? (yes/no) : ")
        if assign =="no":
            break  
def update_grades():
    found=False
    update=input("Please enter your id : ")
    for student in students:
        if update == student["id"]:
            student["math"]=get_valid_grade("math")
            student["english"]=get_valid_grade("english")
            student["science"]=get_valid_grade("science")
            student["programming"]=get_valid_grade("programming")
            average = calculate_average(
                student["math"],
                student["english"],
                student["science"],
                student["programming"])
            student["average"]=average
            student["grade"]=calculate_grade(average)
            found=True
    if found==False:
        print("Student not found")
def class_statistics():
    total_average=0
    passing_students = 0
    highest_student=students[0]
    lowest_student=students[0]
    for student in students:
        total_average=total_average+student["average"]
        if student["average"] > highest_student["average"]:
             highest_student=student
        if student["average"] < lowest_student["average"]:
            lowest_student = student
        if student["grade"] != "F":
            passing_students = passing_students + 1   
    class_average=total_average/len(students)
    print("Class Average  :", class_average)          
    print("Highest Student :", highest_student["name"])
    print("Highest Average :", highest_student["average"])
    print("Lowest Student :", lowest_student["name"])
    print("Lowest Average :", lowest_student["average"])
    print("Passing Students :", passing_students)
def sort_students():
    sorted_students = students.copy()
    for i in range (len(sorted_students)):
        for j in range(0,len(sorted_students)-i-1):
            if sorted_students[j]["average"]<sorted_students[j+1]["average"]:
                sorted_students[j],sorted_students[j+1]=sorted_students[j+1],sorted_students[j]
    for student in sorted_students:
        print (student["name"], "-" , student["average"]) 
def run_grade_manager():
    while True :
        print("1- Add Student ")
        print("2- Update Grades")
        print("3- Find Student")
        print("4- Display Student")
        print("5- Class Statistics ")
        print("6- Sort Students")
        print("7- Exit")

        choice = input("Enter your choice : ")
        if choice == "1":
            loop()
        elif choice == "2":
            update_grades()
        elif choice == "3":
            find_student()
        elif choice == "4":
            display_student()
        elif choice == "5":
            class_statistics()
        elif choice == "6":
            sort_students()
        elif choice == "7":
            break
        else:
            print("Please enter a number from 1 to 7!")
run_grade_manager()

