def processed_output(list_of_str: list[str]):
    for item in list_of_str:
        processed_item = item.strip().split(':')
        yield tuple(map(lambda e: e.strip(), processed_item))

with open('experiment.txt', 'r') as file:
    result = file.readlines()
    output = processed_output(result)

result = dict(list(output))
print(result)


# for text in output:
#     print(text)
# print(type(result))
# print(result)