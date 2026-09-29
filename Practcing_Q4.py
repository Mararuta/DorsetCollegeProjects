import csv

students = []

with open("exam_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Module", "Score"])
    writer.writerow(["ALice", "Python 2", 78])
    writer.writerow(["jhon", "Python 2", 45])
    writer.writerow(["Mary", "Python 2", 66])
    writer.writerow(["Grace", "Python 2", 90])
    writer.writerow(["David", "Python 2", 52])

with open("exam_results.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        students.append(row)

    for row in reader:
        print(row["Name"], row["Module"], row["Score"])
    
       

students.sort(key=lambda x: x["Score"])

for student in students:
    print(student["Name"], student["Score"])

name = input("Enter student name: ").lower()

found = False

for student in students:
    if student["Name"].lower() == name:
        print("NAME -", "MODULE -", "SCORE")
        print(student["Name"], "-", student["Module"], "-", student["Score"])
        found = True
        break

if not found:
    print("Student not found")
