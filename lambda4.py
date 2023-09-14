def add_n(n):
    return lambda x: x + n
add_25 = add_n(25)
num = float(input("Enter a number: "))
result = add_25(num)
print(f"Result: {result}")
