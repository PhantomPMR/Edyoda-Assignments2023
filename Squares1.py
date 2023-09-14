def square_number(x):
    return x * x
input_str = input("Enter a list of integers separated by commas: ")
input_list = [int(num) for num in input_str.split(',')]

squared_list = list(map(square_number, input_list))

print("Square the elements of the list:")
print(squared_list)
