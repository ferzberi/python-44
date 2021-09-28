x = input('Введите аругмент x: \n')
y = input('Введите аргумент y: \n')
z = input('Укажите знак математической операции: \n')

a = ''
b = ''

try: 
    a = float(x) 
    b = float(y)
      
except ValueError:
    print(x+y)

if a in range(3,23) and b in range(3,23):
    if z == '+':
        print(a+b)
    elif z == '-':
        print(a-b)
    elif z == '*':
        print(a*b)
    elif z == '/':
        print(a/b)          
    else:
        print('Ошибка! Проверьте корректность ввода')

