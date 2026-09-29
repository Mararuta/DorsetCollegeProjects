student =  [{
    "Name": "Alice",
    "Score": 78
},

{
    "Name": "John",
    "Score": 45
},

{
    "Name": "Grace",
    "Score": 90
}]

print(student)


total_score = sum(s["Score"] for s in student)
average_score = total_score / len(student)
top_student = max(student, key=lambda s: s["Score"])

print(student)
print("Average Score:", average_score)
print("Top Student:", top_student["Name"], "with score", top_student["Score"])

student.append({"Name": "Mary", "Score": 66})

total_score1 = sum(s["Score"] for s in student)
average_score1 = total_score1 / len(student)

print("new average", average_score1)
print("new updated student list", student)
