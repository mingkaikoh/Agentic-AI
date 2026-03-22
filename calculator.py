def basic_calculator():
    print("--- Simple Python Calculator ---")
    
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        
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
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")

    # error
    except ValueError:
        print("\nInput Error: Please make sure to enter numeric values.")

# Run the calculator
def main():
    basic_calculator()

if __name__ == "__main__":
    main()
    hello()
    bye()
    no()
