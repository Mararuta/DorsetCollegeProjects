from datetime import date

try:
    
    with open("attendance_notes.txt", "w", encoding="utf-8") as file:
        file.write("Python class attendance was recorded successfully")

    date_today = date.today()
    
    with open("attendance_notes.txt", "a", encoding="utf-8") as file:
        file.write(f"\n Grace {date_today}")

    with open("attendance_notes.txt", "r", encoding="utf-8") as file:
        file = file.read()
        print(file)

except Exception as e:
    print("File can not be opened or written to. Error:", e)

