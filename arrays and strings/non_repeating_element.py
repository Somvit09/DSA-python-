# User function Template for python3
from collections import defaultdict

class Solution:
    def firstNonRepeating(self, arr, n):
        # Complete the function
        mp = defaultdict(lambda: 0)

        for i in range(n):
            mp[arr[i]] += 1

        for i in range(n):
            if mp[arr[i]] == 1:
                return arr[i]

        return -1


# {
#  Driver Code Starts
# Initial Template for Python 3

from collections import defaultdict

for _ in range(0, int(input())):
    n = int(input())
    arr = list(map(int, input().strip().split()))
    ob = Solution()
    print(ob.firstNonRepeating(arr, n))

# } Driver Code Ends