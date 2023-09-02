def multiply_number(x):
    return x * 3

original_list = [17, 29, 36, 45, 59,76, 87]
multiplied_list = list(map(multiply_number, original_list))
print("Triple of list numbers:")
print(multiplied_list)
