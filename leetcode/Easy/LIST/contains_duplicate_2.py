from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_indices = {}
        for i, num in enumerate(nums):
            if num in num_indices and i - num_indices[num] <= k:
                return True
            num_indices[num] = i
        return False
    

arr = [1,2,3,1,2,3]
k = 2
obj = Solution()
print(obj.containsNearbyDuplicate(arr, k))