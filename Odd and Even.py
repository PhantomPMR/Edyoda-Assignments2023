numbers = (11,22, 33, 44, 55, 66, 77, 88, 99)

even_numbers = 0
odd_numbers = 0

for num in numbers:
    if num % 2 == 0:
        even_numbers += 1
    else:
        odd_numbers += 1

print("Number of even numbers:", even_numbers)
print("Number of odd numbers:", odd_numbers)
