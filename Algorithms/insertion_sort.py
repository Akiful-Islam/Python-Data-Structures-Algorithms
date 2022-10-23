def insertion_sort(arr):
    for i in range(1, len(arr)):
        index = i - 1
        value = arr[i]
        while (arr[index] > value) and (index >= 0):
            arr[index + 1] = arr[index]
            index -= 1
        arr[index + 1] = value
    return arr
        
arr = ['i', 'a', 'e', 'u', 'o']
print ("Sorted array is:", insertion_sort(arr))