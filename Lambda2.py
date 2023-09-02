def add_98(x):
    return lambda x: x + 98

add = add_98(100)
result = add(100)
print(result)  
