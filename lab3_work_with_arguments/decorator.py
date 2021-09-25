def decorator (func):
    def new_kolve_chet(arr):
        original = func(arr)
        if not original:
            return('Нет(')
        elif original > 10:
            return('Очень много')
        else:
            return original
    return new_kolve_chet

@decorator
def kolve_chet (arr):
    k = 0
    for i in range (len(arr)):
        if arr[i]%2==0:
            k+=1
    return k
arr = [2, 4, 6, 8, 10, 12, 14, 16, 0, 20, 18, 90, 80, 50]
print(kolve_chet (arr))
arr = [2, 4, 6, 1, 5, 3]
print(kolve_chet (arr))
arr = [3, 9, 5]
print(kolve_chet (arr))