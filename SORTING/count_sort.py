def countingSort(arr):
    # Write your code here
    max_ = max(arr)
    # finding the maximum integer sothat we could create a count array of that maximum number
    count_array = [0] * (max_+1)
    # max_+1 means if max of an array will be 8 then we create a 0 array of index range 8 and len of 9
    # so max_ + 1 needed.
    for i in range(len(arr)):
        value = arr[i]
        count_array[value] += 1
    # assigning each value of count array accroding to the index which are the values of the main unsorted
    # array and for every occurance we increase the value of count array to +1
    sorted_array = []
    # final sorted array
    for i in range(len(count_array)):
        if count_array[i] > 0:
            # if the value is 0 in count array then the index of that 0 is not present as value in the 
            # main unsorted array, but if this value is more than 0 then it is present and we are gonna 
            # print that index associated with the non-0 value. Thus we get a sorted array.
            sorted_array += ([i] * count_array[i])
    # at last return the sorted array
    return sorted_array



a = [1, 8, 4, 6, 4, 10, 52, 47, 89, 4, 5, 3]
print(countingSort(a))