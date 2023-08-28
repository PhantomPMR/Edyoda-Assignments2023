def count_case_characters(s):
    upper_count = sum(1 for char in s if 'A' <= char <= 'Z')
    lower_count = sum(1 for char in s if 'a' <= char <= 'z')
    return upper_count, lower_count

sample_string = 'This Python Module is taught by Divya Mam'
upper_count, lower_count = count_case_characters(sample_string)
print("No. of Upper case characters:", upper_count)
print("No. of Lower case characters:", lower_count)
