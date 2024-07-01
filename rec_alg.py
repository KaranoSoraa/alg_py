# Задача с башнями. Решение рекурсией.
def rec(n, fr, to):
    temp = fr ^ t
    if n == 1:
        print(f"{fr} -> {to}")
        return
    rec(n - 1, fr, temp)
    rec(1, fr, to)
    rec(n - 1, temp, to)

col = int(input("Введите количество колец: "))
rec(col, 1, 3)