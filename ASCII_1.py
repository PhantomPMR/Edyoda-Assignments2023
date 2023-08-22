ascii_dict = {}

for char in range(ord('A'), ord('Z') + 1):
    ascii_dict[chr(char)] = char

print(ascii_dict)
