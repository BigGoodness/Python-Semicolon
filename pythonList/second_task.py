def even_numbers(new_list):
    even_list = []
    for number in new_list:
        if number % 2 == 0:
            even_list.append(number)
    return even_list


new_list = [1,2,3,4,5,6,7,8,9,10]
print(even_numbers(new_list))
