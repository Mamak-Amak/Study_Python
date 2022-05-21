duration = int(input('Введите положительное число = '))

if duration < 60:

    print(1 * duration, 'сек')
elif duration == 60 or duration < 3600:
    print(duration // 60, 'мин', duration % 60, 'сек')
elif duration == 3600 or duration < 86400:
    print(duration // 3600, 'час', (duration // 60) % 60, 'мин', duration % 60, 'сек')
else:
    if duration >= 86400:
        print(duration // 86400, 'день', (duration % 86400) // 3600, 'час', (duration // 3600) % 60, 'мин', duration % 60, 'сек')

#s = 1
#m = 60
#h = 3600
#d = 86400




