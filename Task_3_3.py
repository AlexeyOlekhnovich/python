def thesaurus(*names):
    resault = {}
    for name in names:
        key = name[0].capitalize()
        if key not in resault:
            resault[key] = []
        resault[key].append(name)
    return resault

print(thesaurus("Иван", "Мария", "Петр", "Илья", "Евгений", "Есения", "Василий", "Василиса", "Марина"))