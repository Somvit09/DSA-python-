#User function Template for python3
//Factorials of large numbers
//[Given an integer N, find its factorial.

Example 1:

Input: N = 5
Output: 120
Explanation : 5! = 1*2*3*4*5 = 120
Example 2:

Input: N = 10
Output: 3628800
Explanation :
10! = 1*2*3*4*5*6*7*8*9*10 = 3628800]


class Solution:
    def factorial(self, N):
        #code here
        temp = []
        for i in range(1,N):
            N *= i
        m = str(N)
        for i in m:
            temp.append(int(i))
        return temp

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.factorial(N);
        for i in ans:
            print(i,end="")
        print()
    
# } Driver Code Ends