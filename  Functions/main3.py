def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract two numbers"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide two numbers"""
    if y == 0:
        return "Error: Division by zero is not allowed!"
    return x / y

def main():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        # Take input from the user
        choice = input("\nEnter choice (1/2/3/4) or 'quit' to exit: ")
        
        if choice.lower() == 'quit':
            print("Exiting calculator. Goodbye!")
            break
        
        # Check if choice is one of the four options
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter numeric values.")
                continue
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):  # Error message
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice! Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()