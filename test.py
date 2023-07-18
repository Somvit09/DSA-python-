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


# def migratoryBirds(arr):
#     count = [0] * len(arr)  # Create an array to store the count of each bird type (from 1 to 5)
#     for bird in arr:
#         count[bird] += 1  # Count the occurrence of each bird type
    

#     max_count = max(count)  # Find the maximum count
#     min_bird = float('inf')  # Initialize the minimum bird type to infinity

#     for bird_type in range(1, 6):
#         if count[bird_type] == max_count and bird_type < min_bird:
#             min_bird = bird_type  # Update the minimum bird type if a smaller one is found

#     return min_bird


# arr = [1, 4, 4, 4, 5, 3]
# print(migratoryBirds(arr))


# def bonAppetit(bill, k, b):
#     # Write your code here
#     not_eaten = bill[k]
#     eaten_total_amount = 0
#     for i in  bill:
#         if i != bill[k]:
#             eaten_total_amount += i
#     each_eaten_amount = eaten_total_amount / 2
#     total_bill_each = sum(bill) / 2
#     if each_eaten_amount == b:
#         return "Bon Appetit"
#     else:
#         return total_bill_each - each_eaten_amount
    

# def sockMerchant(n, ar):
#     # Write your code here
#     data = {}
#     for i in ar:
#         data[i] = ar.count(i)
#     pair_count = 0
#     for keys, values in data.items():
#         if values % 2 != 0:
#             pair_count += ((values-1) // 2)
#         else:
#             pair_count += ((values) // 2)

#     print(pair_count)
        

# sockMerchant(7, [1,2,1,2,1,3,2])

# def pageCount(n, p):
#     # Write your code here
#     page_count = 0
#     data = {}
#     i = 1
#     while i < n+1:
#         if i == 1:
#             data[page_count] = [1]
#             page_count += 1
#             i += 1
#         elif i == n:
#             data[page_count] = [n]
#             break
#         else:
#             data[page_count] = [i, i + 1]
#             i += 2
#             page_count += 1
#     data_reverse_order = {}
#     for keys, values in data.items():
#         reversed_key = len(data)-1-keys
#         data_reverse_order[reversed_key] = values
#     print(data_reverse_order)
#     for  keys, values in data.items():
#         if p in values:
#             page = keys
#     for  keys, values in data_reverse_order.items():
#         if p in values:
#             page_reversed = keys
#     return min(page, page_reversed)

# print(pageCount(9, 3))


# def pickingNumbers(a):
#     # Write your code here
#     temp = []
#     t = []
#     i = 0
#     while i < len(a):
#         a.sort()
#         curr = a[i]
#         if curr + 1 in a:
#             t.append(curr)
#             for j in range(len(a)):
#                 if a[j] == curr and j != i:
#                     t.append(a[j])
#             for j in a:
#                 if j == curr+1:
#                     t.append(j)
#         temp.append(t)
#         t = []
#         i+=1
#     max_ = 0
#     for i in temp:
#         if max_ < len(i):
#             max_ = len(i)
#     return max_

# a = [4, 97, 5, 97, 97, 4, 97, 4, 97, 97, 97, 97, 4, 4, 5, 5, 97, 5, 97, 99, 4, 97, 5, 97, 97, 97, 5, 5, 97, 4, 5, 97, 97, 5, 97, 4, 97, 5, 4, 4, 97, 5, 5, 5, 4, 97, 97, 4, 97, 5, 4, 4, 97, 97, 97, 5, 5, 97, 4, 97, 97, 5, 4, 97, 97, 4, 97, 97, 97, 5, 4, 4, 97, 4, 4, 97, 5, 97, 97, 97, 97, 4, 97, 5, 97, 5, 4, 97, 4, 5, 97, 97, 5, 97, 5, 97, 5, 97, 97, 97]
# print(len(a))
# print(pickingNumbers(a))


# def climbingLeaderboard(ranked, player):
#     # Write your code here
#     i = 0
#     new_rank = []
#     while i < len(player):
#         if player[i] not in ranked:
#             ranked.append(player[i])
#         r = sorted(list(set(ranked)))[::-1]
#         rank = r.index(player[i]) + 1
#         new_rank.append(rank)
#         i += 1
#     return new_rank


