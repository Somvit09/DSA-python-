# class Solution:
#     def commonElements (self,A, B, C, n1, n2, n3):
#         # your code here
#         final_list = []
#         for i in A:
#             for j in B:
#                 for k in C:
#                     if i==j and j == k and k == i:
#                         final_list.append(i)
#         return sorted(list(set(final_list)))

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        arr = []
        i, j, k = 0, 0, 0
        while i < n1 and j < n2 and k < n3:
            if A[i] == B[j] and B[j] == C[k] and C[k] == A[i]:
                arr.append(A[i])
                i += 1
                j += 1
                k += 1
            elif A[i] < B[j]:
                i += 1
            elif B[j] < C[k]:
                j += 1
            else:
                k += 1
        return sorted(list(set(arr)))


a = [1, 5, 10, 20, 40, 80]
b = [1, 5, 10, 20, 40, 80]
c = [3, 4, 15, 20, 30, 70, 80, 120]
sol = Solution()
print(sol.commonElements(a, b, c, len(a), len(b), len(c)))
