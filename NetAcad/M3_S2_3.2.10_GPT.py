# 3.2.10 - LAB - The continue statement – the Ugly Vowel Eater

user_word = input("Enter a word: ").upper()

for letter in user_word:
    removed_characters = "AEIOU"
    if letter in removed_characters:
        continue
    print(letter)

# ChatGTP salvation :)))) ------------------------------------------------------------------------

# Certainly! Here are the specific statements regarding the first snippet:

# Placement of .upper() Conversion:
# The input is immediately converted to uppercase with user_word = input("Enter a word: ").upper(),
# making user_word uppercase for the rest of the code.

# Variable Naming:
# The variable chars is used to represent each character,
# which may be slightly confusing because chars sounds plural.

# Final print Statement Placement:
# The final print(chars) is outside the for loop, so it will print only the last character
# of user_word rather than printing each consonant individually.