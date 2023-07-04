class Solution:
    
    def partition(self,arr,low,high):
        # code here
        pivot = arr[high]
        pindex = low
        for i in range(low, high):
            if arr[i] < pivot: # checking if the element is greater than pivot
                arr[i], arr[pindex] = arr[pindex], arr[i]
                pindex += 1
        arr[high], arr[pindex] = arr[pindex], arr[high]
        return pindex
        
    def quickSort(self,arr,low,high):
        # the algo runs untill l is less than high
        if low<high:
            p = self.partition(arr, low, high)
            # recursion occurs in the left sub array
            self.quickSort(arr, low, p-1)
            # recursion occurs in the right subarray
            self.quickSort(arr, p+1, high)


sol = Solution()
arr = [4,5,6,8,2,3]
low = 0
high = len(arr) - 1
sol.quickSort(arr, low, high)
print(arr)