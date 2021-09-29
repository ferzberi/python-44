x = input('Введите число от 0 до бесконечности:\n')
array = []

for elem in x: 
    array.append(int(elem))

print ('Сумма фицр введенного числа равна:', sum(array))
