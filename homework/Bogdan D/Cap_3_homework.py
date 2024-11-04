element_list = ['abc', 123, '1', 1]

# Cerinta 1:
for character in element_list:
    print(f"Element: {character}, Type: {type(character)}")

# nu stiu cum sa fac aliniatul 2


print()
# Cerinta 2
user_input = input("Introdu un cuvant: ")
list_conversion = list(user_input)
vocale = "aeiouAEIOU"
nr_vocale = 0
for caracter in user_input:
    if caracter in vocale:
        nr_vocale += 1
print(f"Nr de vocale din cuvant: {nr_vocale}")

# --------------------------------------------------
