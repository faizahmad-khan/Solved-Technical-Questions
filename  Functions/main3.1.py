def is_palindrome(number):
    """
    Check if a number is a palindrome or not.
    
    Args:
        number: An integer to check
    
    Returns:
        bool: True if the number is a palindrome, False otherwise
    """
    # Convert number to string to easily compare digits
    str_num = str(abs(number))  # Use abs() to handle negative numbers
    
    # Compare the string with its reverse
    return str_num == str_num[::-1]


def main():
    # Test cases
    test_numbers = [121, 123, 1221, 12321, 1234, -121, 0, 7]
    
    print("Testing palindrome function:")
    for num in test_numbers:
        result = is_palindrome(num)
       print (f"{num} is {'a palindrome' if result else 'not a palindrome'}")


if __name__ == "__main__":
    main()