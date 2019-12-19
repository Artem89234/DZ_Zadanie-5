c = []
b = 0
for i in range(10):
    a = int(input('Введите число: '))
    c.append(a)

for i in range(5):
    i = i + 1
    if c[i]%2==1:
        i = i - 1
        b = b + c[i]
print('Сумма нечетных чисел в четных индексах: ',b)
    
