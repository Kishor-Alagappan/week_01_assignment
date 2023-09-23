def find_greatest(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]
    return arr[-1]

my_list = [64,134,25,12,22,11,90,22]
print(find_greatest(my_list))