# Question 1: Create a for loop that counts from 0 to 10, and prints odd numbers to the screen.

"""for i in range(0, 11):
    if i % 2 != 0:
        print(i)"""

# Question 2: Create a while loop that counts from 0 to 10, and prints odd numbers to the screen.

"""x = 1
while x < 11:
    if x % 2 != 0:
        print(x)
    x += 1"""

# Question 3: Create a program with a for loop and a break statement. The program should iterate over characters
# in an email address, exit the loop when it reaches the @ symbol, and print the part before @ on one line.

"""for ch in "john.smith@pythoninstitute.org":
    if ch == "@":
        break
    print(ch, end="")"""

# Question 4: Create a program with a for loop and a continue statement. The program should iterate over a string
# of digits, replace each 0 with x, and print the modified string to the screen.

"""for digit in "0165031806510":
    if digit == "0":
        print("x", end="")
        continue
    print(digit, end="")"""

# Question 5: What is the output of the following code?

"""n = 3
while n > 0:
    print(n + 1)
    n -= 1
else:
    print(n)"""

# Explanation:
# Initialization: n is set to 3.
# while n > 0 Loop: The loop continues to run as long as n is greater than 0.
# During each iteration, it prints n + 1 and then decreases n by 1.
# else: block: The else block executes after the while loop finishes.
# In Python, the else block associated with a while loop runs only if the loop terminates normally
# (i.e., without a break).

# Iteration Breakdown:
# First iteration: n = 3. The condition n > 0 is True, so it prints 3 + 1 = 4. Then, n is decreased to 2.
# Second iteration: n = 2. The condition n > 0 is True, so it prints 2 + 1 = 3. Then, n is decreased to 1.
# Third iteration: n = 1. The condition n > 0 is True, so it prints 1 + 1 = 2. Then, n is decreased to 0.
# Fourth iteration: n = 0. The condition n > 0 is now False, so the loop ends.
# At this point, the else block executes and prints the current value of n, which is 0.


# Question 6: What is the output of the following code?
"""n = range(4)
for num in n:
    print(num - 1)
else:
    print(num)"""

# Question 7: What is the output of the following code?
"""for i in range(0, 6, 3):
    print(i)"""