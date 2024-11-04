hat_list = [1, 2, 5, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.

hat_list[2] = int(input("Enter a number: "))

# Step 2: write a line of code that removes the last element from the list.

"""hat_list.remove(5) # deletes a value in the list. It will delete it only once."""
hat_list.pop(4)

# Step 3: write a line of code that prints the length of the existing list.

print(f"The lenght of the list is {len(hat_list)} entries")
print(hat_list)
