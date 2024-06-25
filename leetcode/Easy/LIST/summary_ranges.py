# from typing import List

# class Solution:
#     final_list = []
#     temp = []
#     temp_ = []

#     def update_final_list(self, temp):
#         for i in temp:
#             list(set(i)).sort()
#             if len(i) > 1:
#                 final_string = f"{i[0]}->{i[len(i)-1]}"
#                 self.final_list.append(final_string)
#             else:
#                 self.final_list.append(f"{i[0]}")
#         return self.final_list


#     def summaryRanges(self, nums: List[int]) -> List[str]:

#         n = len(nums)
#         for i in range(n):
#             if i+1 < n:
#                 if nums[i] + 1 == nums[i+1]:
#                     self.temp.extend([nums[i], nums[i+1]])
#                     print(self.temp)
#                 else:
#                     if nums[i] not in self.temp:
#                         self.temp = [nums[i]]
#                     print(self.temp)
#                     self.temp_.append(self.temp)
#                     self.temp = []
#             else:
#                 if nums[i] in self.temp:
#                     self.temp_.append(self.temp)
#                 else:
#                     self.temp_.append([nums[i]])
#         return self.update_final_list(self.temp_)
    
import time
from typing import List

class Solution:
    
    def update_final_list(self, ranges):
        final_list = []
        for r in ranges:
            if len(r) > 1:
                final_string = f"{r[0]}->{r[-1]}"
                final_list.append(final_string)
            else:
                final_list.append(f"{r[0]}")
        return final_list

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        ranges = []
        temp = [nums[0]]

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1] + 1:
                temp.append(nums[i])
            else:
                ranges.append(temp)
                temp = [nums[i]]
        
        ranges.append(temp)

        return self.update_final_list(ranges)


        
temp = [0,2,3,4,6,8,9]
s = Solution()
print(s.summaryRanges(temp))