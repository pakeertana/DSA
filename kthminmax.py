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

#
import heapq

def kth_min_max_heap(arr, k):
    # k-th smallest using nsmallest (O(n log k))
    kth_min = heapq.nsmallest(k, arr)[-1]
    
    # k-th largest using nlargest (O(n log k))
    kth_max = heapq.nlargest(k, arr)[-1]
    
    return kth_min, kth_max


# Example
arr = [12, 3, 5, 7, 19, 4]
k = 2
kth_min, kth_max = kth_min_max_heap(arr, k)
print(f"{k}th smallest element is {kth_min}")
print(f"{k}th largest element is {kth_max}")
