upper_limit = int(input("Enter the upper limit for the Fibonacci series: "))
a = 0
b = 1

print(a, b, end=" ")

while a + b <= upper_limit:
    c = a + b
    a = b
    b = c
    print(c, end=" ")
    
