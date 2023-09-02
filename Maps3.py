def multiply_with_3(x):
    return x * 3

New_list = [100,200,300,400,500,600,700]
tripled_list = list(map(multiply_with_3, New_list))
print("Triple of list numbers:")
print(tripled_list)
