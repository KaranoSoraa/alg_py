# Решение задачи по сортировке массива методом двух указателей. 
n = int(input("Введите размер массива: "))
k = int(input("Введите число К: "))
uk = 0
arr, res = [], []

for i in range(n):
    num = int(input("Введите элемент массива: "))
    arr.append(num)
    while uk + 1 <= i and arr[uk + 1] + k <= num:
        uk += 1
    if arr[uk] + k <= num:
        res.append(arr[uk])
    else:
        res.append(-1)

for j in res:
    print(j, end=' ')
