
// Subarray with 0 sum
// Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.
// Input:
//5
//4 2 -3 1 6

// Output: 
//Yes

//Explanation: 
//2, -3, 1 is the subarray 
//with sum 0.


class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        ##Your code here
        #Return true or false
        sum_ = 0
        s = set() 
        for i in arr:
            sum_ += i 
            if sum_ == 0 or sum_ in s:
                return True
            s.add(sum_)
        return False
    
