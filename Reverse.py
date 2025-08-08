# Using slicing
arr = [1, 2, 3, 4, 5]
reversed_arr = arr[::-1]
print(reversed_arr)  # [5, 4, 3, 2, 1]

#using reverse() (in-place)
arr = [1, 2, 3, 4, 5]
arr.reverse()
print(arr)  # [5, 4, 3, 2, 1]

#working with a NumPy array
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
reversed_arr = arr[::-1]
print(reversed_arr)  # [5 4 3 2 1]

#reverse an array manually in Python without using reverse() or reversed():
#1. Swapping elements in place
arr = [1, 2, 3, 4, 5]
n = len(arr)

for i in range(n // 2):
    # Swap first and last elements, moving inward
    arr[i], arr[n - i - 1] = arr[n - i - 1], arr[i]

print(arr)  # [5, 4, 3, 2, 1]

#2. Building a new reversed list
arr = [1, 2, 3, 4, 5]
reversed_arr = []

for i in range(len(arr) - 1, -1, -1):
    reversed_arr.append(arr[i])

print(reversed_arr)  # [5, 4, 3, 2, 1]
