summa_number_power_over = 0
start_list = 1
end_list = 1000
while start_list <= end_list:
    if start_list % 2:
        summa_number_power = 0
        number_to_the_power = start_list ** 3
        number_to_the_power_for_print = number_to_the_power;
        while number_to_the_power > 0:
            last_digit = number_to_the_power % 10
            number_to_the_power = number_to_the_power // 10
            summa_number_power += last_digit
        if summa_number_power % 7 == 0:
            summa_number_power_over += summa_number_power
            print(start_list, "^3: ", number_to_the_power_for_print, "sum:", summa_number_power_over, "[" ,summa_number_power, "]")
    start_list += 1