def basic_calculator():
    print("--- Simple Python Calculator ---")
    
    try:
        # Inputting the two double (float) variables
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        # operation
        print("\nChoose an operation:")
        print(" +  for Addition")
        print(" -  for Subtraction")
        print(" * for Multiplication")
        print(" /  for Division")
        
        choice = input("\nEnter choice (+, -, *, /): ")

        # Performing the calculation based on the operand
        if choice == '+':
            result = num1 + num2
            print(f"\nResult: {num1} + {num2} = {result}")
        elif choice == '-':
            result = num1 - num2
            print(f"\nResult: {num1} - {num2} = {result}")
        elif choice == '*':
            result = num1 * num2
            print(f"\nResult: {num1} * {num2} = {result}")
        elif choice == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"\nResult: {num1} / {num2} = {result}")
            else:
                print("\nError: You cannot divide by zero!")
        else:
            print("\nInvalid input! Please use one of the four operators provided.")
            
    except ValueError:
        print("\nInput Error: Please make sure to enter numeric values.")

# Run the calculator
basic_calculator()
