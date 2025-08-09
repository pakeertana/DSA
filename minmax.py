#using built-in 
arr = [10, 3, 45, 7, 2, 99, 23]
maximum = max(arr)
minimum = min(arr)
print("Maximum element:", maximum)
print("Minimum element:", minimum)

# Without using built-in functions
arr = [10, 3, 45, 7, 2, 99, 23]

# Assume first element is both min and max
maximum = minimum = arr[0]

for num in arr:
    if num > maximum:
        maximum = num
    elif num < minimum:
        minimum = num

print("Maximum element:", maximum)
print("Minimum element:", minimum)

#one-liner way using sorted()
arr = [10, 3, 45, 7, 2, 99, 23]

minimum, maximum = sorted(arr)[0], sorted(arr)[-1]

print("Maximum element:", maximum)
print("Minimum element:", minimum)
