def count_case_characters(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

sample_string = 'I am learning PYTHON from Edyoda'
upper_count, lower_count = count_case_characters(sample_string)
print("No. of Upper case characters:", upper_count)
print("No. of Lower case characters:", lower_count)
