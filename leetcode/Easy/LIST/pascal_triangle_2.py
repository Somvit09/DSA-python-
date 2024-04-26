from typing import List

class Solution:
    def __init__(self):
        self.arr = [[1],[1,1],[1,2,1]]

    def getRow(self, rowIndex: int) -> List[int]:
        n = 3
        if rowIndex < n:
            return self.arr[rowIndex]
        while n <= rowIndex:
            temp = [1]
            i = 0
            j = i+1
            for _ in range(n - 1):
                temp.append(self.arr[-1][i] + self.arr[-1][j])
                i += 1
                j += 1
            temp.append(1)
            self.arr.append(temp)
            if n == rowIndex:
                return self.arr[rowIndex]
            n += 1



obj = Solution()
print(obj.getRow(4))