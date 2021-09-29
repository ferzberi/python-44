x = input('Введите аругмент x: \n')
y = input('Введите аргумент y: \n')

a = ''
b = ''

try: 
    a = float(x) 
    b = float(y)
    
except ValueError:
    print(x+y)

if a in range(3,21) and b in range(3,21):
    print(abs(a-b))
