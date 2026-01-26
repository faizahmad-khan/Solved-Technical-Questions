class Palindrome:
    
    def is_palindrome(self, x: int) -> bool:
        s = str(x)
        return s == s[::-1]


def main():
    palindrome_checker = Palindrome()
    
    print("Palindrome Checker")
    print("-" * 18)
    
    while True:
        try:
            user_input = input(
                "\nEnter a number to check if palindrome (or 'quit' to exit): "
            )
            
            if user_input.lower() in ['quit', 'exit', 'q']:
                print("Goodbye!")
                break
                
            number = int(user_input)
            
            result = palindrome_checker.is_palindrome(number)
            
            if result:
                print(f"{number} is a palindrome!")
            else:
                print(f"{number} is not a palindrome.")
                
        except ValueError:
            print("Please enter a valid integer or 'quit' to exit.")


if __name__ == "__main__":
    main()