# generators
def my_generator(text: str):
    for index, data in enumerate(text):
        if data == '_':
            return
        yield f"{index}: {data}"

result = my_generator('my_text')
print(type(result))
for letter in result:
    print(letter)

# # file operations
#
# file = open("C:/Users/ozy24/PycharmProjects/PEP24G04/modul8/session1/file.txt", 'wt')
# file.write("Hello Python")
# file.flush()
# file.close()
#
# with open("file1.txt", 'wt') as file1:
#     file1.write("Hello Python")
#
# with open("file1.txt", 'rb') as file2:
#     result = file2.read()
#     print(type(result))
#     print(result)


# datetime
