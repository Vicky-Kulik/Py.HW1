x = float(input('Введите х: '))
y = float(input('Введите y: '))

distance = float(x**2+y**2)**0.5
distance = round(distance, 2)

print(f'Расстояние между точками: {distance}')