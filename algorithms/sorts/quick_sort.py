def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)

arr = [3, 33, 10, 45 , 72, 86, 69, 24, 51, 99]
print("Sorted array is: ", quick_sort(arr))