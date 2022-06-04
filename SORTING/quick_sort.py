class Solution:
    
    def partition(self,arr,low,high):
        # code here
        pivot = arr[high]
        pindex = low
        for i in range(low, high):
            if arr[i] < pivot:
                arr[i], arr[pindex] = arr[pindex], arr[i]
                pindex += 1
        arr[high], arr[pindex] = arr[pindex], arr[high]
        return pindex
        
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        # code here
        if low<high:
            p = self.partition(arr, low, high)
            self.quickSort(arr, low, p-1)
            self.quickSort(arr, p+1, high)


sol = Solution()
arr = [4,5,6,8,2,3]
low = 0
high = len(arr) - 1
sol.quickSort(arr, low, high)