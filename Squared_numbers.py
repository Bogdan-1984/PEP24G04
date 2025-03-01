nums = [1,2,3,4,5]

# V1.
squared_nums = [num ** 2 for num in nums]

# V2.
# squared_nums = []
# for num in nums:
#     squared_nums.append(num ** 2)

# V3.
# squared_nums = list(map(lambda x: x ** 2, nums))

print(squared_nums)