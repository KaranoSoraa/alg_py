mas = []
for i in range(1, 1001):
    mas.append(i)

start, last = 0, len(mas)
sic = float(input("Введите искомое число: "))
num = 0
while last >= start:
    mid = (start + last) // 2
    print(f"Мид {mid}")
    if mid == sic:
        print(f"Наш результат: {mid}")
        print(num + 1)
        exit()
    if mas[mid] < sic:
        start = mid + 1
        num += 1
    elif mas[mid] > sic:
        last = mid - 1
        num += 1
    else:
        print(f"Наш результат {mid}")
        num += 1
        print(num)
        exit()
print(f"Наш результат a {start}")
print(num)
