c0 = int(input("Give number: "))
count = 0
if c0 >= 0:
    while c0 != 1:
        if c0 % 2:
            print("Odd number")
            c0 = 3 * c0 + 1
        else:
            print("Even number")
            c0 = c0/2
        count += 1
else:
    print("Not a good number")
print(count)