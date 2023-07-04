def BinarySearch(arr, key):
    l = 0 # setting the l pointer
    r = len(arr)-1 # setting the r pointer
    while l <= r:
        mid = l + r//2 # mid 
        if arr[l] == key: # if the target element is the present element(arr[l]) then we found the key
            return f"{key} is present."
        elif arr[l] < key: # if the target element is greater than present element(arr[l]) then search in the right subarray
            l = mid + 1
        else:
            l = mid - 1 # if the target element is less than present element(arr[l]) then search in the left sub array
    return f"{key} is not present."