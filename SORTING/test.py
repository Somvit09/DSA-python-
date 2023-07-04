class Sorting:

    def __init__(self, arr):
        self.arr = arr

    def Partition(self, arr, l, r):
        pivot = arr[r]
        pindex = l
        for i in range(l, r):
            if arr[i] < pivot:
                arr[i], arr[pindex] = arr[pindex], arr[i]
                pindex += 1
        arr[r], arr[pindex] = arr[pindex], arr[r]
        return pindex
    
    def Quicksort(self, arr, l, r):
        if l < r:
            pi = self.Partition(arr, l, r)
            self.Quicksort(arr, l, pi-1)
            self.Quicksort(arr, pi+1, r)
        
    def Mergesort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            ls = arr[:mid]
            rs = arr[mid:]
            self.Mergesort(ls)
            self.Mergesort(rs)
            i = j = k = 0
            while i < len(ls) and j < len(rs):
                if ls[i] < rs[j]:
                    arr[k] = ls[i]
                    i += 1
                else:
                    arr[k] = rs[j]
                    j += 1
                k += 1
            while i < len(ls):
                arr[k] = ls[i]
                i += 1
                k += 1
            while j < len(rs):
                arr[k] = rs[j]
                j += 1
                k += 1

    def InsertionSort(self, arr):
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key

    def BinarySearch(self, arr, key):
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
arr = [1, 8, 9, 4, 44, 1, 552, 2]
obj = Sorting(arr)
n = len(arr)
print(obj.BinarySearch(arr, 77))
print(arr)