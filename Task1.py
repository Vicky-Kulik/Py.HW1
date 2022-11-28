DayNumber = int(input ('Введите число, обозначающее день недели: '))
if DayNumber > 0 and DayNumber <= 5:
    print('Будний день')
elif DayNumber == 6 or DayNumber == 7:
    print('Выходной день')
else:
    print('Ошибка. Введите целое число от 1 до 7')
