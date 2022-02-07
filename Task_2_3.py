lst = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
for elements in lst:
    splitting_up = elements.split()
    elements_reversed = splitting_up[::-1]
    del elements_reversed[1:]
    ending_word = ' '.join(elements_reversed).capitalize().split()
    for letter in ending_word:
        ending_words = 'Привет, ' + letter + '!'
        print(ending_words)