# Слияние двух массивов методом двух указателей.
n = int(input("Введите длину первого массива: "))
m = int(input("Введите длину второго массива: "))
arr, res = [], []
uk = 0

for i in range(n):
    arr.append(int(input("Введите элемент первого массива: ")))

# Второй массив не вводим, сразу проводим слияние.
for uk2 in range(m):
    num = int(input("Введите элемент второго массива: "))
    while uk != len(arr) and arr[uk] <= num:
        res.append(arr[uk])
        uk += 1
    res.append(num)

while uk != len(arr):
    res.append(arr[uk])
    uk += 1

for j in res:
    print(j, end=' ')
