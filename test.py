from bigO import BigO
from random import randint

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


# class Solution:
#     def longestCommonPrefix(self, arr, n):
#         frst_str = arr[0][0]
#         i = 1
#         while i < n:
#             if arr[i][0] != frst_str:
#                 return -1
#             else:
#                 i += 1
#         minimal_str = min(arr)
#         print(minimal_str)
#         j = 1
#         i = 0
#         common_prefix = ''
#         while j <= len(minimal_str):
#             print("here1")
#             common_prefix = minimal_str[:j]
#             print(common_prefix)
#             while i < n:
#                 print("here2")
#                 if common_prefix not in arr[i]:
#                     print('here3', common_prefix[:j-1])
#                     return common_prefix[:j-1]
#                 i += 1
#             i = 0
#             j += 1
#         return common_prefix
            
        
    

# arr = ['d', 'd', 'd', 'd']
# sol = Solution()
# print(sol.longestCommonPrefix(arr, len(arr)))


# class Solution:
#     def productExceptSelf(self, nums, n):
#         temp = []
#         for i in range(n):
#             index = i
            
#             if index == 0:
#                 arr = nums[index+1:]
#                 value = 1
#                 for i in arr:
#                     value *= i
#                 temp.append(value)
#                 print(temp)
#             elif index == len(nums)-1:
#                 value = 1
#                 arr = nums[:len(nums)-1]
#                 for i in arr:
#                     value *= i
#                 temp.append(value)
#                 print(temp)
#                 return temp
#             else:
#                 left_array = nums[:index]
#                 right_array = nums[index+1:]
#                 print(left_array, right_array)
#                 value = 1
#                 for i in left_array:
#                     value *= i
#                 print(value)
#                 for i in right_array:
#                     value *= i
#                 print(value)
#                 print(index, ", ", value)
#                 temp.append(value)
#                 print(temp)
        
            

# nums = [7, 8, 6, 4, 6, 7, 3, 10, 2, 3, 8, 1, 10, 4, 7, 1, 7, 3, 7, 2, 9, 8, 10, 3, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1]
# sol = Solution()
# print(sol.productExceptSelf(nums, len(nums)))


# class Solution:
#     def rearrange(self,arr, n):
#         pos, neg = [], []
#         for i in arr:
#             if i >= 0:
#                 pos.append(i)
#             else:
#                 neg.append(i)

#         i, j = 0, 0
#         temp = []
#         while i < len(pos) or j < len(neg):
#             if len(pos) == 0:
#                 temp = neg
#             if len(pos) == 1:
#                 temp.append(pos[i])
#                 temp.extend(neg)
#             if len(pos) > 1:
#                 temp.append(pos[i])
#                 i += 1
#                 if j < len(neg):
#                     temp.append(neg[j])
#                     j += 1
#         arr = temp
#         return arr

            
                
    
# # arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]
# # n = len(arr)
# # sol = Solution()
# # print(sol.rearrange(arr, n))

# if __name__ == '__main__':
# 	tc = int(input())
# 	while tc > 0:
# 		n = int(input())
# 		arr = list(map(int, input().strip().split()))
# 		ob = Solution()
# 		ob.rearrange(arr, n)
# 		for x in arr:
# 			print(x, end=" ")
# 		print()
# 		tc -= 1

# class Solution:
#     # A1[] : the input array-1
#     # N : size of the array A1[]
#     # A2[] : the input array-2
#     # M : size of the array A2[]
    
#     #Function to sort an array according to the other array.
#     def partition(self, arr, l, h):
#         pivot = arr[h]
#         j = l
#         for i in range(l, h):
#             if arr[i] < pivot:
#                 arr[i], arr[j] = arr[j], arr[i]
#                 j += 1
#         arr[j], arr[h] = arr[h], arr[j]
#         return j
#     def quicksort(self, arr, l, h):
#         if l < h:
#             pi = self.partition(arr, l, h)
#             self.quicksort(arr, l, pi-1)
#             self.quicksort(arr, pi+1, h)
#     def relativeSort (self,A1, N, A2, M):
#         # Your Code Here
#         temp = []
#         temp1 = []
#         for i in A2:
#             if i in A1:
#                 count_i = A1.count(i)
#                 if count_i == 1:
#                     temp.append(i)
#                 else:
#                     for j in range(count_i):
#                         temp.append(i)
#         for i in A1:
#             if i not in temp:
#                 temp1.append(i)
#         self.quicksort(temp1, 0, len(temp1)-1)
#         temp.extend(temp1)
#         return temp


# A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
# A2 = [99, 22, 444, 56]
# N = len(A1) 
# M = len(A2)
# sol = Solution()
# print(sol.relativeSort(A1, N, A2, M))

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class ll:
#     def __init__(self):
#         self.head = None

#     def insert(self, data):
#         if self.head is None:
#             self.head = Node(data)
#         else:
#             n = self.head
#             while n.next is not None:
#                 n = n.next
#             n.next = Node(data)
#     def printll(self):
#         n = self.head
#         while n:
#             print(n.data)
#             n = n.next
            

