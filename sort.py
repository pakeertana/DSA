#Given an array which consists of only 0, 1 and 2. Sort the array without using any sorting algo

def sort012(arr):
    count0 = arr.count(0)
    count1 = arr.count(1)
    count2 = arr.count(2)

    # Overwrite the array
    arr[:] = [0]*count0 + [1]*count1 + [2]*count2
    return arr

# Example
arr = [0, 2, 1, 2, 0, 1, 0]
sorted_arr = sort012(arr)
print(sorted_arr)

#If you want it in-place and single-pass without counting, you can use the Dutch National Flag algorithm:
def sort012(arr):
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr

# Example
arr = [0, 2, 1, 2, 0, 1, 0]
print(sort012(arr))
