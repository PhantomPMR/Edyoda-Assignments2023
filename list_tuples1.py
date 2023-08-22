def sort_tuples_by_last_element(tuples_list):
    n = len(tuples_list)
    
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if tuples_list[j][-1] < tuples_list[min_index][-1]:
                min_index = j
        tuples_list[i], tuples_list[min_index] = tuples_list[min_index], tuples_list[i]
    
    return tuples_list

sample_list = [(32, 45), (31, 42), (34, 44), (32, 43), (32, 41)]

sorted_list = sort_tuples_by_last_element(sample_list)

print(sorted_list)
