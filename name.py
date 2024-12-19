# Program to swap three numbers given by the user

def swap_numbers(a, b, c):
    # Swapping logic
    a, b, c = c, a, b
    return a, b, c

# Input from user
try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    num3 = int(input("Enter the third number: "))

    print(f"Before swapping: num1 = {num1}, num2 = {num2}, num3 = {num3}")
    
    # Swap the numbers
    num1, num2, num3 = swap_numbers(num1, num2, num3)

    print(f"After swapping: num1 = {num1}, num2 = {num2}, num3 = {num3}")
except ValueError:
    print("Please enter valid integers.")
