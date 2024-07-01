# Тут будет реализована сортировка выбором. Не знаю, зачем мне эта древность, но пусть будет.

def sort_1(arr):
    mi = None
    res = []
    ans = [0 for i in range(len(arr))]
    for i in range(len(arr)):
        fl = False
        num = 0
        for j in range(len(arr)):
            if not ans[j] and (not fl or mi > arr[j]):
                mi = arr[j]
                num = j
                fl = True
        ans[num] = 1
        res.append(mi)
    return res



mass = [2, 3, 1, 4, 2, 4]
mass2 = [5, 12, 3, 1, 0, 6]
res = sort_1(mass)
print(res)