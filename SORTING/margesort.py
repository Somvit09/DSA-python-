def Margesort(arr):
    if len(arr) > 1:
        # mid pointer 
        mid = len(arr) // 2
        # left subarray
        l = arr[:mid]
        # right subarray
        r = arr[mid:]
        # margesorting left subarray
        Margesort(l)
        # margesorting right subarray
        Margesort(r)
        i = j = k = 0
        # checking and comparing happened between the elements
        while i < len(l) and j < len(r):
            if l[i] <= r[j]: # checking the element of left array is less than the element of right array or not?
                arr[k] = l[i]
                i += 1
            else:
                arr[k] = r[j]
                j += 1
            k += 1
        # if any element has left in the left array
        while i < len(l):
            arr[k] = l[i]
            i += 1
            k += 1
        # if any element has left the right array
        while j < len(r):
            arr[k] = r[j]
            j += 1
            k += 1


arr = [12, 11, 13, 5, 6, 7]
Margesort(arr)
print(arr)