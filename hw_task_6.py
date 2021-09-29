x = input('Введите первое число:\n')
y = input('Введите второе число:\n')

def nod(x, y):
    while x != y:
        if x > y:
            x = x-y
        else:
            y = y-x
    return x

print(f'НОД чисел {x} и {y} равен', nod(8,10))
