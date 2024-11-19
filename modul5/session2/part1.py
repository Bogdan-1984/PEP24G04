print(chr(97))
print(ord('a'))
print(bin(ord('a')))
print(bin(10))
# 0b1100001 &
# 0b0001011
# 0b0000001

# 0b1100001 |
# 0b0001011
# 0b1101011

# 0b1100001 ^
# 0b0001011
# 0b1101010 ^
# 0b0001011
# 0b1100001
print(chr(ord('a') ^ 133))
print(chr(ord('ä') ^ 133))