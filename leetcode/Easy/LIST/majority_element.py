from typing import List


# 1st approach : not optimuzed for [1000000000,1000000000,-1000000000,-1000000000,-1000000000] these kind of list.
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_array = [0] * (max(nums) + 1)
        for i in nums:
            count_array[i] += 1
        max_majority_count = len(nums) / 2
        max_majority_element = 0
        for i in range(len(count_array)):
            if count_array[i] >= max_majority_count:
                if i >= max_majority_element:
                    max_majority_element = i
        return max_majority_element

# 2nd approach optimised for memory exceed error.   
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = None
        count = 0

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate

arr = [2,2,1,1,1,2,2]
obj = Solution()
print(obj.majorityElement(arr))