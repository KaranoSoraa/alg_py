# Решение задачи о рюкзаке через рекурсию.

def rec(mask, ws, cs, num):
    global ma, mask_ma
    if WE < ws:
        return
    if cs > ma:
        ma = cs
        mask_ma = mask
    if num == n:
        return
    rec(mask + (1<<num), ws + we[num], cs + ci[num], num + 1)
    rec(mask, ws, cs, num + 1)
    
we, ci = [], []
ma, mask_ma = 0, 0
WE = int(input("Введите максимальный переносимый вес рюкзака: "))
n = int(input("Введите количество вещей: "))
text = "Введите вес предмета и его стоимость: "

for i in range(n):
    w, c = map(int, input(text).split())
    we.append(w), ci.append(c)

rec(0, 0, 0, 0)
print(ma)

for i in range(n):
    if mask_ma & 1:
        print(i + 1)
    mask_ma >>= 1

