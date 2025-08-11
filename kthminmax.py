def kth_min_max(arr, k):
    # Remove duplicates if required:
    # arr = list(set(arr))

    arr_sorted = sorted(arr)  # ascending order

    kth_min = arr_sorted[k-1]          # k-th smallest
    kth_max = arr_sorted[-k]           # k-th largest

    return kth_min, kth_max


# Example
arr = [12, 3, 5, 7, 19, 4]
k = 2
kth_min, kth_max = kth_min_max(arr, k)
print(f"{k}th smallest element is {kth_min}")
print(f"{k}th largest element is {kth_max}")