# s = ll()
# s.insert(1)
# s.insert(2)
# s.insert(3)
# s.insert(4)
# s.insert(5)
# s.printll()

# class Solution:
#     #Function to sort the given linked list using Merge Sort.
#     def margesort(self, arr):
#         if len(arr) > 1:
#             mid = len(arr) // 2
#             l = arr[:mid]
#             r = arr[mid:]
#             self.margesort(l)
#             self.margesort(r)
#             i = j = k = 0
#             while i < len(l) and j < len(r):
#                 if l[i] < r[j]:
#                     arr[k] = l[i]
#                     i += 1
#                 else:
#                     arr[k] = r[j]
#                     j += 1
#                 k += 1
#             while i < len(l):
#                 arr[k] = l[i]
#                 i += 1
#                 k += 1
#             while j < len(r):
#                 arr[k] = r[j]
#                 j += 1
#                 k += 1
            

#     def mergeSort(self, head):
#         temp = []
#         if head is not None:
#             n = head
#             while n:
#                 temp.append(n.data)
#                 n = n.next

#         self.margesort(temp)
        
        


# a = Solution()
# print(a.apped_nodes_to_list(s.head))

# class Solution:
    
#     def mergeSort(self, arr):
#         if len(arr)>1:
#             mid = len(arr) // 2
#             l = arr[:mid]
#             r = arr[mid:]
#             self.mergeSort(l)
#             self.mergeSort(r)
#             i = j = k = 0
#             while i < len(l) and j < len(r):
#                 if l[i] < r[j]:
#                     arr[k] = l[i]
#                     i += 1
#                 else:
#                     arr[k] = r[j]
#                     j += 1
#                 k += 1
#             while i <  len(l):
#                 arr[k] = l[i]
#                 i += 1
#                 k += 1
#             while j < len(r):
#                 arr[k] = r[j]
#                 j += 1
#                 k += 1
            

#     #Function to merge the arrays.
#     def merge(self,arr1,arr2,n,m):
#         #code here
#         arr1.extend(arr2)
#         print(arr1)
#         self.mergeSort(arr1)
#         print(arr1)
#         arr = arr1[:n]
#         arr2 = arr1[n:]
#         return arr, arr2
    
# arr1 = [1, 3, 5, 7] 
# arr2 = [0, 2, 6, 8, 9]
# sol = Solution()
# print(sol.merge(arr1, arr2, len(arr1), len(arr2)))


# def printFirstNegativeInteger( A, N, K):
#     # code here
#     i, j = 0, 0
#     f = []
#     neg_int_arr = []
#     while i+j < N:
#         for j in range(K):
#             f.append(A[j+i])
#         print(f)
#         for k in range(len(f)):
#             if f[k] < 0:
#                 neg_int_arr.append(f[k])
#                 break
#             elif f[k] < 0 and f[k] == f[len(f)-1] and k == len(f)-1:
#                 neg_int_arr.append(k)
#             elif f[k] >= 0 and f[k] == f[len(f)-1] and k == len(f)-1:
#                 neg_int_arr.append(0)
#         i += 1
#         print(neg_int_arr)
#         f = []
#     return neg_int_arr

# arr = [-458, -598, -79, 544, 4, 954, 954, 4]
# n = len(arr)
# k = 3
# lib = BigO()
#a,b = lib.test(printFirstNegativeInteger(arr, n, k), array="random", limit=True, prtResult=True)

        

# def findCountsOfAverage(arr):
#     average = sum(arr) / len(arr)
#     return arr.count(average)

# arr = [1, 3, 2, 4, 5]
# print(findCountsOfAverage(arr))

# import operator

# def send_email_function(email):
#     import smtplib

#     # Here are the email package modules we'll need.
#     from email.message import EmailMessage

#     # Create the container email message.
#     msg = EmailMessage()
#     msg['Subject'] = 'Our family reunion'
#     # me == the sender's email address
#     # family = the list of all recipients' email addresses
#     msg['From'] = 'senderemail@gmail.com'
#     msg['To'] = email

#     # Send the message via our own SMTP server.
#     s = smtplib.SMTP('localhost')
#     s.send_message(msg)
#     s.quit()

# def send_emails(emails):
#     domain_dict = {}
#     for email in emails:
#         domain = email.split('@')[1]
#         if domain not in domain_dict:
#             domain_dict[domain] = []
#         domain_dict[domain].append(email)
#     sorted_domains = sorted(domain_dict.items(), key=operator.itemgetter(0))
#     for domain, emails in sorted_domains:
#         sorted_emails = sorted(emails)
#         send_email_function(sorted_emails[0])

# # Example usage
# emails = ['ghi@hotmail.com', 'def@yahoo.com', 'ghi@gmail.com', 'abc@channelier.com', 'abc@hotmail.com', 'def@hotmail.com', 'abc@gmail.com', 'abc@yahoo.com', 'def@channelier.com','jkl@hotmail.com', 'ghi@yahoo.com', 'def@gmail.com']
# send_emails(emails)









