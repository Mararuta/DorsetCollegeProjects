from datetime import date

try:
    with open("attendance_notes2.txt", "w", encoding="utf-8") as file:
        file.write("Python class attendance was recorded successfully.")

    today_date = date.today().strftime("%Y-%m-%d")

    with open("attendance_notes2.txt", "a", encoding="utf-8") as file:
        file.write(f"\nGrace {today_date}")

    with open("attendance_notes2.txt", "r", encoding="utf-8") as file:
       read = file.read()

    print(read)

except Exception as e:
    print("An error occurred:", e)

