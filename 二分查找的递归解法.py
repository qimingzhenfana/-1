def bSearch(arr, low, high, key):
    if low > high:
        return -1
    mid = low + ((low + high)) >> 1
    midVal = arr[mid]
    if midVal < key:
        return bSearch(arr, mid + 1, high, key)
    elif midVal > key:
        return bSearch(arr, low, mid - 1, key)
    else:
        return mid


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
low = 0
high = len(arr) - 1
print("请输入要查询的数：")
N = int(input())
i = bSearch(arr, low, high, N)
if i == -1:
    print("没有找到！")
else:
    print("可以找到！")
