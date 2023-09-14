user_str = input("Enter a list of integers separated by commas: ")

input_list = [int(num) for num in user_str.split(',')]
tripled_list = list(map(lambda x: x * 3, input_list))

print("Triple of list numbers:")
print(tripled_list)
