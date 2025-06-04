def count_sort(arr):
    if not arr:
        return []
    
    min_val = min(arr)
    max_val = max(arr)
    range_size = max_val - min_val + 1
    
    count = [0] * range_size
    for num in arr:
        count[num - min_val] += 1
    
    for i in range(1, range_size):
        count[i] += count[i-1]
    
    sorted_arr = [0] * len(arr)
    for num in reversed(arr):
        pos = count[num - min_val] - 1
        sorted_arr[pos] = num
        count[num - min_val] -= 1
    
    return sorted_arr

print(count_sort([5, 1, 2, 4, 3])) 