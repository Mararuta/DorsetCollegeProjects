from student import Student
from student_repository import save_student, load_students, find_student_by_id, edit_student_by_id

while True:
    print("===========================")
    print("Student Registry")
    print("===========================")
    print(" 1. Add Student")
    print(" 2. Show all student")
    print(" 3. Search student by Id")
    print(" 4. Edit student by Id")
    print(" 5. Exit")

    choice = input("Choose an option: ").strip()

    match choice:
        case "1":
            student_id = input("Student ID: ").strip()
            name = input("Student Name: ").strip()
            course = input("Student Course: ").strip()

            if not student_id or not name or not course:
                print("A stsudent with that id already exist.")
                continue

            existing_student = find_student_by_id(student_id)
            if existing_student is not None:
                print("A stsudent with that id already exist.")
                continue

            student = Student(student_id, name, course)
            save_student(student)
            print("Student Saved.")

        case "2":
            students = load_students()

            if not students:
                print("\nno students saved yet")
            else:
                print("\n-----------------")
                print("Saved students.")
                for student in students:
                    print(student)
                    

        case "3":
            student_id = input("Enter student ID: ").strip()
            student = find_student_by_id(student_id)

            if student is not None:
                print(student)
            else:
                print("\nStudent not found.")

        case "4":
            existing_student_id = input("Enter the ID of the student to edit: ").strip()
            student = edit_student_by_id(existing_student_id)

            


        case "5":
            print("\nGood Bye!")
            break
        
        case _:
            print("\nInvalid option. Please choos between 1 and 5.")
