symbols = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
number_element = 0
final_text = ''
for elements in symbols:
    if elements[0] in '+-':
        a = elements[0]
        while number_element < len(symbols):
            if symbols[number_element].isdigit() or symbols[number_element][1:].isdigit():
                if symbols[number_element].isdigit():
                    symbols[number_element] = symbols[number_element].zfill(2)
                elif symbols[number_element][1:].isdigit():
                    symbols[number_element] = a + symbols[number_element][1:].zfill(2)
                symbols.insert(number_element, '"')
                symbols.insert(number_element + 2, '"')
                number_element += 2
            number_element += 1
for elements in symbols:
    if elements[0] in '"':
        final_text += elements
    else:
        final_text += elements
        final_text += ' '
print(final_text)
