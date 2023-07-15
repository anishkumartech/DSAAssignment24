def find_closest_elements(arr, k, x):
    left = 0
    right = len(arr) - 1

    while right - left + 1 > k:
        if abs(arr[left] - x) > abs(arr[right] - x):
            left += 1
        else:
            right -= 1

    return arr[left:right+1]

# Example usage
arr = [1, 2, 3, 4, 5]
k = 4
x = 3
print(find_closest_elements(arr, k, x))

arr = [1, 2, 3, 4, 5]
k = 4
x = -1
print(find_closest_elements(arr, k, x))
