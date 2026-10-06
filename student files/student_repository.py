from student import Student

DATA_FILE = "students.txt"

def save_student(student):
    with open (DATA_FILE, "a", encoding="utf-8") as file:
        file.write(student.to_file_line() + "\n")

def load_students():
    students = []

    try:
        with open (DATA_FILE, "r", encoding="utf-8") as file:
            for line in file:
                student = Student.from_file_line(line)

                if student is not None:
                    students.append(student)
    except FileNotFoundError:
        return[]

    return students    

def find_student_by_id(student_id):
    students = load_students()

    for student in students:
        if student.student_id.lower() == student_id.lower():
            return student
    return None

def edit_student_by_id(student_id):
    students = load_students()

    for student in students:
        if student.student_id.lower() == student_id.lower():
            return student
    return None