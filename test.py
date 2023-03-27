# def isSubset( a1, a2, n, m):
#     temp = []
#     for i in range(len(a2)):
#         if a2[i] in a1:
#             if a2.count(a2[i]) > a1.count(a2[i]):
#                 return "No"
#             temp.append(a2[i])
#     print(temp)
#     if temp == a2:
#         return "Yes"
#     else:
#         return "No"
    
# a1 = [8, 4, 5, 3, 1, 7, 9]
# a2 = [5, 1, 3, 7, 9]
# print(isSubset(a1, a2, len(a1), len(a2)))


class Solution:
    def longestCommonPrefix(self, arr, n):
        frst_str = arr[0][0]
        i = 1
        while i < n:
            if arr[i][0] != frst_str:
                return -1
            else:
                i += 1
        minimal_str = min(arr)
        print(minimal_str)
        j = 1
        i = 0
        common_prefix = ''
        while j <= len(minimal_str):
            print("here1")
            common_prefix = minimal_str[:j]
            print(common_prefix)
            while i < n:
                print("here2")
                if common_prefix not in arr[i]:
                    print('here3', common_prefix[:j-1])
                    return common_prefix[:j-1]
                i += 1
            i = 0
            j += 1
        return common_prefix
            
        
    

arr = ['d', 'd', 'd', 'd']
sol = Solution()
print(sol.longestCommonPrefix(arr, len(arr)))