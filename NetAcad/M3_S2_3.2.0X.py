# 3.2.2 An infinite loop
"""while True:
    print("I'm stuck inside a loop.")"""

# ---------------------------------------------------------------------------------

"""# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)"""

# ---------------------------------------------------------------------------------

# 3.2.3 The while loop: more examples

"""# A program that reads a sequence of numbers
# and counts how many numbers are even and how many are odd.
# The program terminates when zero is entered.
odd_numbers = 0
even_numbers = 0

# Read the first number.
number = int(input("Enter a number or type 0 to stop: "))

# 0 terminates execution.
while number != 0:
    # Check if the number is odd.
    if number % 2 == 1:
        # Increase the odd_numbers counter.
        odd_numbers += 1
    else:
        # Increase the even_numbers counter.
        even_numbers += 1
    # Read the next number.
    number = int(input("Enter a number or type 0 to stop: "))

# Print results.
print("Odd numbers count:", odd_numbers)
print("Even numbers count:", even_numbers)"""

# ---------------------------------------------------------------------------------
"""counter = 5
while counter:
    print("Inside the loop.", counter)
    counter -= 1
print("Outside the loop.", counter)"""

# ---------------------------------------------------------------------------------
# 3.2.4 - LAB - Guess the secret number


"""secret_number = 777
user_input = int(input("Enter number: "))
while user_input != secret_number:
    print("Ha ha! You're stuck in my loop!")
    user_input = int(input("Enter number: "))
    if user_input == secret_number:
        continue
print("Success")
"""

# -----------------------------------------
"""secret_number = 777
while True:
    user_input = int(input("Enter number: "))
    if user_input == secret_number:
        print("You are right")
        break
    else:
        print("Ha ha! You're stuck in my loop!")"""

# ---------------------------------------------------------------------------------

# 3.2.7 - LAB - Essentials of the for loop – counting mississippily

# ---------------------------------------------------------------------------------

# 3.2.8 The break and continue statements

"""largest_number = -99999999
counter = 0

while True:
    number = int(input("Enter a number or type -1 to end the program: "))
    if number == -1
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")"""

# ----------------------------------------------------------------------------------------

"""largest_number = -99999999
counter = 0

number = int(input("Enter a number or type -1 to end program: "))

while number != -1:
    if number == -1:
        continue
    counter += 1

    if number > largest_number:
        largest_number = number
    number = int(input("Enter a number or type -1 to end the program: "))

if counter:
    print("The largest number is", largest_number)
else:
    print("You haven't entered any number.")"""

