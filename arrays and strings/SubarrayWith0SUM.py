
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
        sum_ = 0// initializing sum as 0
        s = set() // using set for duplicate values
        for i in arr:
            sum_ += i // storing variables by adding them
            if sum_ == 0 or sum_ in s: // if there is a 0 or at a point a duplicate variable arrived in sum_ then retrun True
                return True
            s.add(sum_)// else just add it in s set
        return False