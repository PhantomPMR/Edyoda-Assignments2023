def sum_of_list(nums):
    if len(nums) == 0:
        return 0
    else:
        return nums[0] + sum_of_list(nums[1:])

sample_list = [8, 2, 3, 0, 7]
print(sum_of_list(sample_list))  
