def reverse_string(s):
    if len(s) == 0:
        return s
    else:
        return reverse_string(s[1:]) + s[0]

sample_string = "1716Phantom"
reversed_string = reverse_string(sample_string)
print(reversed_string)
