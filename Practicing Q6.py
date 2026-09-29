names = ["Mary", "Jhon", "Grace", "Alice", "David"]

sorted_names = sorted(names)

print(sorted_names)

name_input = input("Enter student name: ").strip().lower()

found = False
for name in sorted_names:
    if name.lower() == name_input:
        found = True
        break
if found:
    print("Student name found in the list.")
else:
    print("Student name not found in the list.")

    





























    