# def climbingLeaderboard(ranked, player):
#     # Write your code here
#     r = sorted(list(set(ranked)))[::-1]
#     rank_ = {}
#     rank = []
#     for i in range(len(r)):
#         rank_[i+1] = r[i]
#     i = 0
#     while i < len(player):
#         for keys, values in rank_.items():
#             if player[i] == values:
#                 rank.append(keys)
            


# ranked = [100, 90, 90, 80, 75, 60]
# player = [50, 65, 77, 90, 102]
# print(climbingLeaderboard(ranked, player))


# import smtplib, ssl

# port = 465  # For SSL
# smtp_server = "smtp.gmail.com"
# sender_email = "makautcell@gmail.com"  # Enter your address
# receiver_email = "maitysomvit@gmail.com"  # Enter receiver address
# password = "SOMvit@200032"
# message = """\
# Subject: Hi there

# This message is sent from Python."""

# context = ssl.create_default_context()
# with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)

import string


# def get_width(ch, h):
#     alphabet_list = list(string.ascii_lowercase)
#     index_ch = alphabet_list.index(ch)
#     return h[index_ch]
    
    
# def designerPdfViewer(h, word):
#     # Write your code here
#     width = 1
#     for i in word:
#         ch_width = get_width(i, h)
#         print(ch_width)
#         width *= ch_width
#     return width


# a = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
# word = "abc"

# print(designerPdfViewer(a, word))



# def utopianTree(n):
#     # Write your code here
#     et = [0] * (n+1)
#     print(et)
#     for i in range(n+1):
#         if i == 0:
#             et[i] = 1
#         if i % 2 == 1: 
#             et[i] = et[i-1] * 2
#         if i % 2 == 0:
#             et[i] = et[i-1] + 1
#     return et[n]

# print(utopianTree(7))


# def angryProfessor(k, a):
#     # Write your code here
#     attendee = []
#     for i in a:
#         if i <= 0:
#             attendee.append(i)
#     if len(attendee) >= k:
#         return "No"
#     else:
#         return "Yes"
    
# a = [-1, -3, 4, 2]
# print(angryProfessor(3, a))

# def beautifulDays(i, j, k):
#     # Write your code here
#     days = []
#     for i in range(i, j+1):
#         print(int(str(i)[::-1]))
#         if abs(i-int(str(i)[::-1])) % k == 0:
#             days.append(i)
#     return len(days)




# print(beautifulDays(20, 23, 6))


# def viralAdvertising(n):
#     # Write your code here
#     cm = 2
#     starting_people = 5
#     shared = [5]
#     liked = [2]
#     for i in range(n-1):
#         share = (shared[i] // 2) * 3
#         like = share // 2
#         shared.append(share)
#         liked.append(like)
#         cm += like
#     return cm


# print(viralAdvertising(3))

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bigSorting' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY unsorted as parameter.
#
# def mergesort(unsorted):
#     if len(unsorted) > 1:
#         mid  = len(unsorted) // 2
#         l = unsorted[:mid]
#         r = unsorted[mid:]
#         mergesort(l)
#         mergesort(r)
#         i = j = k = 0
#         while i < len(l) and j < len(r):
#             if l[i] <= r[j]:
#                 unsorted[k] = l[i]
#                 i += 1
#             else:
#                 unsorted[k] = r[j]
#                 j += 1
#             k += 1
#         while i < len(l):
#             unsorted[k] = l[i]
#             k += 1
#             i += 1
#         while j < len(r):
#             unsorted[k] = r[j]
#             k += 1
#             j += 1
# def bigSorting(unsorted):
#     # Write your code here
#     mergesort(unsorted)
#     return unsorted




# a = [6, 31415926535897932384626433832795, 1, 3, 10, 3, 5]
# result = bigSorting(a)
# print(result)

# with open('testcase.txt', mode='r') as file:
#     a = file.read()

# for i in a:
#     if '\n' in i:
#         i.removesuffix('\n')
# print(a)


def countingSort(arr):
    # Write your code here
    max_ = max(arr)
    count_array = [0] * (max_+1)
    for i in range(len(arr)):
        value = arr[i]
        count_array[value] += 1
    sorted_array = []
    for i in range(len(count_array)):
        if count_array[i] > 0:
            sorted_array += ([i] * count_array[i])
    return sorted_array



a = [1, 8, 4, 6, 4, 10, 52, 47, 89, 4, 5, 3]
print(countingSort(a))