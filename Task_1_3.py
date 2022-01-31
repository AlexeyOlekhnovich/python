second_element_of_end = 0
start_list = 1
end_list = 150
while start_list <= end_list:
    second_element_of_end = start_list % 100 // 10
    if second_element_of_end == 1:
        print(start_list, "процентов")
    elif start_list % 10 == 1:
        print(start_list, "процент")
    elif start_list % 10 == 2 or start_list % 10 == 3 or start_list % 10 == 4:
        print(start_list, "процента")
    else:
        print(start_list, "процентов")
    start_list += 1