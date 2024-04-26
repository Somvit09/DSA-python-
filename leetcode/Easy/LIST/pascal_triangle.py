from typing import List

class Solution:
    def __init__(self):
        self.arr = [[1],[1,1],[1,2,1]]

    def generate(self, numRows: int) -> List[List[int]]:
        n = 3
        if numRows <= n:
            return self.arr[:(numRows-1)+1]
        while n <= numRows:
            temp = [1]
            i = 0
            j = i+1
            for _ in range(n - 1):
                temp.append(self.arr[-1][i] + self.arr[-1][j])
                i += 1
                j += 1
            temp.append(1)
            self.arr.append(temp)
            n += 1
            if n == numRows:
                return self.arr
            
obj = Solution()
print(obj.generate(4))

        