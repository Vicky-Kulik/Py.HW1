NumQuarter = int(input('Введите номер координатной четверти: '))
if NumQuarter == 1:
    print('(x>0, y>0')
elif NumQuarter == 2:
    print('(x<0, y>0)')
elif NumQuarter == 3:
    print('(x<0, y<0)')
elif NumQuarter == 4:
    print('(x>0, y<0)')
else:
    print('Ошибка. Введите целое число от 1 до 4')