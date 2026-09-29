name = input("Enter student name: ").lower()

mark1 = int(input("Enter first mark: "))
mark2 = int(input("Enter second mark: "))
mark3 = int(input("Enter third mark: "))

mark_list = [mark1, mark2, mark3]
average = sum(mark_list) / len(mark_list)

if average >= 50:
    print("passed with average mark of", average)
else:
    print("failed with average mark of", average)

student_dict = {"name": name, "marks": mark_list, "average": average}

import json
try:
    with open("student_data.json", "w") as file:
        json.dump(student_dict, file, indent=4)
except Exception as e:
    print("File can not be opened or written to. Error:", e)