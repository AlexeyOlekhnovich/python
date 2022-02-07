list_numbers = [57.8, 46.40, 12.3, 9, 67.54, 8.07, 982.12]
print(list_numbers)
transfer_to_list = ' '.join((map(str, list_numbers))).split()
number = 0
for elements in transfer_to_list:
    element = elements.split()
    for splitting_up in element:
        if "." in splitting_up:
            ruble, pennies = splitting_up.split(".")
            if len(pennies) == 1:
                pennies = pennies + str(number)
            print(ruble, "руб.", pennies, "коп.")
        else:
            print(splitting_up, "руб.", "00 коп.")
print("id перед сортировкой:", id(list_numbers))
list_numbers.sort()
print("id после сортировки:", id(list_numbers))
print(list_numbers)
lst_revers = sorted(list_numbers, reverse=True)
most_values = list_numbers[-1:-6:-1]
transfer_to_list = ' '.join((map(str, most_values))).split()
print("5 самых дорогих товаров")
for elements in transfer_to_list:
    element = elements.split()
    for splitting_up in element:
        if "." in splitting_up:
            ruble, pennies = splitting_up.split(".")
            if len(pennies) == 1:
                pennies = pennies + str(number)
            print(ruble, "руб.", pennies, "коп.")
        else:
            print(splitting_up, "руб.", "00 коп.")