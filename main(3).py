c = []
for i in range(4):
    a = int(input('Ведите число: '))
    c.append(a)

r = 0
for i in range(4):
    i = i + 1
    if i%2==0:
        i = i - 1
        if c[i]%2==1:
            r = r + c[i]

print('Сумма нечетных чисел в четных индексах: ',r)
    
