def InsertionSort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        while j >= 0 and key < arr[j]: # so in it checks that if key is less than the current 
            # element or not. if less then change the position or shift the position of the next element
            # of the j th element to the positon of the j th element
            arr[j+1] = arr[j]
            # decrement the pointer to change the other front element positions accrodingly
            j -= 1
            print(arr , " ," , j)
        arr[j+1] = key
arr = [12, 11, 13, 5, 6]
InsertionSort(arr)
print(arr)