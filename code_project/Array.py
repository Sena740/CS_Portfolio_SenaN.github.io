#Student Information System
#2024/10/08 By Sena Nishimura
student_info = {
    "1": {"name": "Jack", "mail": "jacky_chen@gmail.com", "course": "English", "grade": "D"},
    "2": {"name": "Eric", "mail": "eric_can@gmail.com", "course": "French", "grade": "B"},
    "3": {"name": "Oliver", "mail": "oli_oliver@gmail.com", "course": "Physics", "grade": "C"},
}

def Return(): #function used to return to the options menu after the user completes an operation
    try:
        home = int(input("Press '0' to return to options: "))
        if home != 0:
            print("Invalid option")
            Return()
        elif home == 0:
            print("\nReturning to options...\n")
            welcome()
    except ValueError:
        print("Invalid option. Please enter 0: ")
        Return()

def op1(): #function that prints out the information
    print("------------------------------------------------------------")
    #prints in a table format
    print("{:<5} {:<10} {:<25} {:<10} {:<10}".format('ID#','Name', 'Mail', 'Class', 'Grade'))
    for student, info in student_info.items():
        print("{:<5} {:<10} {:<25} {:<10} {:<10}".format(student, info['name'], info['mail'], info['course'], info['grade']))
    print("------------------------------------------------------------")
    Return()

def op2(): #function that lets the user add a new student information
    print("--------------------")
    student = input("Enter new student ID#: ")
    if student in student_info: #checks if the student ID# is already taken
        print("Student ID# already exists.")
        op2()

    name = input("Enter student's name: ")
    mail = input("Enter student's mail: ")
    course = input("Enter student's course: ")
    grade = input("Enter student's grade: ")

    student_info[student] = {"name": name, "mail": mail, "course": course, "grade": grade}
    print("--------------------\nStudent added successfully.")
    more = input("Would you like to add more students? y/n : ")
    if more =="y":
        op2()
    elif more == "n":
        Return()

def op3(): #function that lets the user update the student info
    print("-----------------------------")
    student_id = input("Enter student ID# to update: ")
    if student_id not in student_info:
        print("Student ID# not found.")
        op3()
    name = input("Enter new name (leave blank to keep current): ")
    mail = input("Enter new mail (leave blank to keep current): ")
    course = input("Enter new course (leave blank to keep current): ")
    grade = input("Enter new grade (leave blank to keep current): ")

    if name:
        student_info[student_id]['name'] = name
    if mail:
        student_info[student_id]['mail'] = mail
    if course:
        student_info[student_id]['course'] = course
    if grade:
        student_info[student_id]['grade'] = grade
    print("----------------------------\nStudent updated successfully")
    ask = input("Would like to update any other info? y/n : ")
    if ask == "y":
        op3()
    elif ask == "n":
        Return()

def op4(): #function that lets the user remove a student info
    print("----------------------------")
    student_id = input("Enter student ID# to remove: ")
    if student_id in student_info:
        del student_info[student_id]
        print("Student removed successfully.")
        print("----------------------------")
        ask = input("Would you like to delete more info? y/n :")
        if ask == "y":
            op4()
        elif ask == "n":
            Return()
    else:
        print("Student ID# not found.")
        op4()

def welcome(): #lets the user pick an option
    print("Please select an option from below:\n1:View Info\n2:Add Info\n"
          "3:Update Info\n4:Delete Info\n5:End Process\n-------------")
    option = input("Your Option: ")
    if option == "1":
        op1()
    elif option == "2":
        op2()
    elif option == "3":
        op3()
    elif option == "4":
        op4()
    elif option == "5":
        print("Closing Program...")
    else:
        print("Invalid option\n")
        welcome()

print("Welcome to the student information menu")
welcome()