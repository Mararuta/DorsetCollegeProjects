# #from exceptionalHandling import get_eight_ball_response

# #questions = input("Ask the Magic 8-Ball a question: ").strip().lower()

# #try:
# #    if not questions.strip():
# #        raise ValueError("Question cannot be empty.")
# #    response = get_eight_ball_response()
# #    print(f"Magic 8-Ball says: {response}")

# #except ValueError as error:
# #    print(f"ValueError caught: {error}")


# balance = 1000.00

# print("\nWelcome to the class Bank!")

# while True:
#     print("\nPlease choose an option:")
#     print("1. Check Balance")
#     print("2. Deposit Money")
#     print("3. Withdraw Money")
#     print("4. Exit")

#     choice = input("Enter your choice (1-4): ").strip()

#     match choice:
#         case 1:
#             print(f"Your current balance is: ${balance:.2f}")
#         case 2:
#             try:
#                 amount = float(input("Enter the amount to deposit: ").strip())
#                 if amount <= 0:
#                     raise ValueError("Deposit amount must be positive.")
#                 balance += amount
#                 print(f"Successfully deposited ${amount:.2f}. New balance: ${balance:.2f}")
#             except ValueError as error:
#                 print(f"ValueError caught: {error}")
#         case 3:
#             try:
#                 amount = float(input("Enter the amount to withdraw: ").strip())
#                 if amount <= 0:
#                     raise ValueError("Withdrawal amount must be positive.")
#                 if amount > balance:
#                     raise ValueError("Insufficient funds for this withdrawal.")
#                 balance -= amount
#                 print(f"Successfully withdrew ${amount:.2f}. New balance: ${balance:.2f}")
#             except ValueError as error:
#                 print(f"ValueError caught: {error}")
#         case 4:
#             print("Thank you for using the class Bank! Goodbye!")
#             break
#         case _:
#             print("Invalid choice. Please enter a number between 1 and 4.")



print("Temperature converter")

print("1 Celsius to Fahrenheit")
print("2 Fahrenheit to Celsius")
print("3 Celsius to Kelvin")
print("4 Fahrenheit to Kelvin")
print("5 Kelvin to Celsius")
print("6 Kelvin to Fahrenheit")

option = input("Choose an option (1-6): ").strip()

try:
    temperature = float(input("Enter temperature in: ").strip())

    match option:
        case "1":
            result = (temperature * 9/5) + 32
            print(f"{temperature}°C is {result}°F")   
        case "2":
            result = (temperature - 32) * 5/9
            print(f"{temperature}°F is {result}°C")
        case "3":
            result = temperature + 273.15
            print(f"{temperature}°C is {result}K")
        case "4":
            result = (temperature - 32) * 5/9 + 273.15
            print(f"{temperature}°F is {result}K")
        case "5":
            result = temperature - 273.15
            print(f"{temperature}K is {result}°C")
        case "6":
            result = (temperature - 273.15) * 9/5 + 32
            print(f"{temperature}K is {result}°F")
        case _:
            print("Invalid option. Please choose a number between 1 and 6.")

except ValueError as error:
    print("Error:", error)