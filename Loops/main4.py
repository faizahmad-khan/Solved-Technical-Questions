# Problem 1: Sum of digits of a number
# Example: 12345 -> 1+2+3+4+5 = 15

print("Problem 2: Sum of digits of a number")
num = 12345
sum_digits = 0
for digit in str(num):
    sum_digits += int(digit)
print(f"Sum of digits of {num}: {sum_digits}")

print("\n" + "="*30 + "\n")

# Problem 2: Reverse a number using loops
# Example: 12345 -> 54321

print("Problem 3: Reverse a number")
num = 12345
reversed_num = 0
temp = num
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp = temp // 10
print(f"Reversed number of {num}: {reversed_num}")

print("\n" + "="*30 + "\n")

# Problem 3: Count vowels in a string
# Example: "hello" -> 2 vowels (e, o)

print("Problem 6: Count vowels in a string")
string = "hello world"
vowels = "aeiouAEIOU"
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels in '{string}': {count}")

print("\n" + "="*30 + "\n")
