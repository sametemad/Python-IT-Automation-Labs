def calculate(choice, num1, num2):
    if choice == "1":
        return num1 + num2

    elif choice == "2":
        return num1 - num2

    elif choice == "3":
        return num1 * num2

    elif choice == "4":
        if num2 == 0:
            return None
        else:
            return num1 / num2


while True:
    print("CLI Calculator")
    print("Choose an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice 1-5: ")
    print("You selected:", choice)

    if choice == "5":
        print("Goodbye!")
        break

    if choice not in ["1", "2", "3", "4"]:
        print("Invalid choice. Please select a number from 1 to 5.")
        print()
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    except ValueError:
        print("Error: Please enter valid numbers.")
        print()
        continue

    print("First number:", num1)
    print("Second number:", num2)

    result = calculate(choice, num1, num2)

    if choice == "4" and result is None:
        print("Error: Cannot divide by zero.")

    else:
        print("Result:", result)

    print()