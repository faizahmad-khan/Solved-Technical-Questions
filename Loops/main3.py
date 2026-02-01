# Loop Problems 

# Problem 1: Print a pyramid pattern


print("Problem 1: Pyramid Pattern")
n = 5
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for j in range(i):
        print("* ", end="")
    print()

print("\n" + "="*30 + "\n")




# Problem 2: Check if a number is palindrome
# Example: 121 -> Yes, 123 -> No

print("Problem 4: Check if a number is palindrome")
num = 121
original = num
reversed_num = 0
while num > 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
is_palindrome = original == reversed_num
print(f"{original} is palindrome: {is_palindrome}")

print("\n" + "="*30 + "\n")

# Problem 3: Print multiplication table
# Example: for 5, print 5*1=5, 5*2=10, ..., 5*10=50

print("Problem 5: Multiplication table")
num = 7
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

print("\n" + "="*30 + "\n")



