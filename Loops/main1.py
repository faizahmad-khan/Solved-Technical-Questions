# Problem 1: Find the largest number in a list using loop
# Example: [45, 23, 89, 12, 56] -> 89

print("Problem 7: Find the largest number in a list")
numbers = [45, 23, 89, 12, 56]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num
print(f"Largest number in {numbers}: {largest}")

print("\n" + "="*30 + "\n")

# Problem 2: Print Fibonacci series up to n terms
# Example: n=5 -> 0, 1, 1, 2, 3

print("Problem 8: Fibonacci series")
n = 8
a, b = 0, 1
print(f"First {n} Fibonacci numbers:")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

