# # generators
# def my_generator(text: str):
#     for index, data in enumerate(text):
#         if data == '_':
#             return
#         yield f"{index}: {data}"
#
# result = my_generator('my_text')
# print(type(result))
# for letter in result:
#     print(letter)
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
import datetime

date1 = datetime.datetime(2020, 10, 10)
date2 = datetime.datetime(2020, 10, 8)
print(date1 > date2)
date_now = datetime.datetime.now()
print(date_now)
print(date_now - date1)
print(type(date_now - date2))
# print(datetime.datetime.now().strftime('%Y-%m-%d'))
result = datetime.datetime.strptime('1998-4-1', '%Y-%m-%d')
print(result)
