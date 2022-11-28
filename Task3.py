x = float(input('Введите х: '))
y = float(input('Введите y: '))

if x > 0 and y > 0:
    print('(x;y) ∈ первой четверти')
elif x < 0 and y > 0:
    print('(x;y) ∈ второй четверти')
elif x < 0 and y < 0:
    print('(x;y) ∈ третьей четверти')
elif x == 0 and y == 0:
    print('(x;y) - начало координат')
else :
    print('(x;y) ∈ четвертой четверти')