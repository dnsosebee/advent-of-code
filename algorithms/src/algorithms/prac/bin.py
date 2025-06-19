
def binary_search(arr, x):
    lo, hi = 0, len(arr) - 1

    while lo <= hi:
        mid = (lo + hi) // 2
        if x < arr[mid]:
            hi = mid -1
        elif x > arr[mid]:
            lo = mid + 1
        else:
            return mid
    return -1
  
print(binary_search([1,2,3,4,5], 50))
