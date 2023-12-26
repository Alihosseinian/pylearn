def remove_duplicates(input_list):
    unique_list = list(set(input_list))
    return unique_list

input_list = [2, 3, 6, 7, 7, 14, 2, 7]

result = remove_duplicates(input_list)
print(result)
