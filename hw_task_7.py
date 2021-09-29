a = float(input('Введите размер вклада:\n'))
b = int(input('Введите срок вклада:\n'))

def bank(a,b):
    
    if b == 0:
        return a

    for i in range (1,b+1):
        a = a + (a*10/100)

    return a

print(bank(a,b))
