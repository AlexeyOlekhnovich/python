duration = input("Введите продолжительность (в секундах): ")
seconds = int(duration)
minutes = seconds // 60
hours = minutes // 60
days = hours // 24

if (seconds >= 60):
    seconds = seconds % 60
    if (minutes != 0):
        minutes = minutes % 60
        if (hours != 0):
            hours = hours % 24
            if (days != 0):
                print(days, "дн", hours, "час", minutes, "мин", seconds, "сек")
            else:
                print("До суток: ", hours, "час", minutes, "мин", seconds, "сек")
        else:
            print("До часа: ",  minutes, "мин", seconds, "сек")
else:
    print("До минуты: ", seconds, "сек")
