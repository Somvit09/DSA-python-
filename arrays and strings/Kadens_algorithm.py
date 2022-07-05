#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        mf = 0 // storing altotal sum from the list
        me = 0 //storing the sum of ith variable
        temp = [] //initializing an empty array
        for i in arr: // checking if the array only contains negative number .only that case we return the maximum variable of the list
            if i<0:
                temp.append(i)
        if len(temp) == N:// checking the length of the temp array with arr
            return max(arr)
        for i in arr:
            me += i //storing the ith addition
            me = max(i, me) //checking the max value between o and me
            mf = max(mf, me) //same as upward with 0 and mf
        return mf //returning the maximum subtotal mf

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends