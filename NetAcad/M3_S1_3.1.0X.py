# 3.1.4 Operators
# The == (equal to) operator compares the values of two operands.
#   If they are equal, the result of the comparison is True.
#   If they are not equal, the result of the comparison is False.

"""var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)"""

# The != (not equal to) operator compares the values of two operands, too.
# Here is the difference:
#   - if they are equal, the result of the comparison is False.
#   - If they are not equal, the result of the comparison is True.

"""var = 0  # Assigning 0 to var
print(var != 0)

var = 1  # Assigning 1 to var
print(var != 0)"""

# 3.1.6 - LAB Variables ‒ Questions and answers -------------------------------------------------------

# Using one of the comparison operators in Python, write a simple two-line program that takes
# the parameter n as input, which is an integer, and prints False if n is less than 100,
# and True if n is greater than or equal to 100.

"""n = int(input("Enter number: "))
print(n >= 100)"""

# 3.1.8 Analyzing code samples -------------------------------------------------------

""""# Example 1:
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)"""

# --------------------------------------------------------------------------------------------------------------

"""# Example 2:
# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1 # if any of the if-elif-else branches contains just one instruction,
# you may code it in a more comprehensive form,
# you don't need to make an indented line after the keyword, but just continue the line after the colon
else: larger_number = number2

# Print the result
print("The larger number is:", larger_number)"""

# --------------------------------------------------------------------------------------------------------------

"""# Example 3:
# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)"""

# 3.1.9 Pseudocode and introduction to loops -------------------------------------------------------------

"""largest_number = -9999999999999999999999
number = int(input("enter data: "))
if number == -1:
    print(largest_number)
    exit()
if number > largest_number:
    largest_number = number
# Go to line 02"""

# -------------------------------------------------------------

"""# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)"""

# 3.1.10 - LAB - Comparison operators and conditional execution ------------------

"""user_input = input("Enter data: ")
if user_input == "Spathiphyllum":
    print("Yes - Spathiphyllum is the best plant ever!")
elif user_input == "spathiphyllum":
    print("No, I want a big Spathiphyllum!")
else:
    print("Spathiphyllum! Not ", user_input, "!")"""

# 3.1.11 - LAB - Essentials of the if-else statement ------------------

"""income = float(input("Enter the annual income: "))

if income < 85528:
    tax = income * 0.18 - 556.02
# Write the rest of your code here.
else:
    tax = (income - 85528) * 0.32 + 14839.02
if tax < 0.0:
    tax = 0.0
tax = round(tax, 0)
print("The tax is:", tax, "thalers")"""

# 3.1.12 - LAB - Essentials of the if-elif-else statement ------------------

"""year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0 or year % 400 != 0:
        print("Common year")
    elif year % 100 != 0:
        print("Leap year")
    else:
        print("Leap year")"""


"""year = int(input("Enter a year: "))

if year < 1582:
    print("Not within the Gregorian calendar period")
else:
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        print("Common year")
    else:
        print("Leap year")"""

# 3.1.14 SECTION QUIZ ------------------------------------------------------------------------

"""x = 5
y = 10
z = 8

print(x > y)
print(y > z)"""

# ------------------------------------------------------------------------

"""x, y, z = 5, 10, 8

print(x > z)
print((y - 5) == x)"""

# ------------------------------------------------------------------------

"""x, y, z = 5, 10, 8
x, y, z = z, y, x

print(x > z)
print((y - 5) == x)"""

# ------------------------------------------------------------------------

"""x = 10

if x == 10:
    print(x == 10)
if x > 5:
    print(x > 5)
if x < 10:
    print(x < 10)
else:
    print("else")"""

# ------------------------------------------------------------------------

"""x = "1"

if x == 1:
    print("one")
elif x == "1":
    if int(x) > 1:
        print("two")
    elif int(x) < 1:
        print("three")
    else:
        print("four")
if int(x) == 1:
    print("five")
else:
    print("six")"""

# ------------------------------------------------------------------------

"""x = 1
y = 1.0
z = "1"

if x == y:
    print("one")
if y == int(z):
    print("two")
elif x == y:
    print("three")
else:
    print("four")"""