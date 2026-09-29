import csv

records = []

with open("exam_result2.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    writer.writerow(["Name", "Module", "Score"])
    writer.writerow(["Alice", "Python2", 78])
    writer.writerow(["John", "Python2", 45])
    writer.writerow(["Mary", "Python2", 66])
    writer.writerow(["Grace", "Python2", 90])
    writer.writerow(["David", "Python2", 52])
            

with open("exam_result2.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["Name"], row["Module"], row["Score"])
        records.append(row)

# Sort using lambda key targeting 'Score'
sorted_records = sorted(records, key=lambda x: x["Score"])

print("\n--- Sorted Student Scores (Lowest to Highest) ---")
for student in sorted_records:
    print(f"Name: {student['Name']}, Score: {student['Score']}")

print("-" * 40)
name = input("Enter a student Name: ").lower()
found = False

for student in sorted_records:
    if student["Name"].lower() == name:
        print("\n Student record found")
        print("NAME -", "MODULE -", "SCORE")
        print(student["Name"], "-", student["Module"], "-", student["Score"])
        found = True
        break

if not found:
    print("Student not found")
