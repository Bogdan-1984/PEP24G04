# exceptions
# print(11/int(input("Divider:")))

try:
    if True:
        print(11/int(input("Divider:")))
    else:
        pass
except ZeroDivisionError:
    print("Divider should not be 0")
except ValueError:
    print("Not a number")
except Exception:
    print("Some other error happened")
else:
    print("Success")
finally:
    print("All Done")