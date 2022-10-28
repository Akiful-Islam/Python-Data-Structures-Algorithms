def selection_sort(list):
    for i in range(len(list)):
        min_idx = i
        for j in range(i+1, len(list)):
            if list[min_idx] > list[j]:
                min_idx = j
        list[i], list[min_idx] = list[min_idx], list[i]
    return list

list = [67, 23, 45, 89, 12, 34, 1, 56, 11, 22, 78, 0, 33, 44, 55, 66, 77, 88, 99]
print("Sorted array is:", selection_sort(list))