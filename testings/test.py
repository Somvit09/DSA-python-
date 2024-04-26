from typing import Any
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


# def countingSort(arr):
#     # Write your code here
#     max_ = max(arr)
#     count_array = [0] * (max_+1)
#     for i in range(len(arr)):
#         value = arr[i]
#         count_array[value] += 1
#     sorted_array = []
#     for i in range(len(count_array)):
#         if count_array[i] > 0:
#             sorted_array += ([i] * count_array[i])
#     return sorted_array



# a = [1, 8, 4, 6, 4, 10, 52, 47, 89, 4, 5, 3]
# print(countingSort(a))



# def longest_common_prefix(arr):
#     length = len(arr)
#     if length == 0:
#         return ""
#     if length == 1:
#         return arr[0]
#     arr.sort()
#     end_portion = min(len(arr[0]), len(arr[length-1]))
#     i = 0
#     while i < end_portion and arr[0][i] == arr[length-1][i]:
#         i += 1
#     pre = arr[0][0:i]
#     return pre



# arr = [
#     """flower""", """flow""", """flight"""
#     ]
# print(longest_common_prefix(arr))


# import numpy as np



# n = int(input())
# a = []
# for i in range(n):
#     a.append(list(map(float, input().split(" "))))
# np_array = np.array(a)
# print(np.linalg.det(np_array))

# n = int(input())
# a = list(map(int, input().split(" ")))
# m = int(input())
# b = list(map(int, input().split(" ")))
# s = list(set(a))

# s_ = list(set(s.extend(b)))
# print(s_)


# n = int(input())
# a = set(list(map(int, input().split(" "))))
# m = int(input())

# for i in range(m):
#     operation, length = map(int, input().split(" "))
#     print(operation, length)
#     set_ = set(list(map(int, input().split(" "))))
#     if operation == "update":
#         a.update(set_)
#     if operation == "intersection_update":
#         a.intersection_update(set_)
#     if operation == "difference_update":
#         a.difference_update(set_)
#     if operation == "symmetric_difference_update":
#         a.symmetric_difference_update(set_)
        
        
# print(sum(list(a)))


# def closestNumbers(arr):
#     # Write your code here
#     arr = list(set(arr))
#     arr.sort()
#     if len(arr) == 1:
#         return 0
#     if len(arr) > 1:
#         min_diff = arr[1] - arr[0]
#         if len(arr) == 2:
#             return arr
#     i = 1
#     while i < len(arr) and i + 1 < len(arr):
#         if min_diff > (arr[i+1] - arr[i]):
#             min_diff = (arr[i+1] - arr[i])
#         i += 1
#     pair = []
#     i = 0
#     while i < len(arr) and i + 1 < len(arr):    
#         if min_diff == (arr[i+1] - arr[i]):
#             pair.append(arr[i])
#             pair.append(arr[i+1])
#         i += 1
#     return pair

# arr = [-20, -3916237, -357920, -3620601, 7374819, -7330761, 30, 6246457, -6461594, 266854, -520, -470]
# print(closestNumbers(arr))


# def activityNotifications(expenditure, d):
#     # Write your code here
#     i = 0
#     count = 0
#     while i < len(expenditure) and i + d < len(expenditure):
#         arr = expenditure[i:d+i]
#         com_vr = expenditure[d+i]
#         print(arr, com_vr)
#         if len(arr) % 2 == 0:
#             mid_i = len(arr)//2
#             median = (arr[mid_i] + arr[mid_i-1]) / 2      
#         else:
#             mid_i = len(arr)//2
#             median = arr[mid_i] 
#         if com_vr >= (median*2):
#             count += 1 
#         i += 1
#         print("median", median, "count", count)  
#     return count 
# arr = [2, 3, 4, 2, 3, 6, 8, 4, 5]
# d = 5
# print(activityNotifications(arr, d))



# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
        

# class cirl:
#     def __init__(self):
#         self.head = None
#         self.cl = []
#     def printcl(self):
#         if self.head is None:
#             return 0 
#         n = self.head
#         self.cl.append(n.data)
#         while n.next is not self.head:
#             self.cl.append(n.next.data)
#             n = n.next

#     def insert(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#             new_node.next = self.head
#         n = self.head
#         while n.next is not self.head:
#             n = n.next
#         n.next = new_node
#         new_node.next = self.head

#     def insert_f(self, data):
#         new_node = Node(data)
#         n = self.head
#         if n is None:
#             self.head = new_node
#             new_node.next = self.head
#             return
#         while n.next is not self.head:
#             n = n.next
#         n.next = new_node
#         new_node.next = self.head
#         self.head = new_node

#     def insert_l(self, data):
#         new_node = Node(data)
#         n = self.head
#         if n is None:
#             self.head = new_node
#             new_node.next = self.head
#             return
#         while n.next is not self.head:
#             n = n.next
#         n.next = new_node
#         new_node.next = self.head

#     def rotate(self):
#         n = self.head
#         while n.next is not self.head:
#             n = n.next
#         self.head = n
#         self.head.next = n.next

        
# def circularArrayRotation(a, k, queries):
#     # Write your code here
#     c = cirl()
#     for i in a:
#         c.insert(i)
#     for i in range(k):
#         c.rotate()
#     c.printcl()
#     for i in queries:
#         print(c.cl[i])
        

# a = [1, 2, 3]
# k = 2
# q = [0, 1, 2]

# circularArrayRotation(a, k, q)


# def permutationEquation(p):
#     # Write your code here
#     y = []
#     max_ = max(p)
#     for i in range(1, max_+1):
#         x = i
#         index = (p.index(x))+1
#         index_inside = p.index(index)
#         y.append(index_inside+1)
#     return y

# p = [5, 2, 1, 3, 4]
# print(permutationEquation(p))


# def findDigits(n):
#     # Write your code here
#     temp = 0
#     for i in str(n):
#         try:
#             if n % int(i) == 0:
#                 temp += 1
#         except ZeroDivisionError:
#             continue
#     return temp

# print(findDigits(110))


# def repeatedString(s, n):
#     # Write your code here
#     if "a" not in s:
#         return 0
#     if len(s) == 1:
#         if s == "a":
#             return n
#     temp_str = ""
#     for i in s:
#         if i == "a":
#             temp_str += i
#     print(temp_str, len(temp_str), len(s))
#     if temp_str == s:
#         return n
    
#     d = n // len(s)
#     excess = abs(len(s)*d - n)
#     count = len(temp_str) * d
#     new_string = s[:excess]
#     count_ = 0
#     for i in new_string:
#         if i == "a":
#             count_ += 1
#     return count_ + count

# a = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# n = 534802106762
# print(repeatedString(a, n))

# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         a = "".join(str(i) for i in l1[::-1])
#         b = "".join(str(i) for i in l2[::-1])
#         result = int(a) + int(b)
#         r = list(str(result)[::-1])
#         return [int(i) for i in r]


# a = [2,4,3]
# b = [5,6,4]

# s = Solution()
# print(s.addTwoNumbers(a,b))
# from typing import Optional

# # Definition for singly-linked list.
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class ListNode:
#     def __init__(self):
#         self.head = None
#         self.list_ = []

#     def ll_to_list(self, ll):
#         pass

#     def new_ll(self, l):
#         self.list_ = l
#         self.head = Node(self.list_[0])
#         n = self.head
#         for i in range(1, len(self.list_)):
#             n.next = Node(self.list_[i])
#             n = n.next

#     def printLL(self):
#         if self.head is None:
#             return 0
#         n = self.head
#         print(n.data, end="-->")
#         while n.next is not None:
#             print(n.next.data, end="-->")
#             n = n.next
    
#     def insert(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         n = self.head
#         while n.next is not None:
#             n = n.next
#         n.next = new_node
#         new_node.next = None

#     def insert_f(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         new_node.next = self.head
#         self.head = new_node

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
#         s1 = ListNode()
#         s2 = ListNode()
#         s1.new_ll(l1)
#         s2.new_ll(l2)
#         a = self.addTwoNumbers_main(s1.list_, s2.list_)
#         print(a)
#     def addTwoNumbers_main(self, l1, l2):
#         a = "".join(str(i) for i in l1[::-1])
#         b = "".join(str(i) for i in l2[::-1])
#         result = int(a) + int(b)
#         r = list(str(result)[::-1])
#         return [int(i) for i in r]
        

# d = Solution()
# l1 = [2,4,3]
# l2 = [5,6,4]
# d.addTwoNumbers(l1, l2)


# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         s = str(x)
#         if '-' in s:
#             return "false"
#         index = len(s) // 2
#         if len(s) % 2 == 1:
#             if s[:index+1] == s[index:][::-1]:
#                 return "true"
#             elif s[:index] == s[index:][::-1]:
#                 return "true"
#             return "false"
        
# z = Solution()
# print(z.isPalindrome(-121))


# class Solution:
#     def position(self, number):
#         if number in range(1, 4):
#             return "I"*number
#         if number == 4:
#             return "IV"
#         if number == 5:
#             return "V"
#         if number in range(6, 9):
#             return "V" + "I"*(number-5)
#         if number == 9:
#             return "IX"
#     def position_under_50(self, number, divider, divisor):
#         x = "X"*divider
#         rest = self.position(number-(divisor * divider))
#         return x+rest
#     def find_dividor_divisor(self, number, string_):
#         div = [1, 10, 100, 1000]
#         divisor = div[len(string_)-1]
#         divider = number // divisor
#         return divider, divisor
#     def romanToInt(self, s: str) -> int:
#         number = int(s)
#         if number < 10:
#             return self.position(number)
#         if number == 10:
#             return "X"
#         if number < 50:
#             divider, divisor = self.find_dividor_divisor(number, s)
#             return self.position_under_50(number, divider, divisor)
#         if number < 90:
#             rest_number = (number-50)
#             divider, divisor = self.find_dividor_divisor(rest_number, s)
#             return "L" + self.position_under_50(rest_number, divider, divisor)
#         if number == 90:
#             return "XC"
#         if number > 90 and number <100:
#             rest_number = number-90
#             return "XC" + self.position(rest_number)

#         return f"({divisor} * {divider}) + {number-(divisor * divider)} = {number}"
        



# class Solution:
#     def position_1_10(self, string):
#         if "I" in string:
#             if string.count("I") == len(string):
#                 return len(string)
#         if "IV" in string:
#             return 4
#         if "V" in string and len(string) == 1:
#             return 5
#         if string[0] == "V":
#             if "I" in string:
#                     return (5 + string.count("I"))
#         if "IX" in string:
#             return 9
#         if "X" in string:
#             return 10

#     def romanToInt(self, s: str) -> int:
#         return self.position_1_10(string=s)
    
# s = Solution()

# #print(s.romanToInt("VI"))

# def a(b):
#     def f():
#         print("dvkfjvbkfn")
#         b()
#     return f
# @a
# def b():
#     print("dkvfk")

# def a(b):
#     for i in range(b):
#         yield i

# for i in a(5):
#     print(i)

# a = lambda x: x*2
# def a(c, b, *args):
#     v = c + b
#     for i in args:
#         v += i
#     return v

# def a(**kwags):
#     for i, k in kwags.items():
#         print(i, k)
# a(arg1 = "jdkdv", arg2="cdjcvdj", arg3="dfjdjv")


# def tellArguments(**kwargs):  
#     for key, value in kwargs.items():
#         print(key + ": " + value)
# tellArguments(arg1 = "argument 1", arg2 = "argument 2", arg3 = "argument 3")

# class a:
#     def __init__(self, car):
#         self.__car = car

#     @property
#     def get_attr(self):
#         print(self.__car)

#     @get_attr.setter
#     def get_attr(self, new_car):
#         self.__car = new_car

# s = a("dkvcnjknv")
# print(s.get_attr)
# a.get_attr = "dkvjnjvfnrnvrn"
# print(s.get_attr)


# class a:
#     def __init__(self, cat):
#         self.cat = cat
#     def f(self):
#         print("djgvknfbvkrnk")

# class b(a):
#     def __init__(self,cat, dog):
#         super().__init__(cat)
#         self.dog =dog
#     def c(self):
#         print("dfkdgvkrf")

# x = b("sjcdsjv", "dvjnfjvb")
# x.f()
# x.c()
# print(x.cat, x.dog)

# class a:
#     def fly(self):
#         pass

# class bird(a):
#     def fly(self):
#         print("birds can fly")

# class dog(a):
#     def fly(self):
#         print("dogs cannot fly")


# x = [bird(), dog()]
# for i in x:
#     i.fly()


# def superReducedString(s):
#     # Write your code here
#     dict_s = {}
#     for i in s:
#         if i in dict_s:
#             dict_s[i] += 1
#         else:
#             dict_s[i] = 1
#     print(dict_s)
#     result_str = ''
#     for keys, values in dict_s.items():
#         if values % 2 == 1:
#             result_str += keys
#     if result_str != "":
#         return result_str
#     return "Empty String"

# s = "acdqglrfkqyuqfjkxyqvnrtysfrzrmzlygfveulqfpdbhlqdqrrqdqlhbdpfqluevfgylzmrzrfsytrnvqyxkjfquyqkfrlacdqj"
# print(superReducedString(s))


# def camelcase(s):
#     # Write your code here
#     count = 0
#     for i in s:
#         if i.isupper():
#             count += 1
#     return count


# numbers = "0123456789"
# lower_case = "abcdefghijklmnopqrstuvwxyz"
# upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# special_characters = "!@#$%^&*()-+"

# def minimumNumber(n, password):
#     has_digit = False
#     has_upper = False
#     has_lower = False
#     has_special = False
#     has_6_chs = False

#     if n >= 6:
#         has_6_chs = True
    
#     for char in password:
#         if char.isdigit():
#             has_digit = True
#         elif char.isupper():
#             has_upper = True
#         elif char.islower():
#             has_lower = True
#         else:
#             has_special = True
#     count = 0
#     if has_6_chs:
#         if not has_digit:
#             count += 1
#         if not has_lower:
#             count += 1
#         if not has_upper:
#             count += 1
#         if not has_special:
#             count += 1
#         return count
#     else:
#         print("n<6")
#         if not has_digit:
#             count += 1
#         if not has_lower:
#             count += 1
#         if not has_upper:
#             count += 1
#         if not has_special:
#             count += 1
#         if count >= (6-n):
#             return count
#         else:
#             return (6-n)
        

        
# s = '4700'

# print(minimumNumber(len(s), s))

# def s(fun):
#     def d():
#         print("d function called")
#         fun()
#     return d

# @s
# def fun():
#     print("fun function called")

# fun()

# def c(n):
#     for i in range(n):
#         yield i

# for i in c(10):
#     print(i)

# a = lambda x:x+2

# print(a(8))
# from copy import copy
# a = [1, 8, 7]
# b = copy(a)
# print(b)
# import csv
# with open('MOCK_DATA.csv', mode='r') as file:
#     sd = csv.reader(file)

#     for lines in sd:
#         print(lines)

# def a(*args):
#     v = 0
#     for i in args:
#         v += i
#     return v
# print(a(1, 5, 7, 8))
# def b(**kwargs):
#     for k, v in kwargs.items():
#         print(k, ":", v)
#     return kwargs
# print(b(arg1="fcjdnv", u44="jfcbejbcvj"))

# class x:
#     pass
# class y(x):
#     pass

# s = x()
# print("smfksnknk")
# if __name__ == "__main__":
#     print(isinstance(s, x))


# class a:
#     def __init__(self, car):
#         self.__car = car
#     @property
#     def get_attr(self):
#         return self.__car
    
#     @get_attr.setter
#     def get_attr(self, new_car):
#         self.__car = new_car

# s = a("porchse")
# print(s.get_attr)
# s.get_attr = "nano"
# print(s.get_attr)
# class a:
#     def __init__(self, cat):
#         self.cat = cat

#     def print_c(self):
#         return self.cat

# class b(a):
#     def __init__(self,cat, dog):
#         super().__init__(cat)
#         self.dog = dog

#     def print_c(self):
#         return self.cat, self.dog
    
# class c(a):
#     def __init__(self,cat, bird):
#         super().__init__(cat)
#         self.bird = bird

#     def print_c(self):
#         return self.cat, self.bird


# for i in (b("cat", "dog"), c("cat", "bird")):
#     print(i.print_c())

# def mergesort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2
#         l = arr[:mid]
#         r = arr[mid:]
#         mergesort(l)
#         mergesort(r)
#         i = j = k = 0
#         while i < len(l) and j < len(r):
#             if l[i] < r[j]:
#                 arr[k] = l[i]
#                 i += 1
#             else:
#                 arr[k] = r[j]
#                 j += 1
#             k += 1

#         while i < len(l):
#             arr[k] = l[i]
#             i += 1
#             k += 1
#         while j < len(r):
#             arr[k] = r[j]
#             j += 1
#             k += 1

# arr = [1, 85, 4, 6, 1, 2, 20]


# def partition(arr, low, high):
#     pivot = arr[high]
#     pindex = low
#     for i in range(low, high):
#         if arr[i] < pivot:
#             arr[i], arr[pindex] = arr[pindex], arr[i]
#             pindex += 1
#     arr[high], arr[pindex] = arr[pindex], arr[high]
#     return pindex 

# def quicksort(arr, l, r):
#     if l<r:
#         pi = partition(arr, l, r)
#         partition(arr, l, pi-1)
#         partition(arr, pi+1, r)


# def insertionsor(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i-1
#         while j>=0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key

# def count_sort(arr):
#     count_array = [0]*(max(arr)+1)
#     for i in arr:
#         count_array[i] += 1
#     temp = []
#     for i in range(len(count_array)):
#         if count_array[i] > 0:
#             temp += [i] * count_array[i]
#     print(temp)

# def binarysearch(arr, key):
#     l = 0
#     r = len(arr) - 1
    
#     while l <= r:
#         mid = (l+r)//2
#         if arr[mid] == key:
#             return arr[mid]
#         if arr[l] < key:
#             l = mid+1
#         else:
#             r = mid - 1

# class stack:
#     def __init__(self):
#         self.stack_ = []
#     def push(self, data):
#         self.stack_.append(data)

#     def pop_(self):
#         self.stack_.pop()
#     def pop_with_value(self, data):
#         self.stack_.pop(self.stack_.index(data))
#     def isempty(self):
#         return len(self.stack_) == 0
#     def peek(self):
#         return self.stack_[-1]
#     def print_s(self):
#         print(self.stack_[::-1])
    
# s = stack()
# s.push(1)
# s.push(2)
# s.push(3)
# s.push(4)
# s.print_s()
# s.pop_()
# s.print_s()
# s.pop_with_value(1)
# s.print_s()
# print(s.isempty())
# print(s.peek())
# s.print_s()

# class node:
#     def __init__(self, data):
#         self.data = data
#         self.left = None
#         self.right = None

# class bst:
#     def __init__(self):
#         self.root = None
#     def print_bst(self, root):
#         print(root.data)
#         if root.left:
#             self.print_bst(root.left)
#         if root.right:
#             self.print_bst(root.right)
# n = node(1)
# n.left = node(2)
# n.right = node(3) 
# a = bst()
# a.print_bst(n)


# a = 'abc'
# count_dict = {}
# for i in a:
#     if i in count_dict:
#         count_dict[i] += 1
#     else:
#         count_dict[i] = 1
# print(count_dict)


# def sum_3_5(n):
#     sum_ = 0
#     for i in range(1, n):
#         if i % 3 == 0 or i % 5 == 0:
#             print(i)
#             sum_ += i
#             print(sum_)
#     return sum_

# T = int(input())
# for i in range(T):
#     N = int(input())
#     print(sum_3_5(N))
    

# import sys

# def check_prime(n):
#     if n <= 1:
#         return False
#     if n % 2 == 0:
#         return False
#     if n == 2:
#         return True
#     return True
# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     temp = []
#     if n % 2 == 0:
#         for i in range(1, n):
#             if n % i == 0:
#                 print(check_prime(i), i)
#                 if check_prime(i):
#                     temp.append(i)
#     else:
#         for i in range(1, n+1):
#             if n % i == 0:
#                 print(check_prime(i), i)
#                 if check_prime(i):
#                     temp.append(i)
#     print(max(temp))
    



#!/bin/python3

#!/bin/python3

# import sys


# def fibonacci(n):
#     temp = [1, 2] 
#     j = 1
#     while temp[j] <= n:
#         print(temp[j])
#         temp.append(temp[j]+temp[j-1])
#         j += 1
#     return temp[:-1]
        


# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     temp = fibonacci(n)
#     sum_ = 0
#     for i in temp:
#         if i % 2 == 0:
#             sum_ += i
#     print(sum_)




#!/bin/python3

# import sys

# def check_prime(n):
#     if n <= 1:
#         return False
#     if n % 2 == 0:
#         return False
#     if n == 2:
#         return True
#     for i in range(3, int(math.sqrt(n)) + 1, 2):
#         if n % i == 0:
#             return False
#     return True

# t = int(input().strip())
# for a0 in range(t):
#     n = int(input().strip())
#     count = 1
#     i = 2
#     primes = [2]
#     while count < n:
#         if check_prime(i):
#             primes.append(i)
#             count += 1
#         i += 1
#     print(primes[len(primes) - 1], primes)
        
    
    
# from functools import reduce
# def problem(n):
#     temp = []
#     i, k = 0, 5
#     last_pointer = i+k
#     while not last_pointer == (len(str(n))+1):
#         temp.append(str(n)[i:last_pointer])
#         last_pointer += 1
#         i += 1
#     max_temp = []
#     number_list = [list(map(int, s)) for s in temp]
#     multiply = lambda a, b: a*b
#     products = [reduce(multiply, i) for i in number_list]
#     return max(products)
    
    

# print(problem(3675356291))

# def problem(n):
#     i = 6
#     if i > n:
#         return (-1)
#     temp = []
#     for i in range(i, n+1, 3):
#         temp.append(i)
    
#     if n in temp:
#         m = temp.index(n)+1
#     else:
#         return (-1)
    
#     if (m**2+(m+1)**2) == (m+2)**2:
#         return (m*(m+1)*(m+2))
#     return -1



# print(problem(4))
# Enter your code here. Read input from STDIN. Print output to STDOUT

# def find_dividors(n):
#     dividor = 0
#     for i in range(1, n+1):
#         if n % i == 0:
#             dividor += 1
#     return dividor

# def trianle_number(k):
#     temp = []
#     dividors = []
#     number = 0
#     i = 1
#     while True:
#         number += i
#         temp.append(number)
#         v = find_dividors(number)
#         dividors.append(v)
#         if v > k:
#             return temp[i-1]
#         i += 1


# T = int(input())
# for i in range(T):
#     k = int(input())
#     print(trianle_number(k))


# def count_divisors_with_prime_factorization(n):
#     # Calculate the prime factors and their counts
#     factors = {}
#     i = 2
#     while i * i <= n:
#         while n % i == 0:
#             n //= i
#             factors[i] = factors.get(i, 0) + 1
#         i += 1
#     if n > 1:
#         factors[n] = factors.get(n, 0) + 1

#     # Calculate the number of divisors using prime factorization
#     divisors = 1
#     for count in factors.values():
#         divisors *= count + 1

#     return divisors

# def find_triangle_number_with_divisors(N):
#     num = 1
#     triangle_num = 1
#     while True:
#         divisors = count_divisors_with_prime_factorization(triangle_num)
#         if divisors > N:
#             return triangle_num
#         num += 1
#         triangle_num += num

# T = int(input())

# for _ in range(T):
#     N = int(input())
#     result = find_triangle_number_with_divisors(N)
#     print(result)

# Enter your code here. Read input from STDIN. Print output to STDOUT

# def Collatz(n):
#     temp = [n]
#     while n != 1:
#         if n % 2 == 0:
#             value = int(n/2)
#         else:
#             value = (3*n) + 1
#         temp.append(value)
#         n = value
#     print(temp)
#     return len(temp)-1
    
    
# T = int(input())
# for i in range(T):
#     n = int(input())
#     temp = []
#     for i in range(1, n+1):
#         temp.append(Collatz(i))
#     maximum_c = max(temp)
#     if temp.count(maximum_c) > 1:
#         print((temp.index(maximum_c))+1, maximum_c)
    


# def factorial(n):
#     m = 1
#     for i in range(1, n+1):
#         m *= i
#     return m

# def problem(n):
#     sum_ = 0
#     for i in str(n):
#         sum_ += int(i)
#     return sum_



# print(problem(factorial(10)))


# Enter your code here. Read input from STDIN. Print output to STDOUT

# def amicable(n):
#     sum_ = 0
#     for i in range(1, (n//2)+1):
#         if n % i == 0:
#             sum_ += i
#     return sum_

# def problem(n):
#     for i in range(n, 1, -1):
#         if amicable(amicable(i)) == i:
#             print(amicable(i) , amicable(amicable(i)) )
#             #return amicable(i) + amicable(amicable(i))  


# T = int(input())
# for _ in range(T):
#     n = int(input())
#     print(problem(n))


# ch = ['ALEX', 'LUIS', 'JAMES', 'BRIAN', 'PAMELA']
# ch.sort()
# print(ch)

# def alphabet_index(alphabet):
#     # Ensure the input is a single alphabet character and convert it to uppercase
#     if len(alphabet) == 1 and alphabet.isalpha():
#         alphabet = alphabet.upper()
#         # Subtract the ASCII value of 'A' to get the index (0-25)
#         index = ord(alphabet) - ord('A')
#         return index+1
#     else:
#         return None  # Invalid input


def get_Fibonacci_number(n):
    temp = [1, 1, 2]
    temp_d = {1: 1}
    i = len(temp)-1
    j = i-1
    while i < 5000 or n < 5000:
        sum_ = temp[i] + temp[j]
        temp.append(sum_)
        if len(str(temp[i])) < len(str(sum_)):
            temp_d[len(str(sum_))] = sum_
        if n in temp_d.keys():
            value = temp_d[n]
            return temp.index(value)+1
        i += 1
        j += 1



# T = int(input())
# for _ in range(T):
#     n = int(input())
#     print(get_Fibonacci_number(n))



# def fibo():
#     a = 0
#     b = 1
#     while True:
#         yield b
#         a,b = b,a+b

# f = enumerate(fibo())
# x = 0
# while len(str(x)) < 1000:
#     i,x = next(f)

# print("The %d-th term has %d digits"%(i+1,len(str(x))))

    

# from math import log10, floor, ceil

# def euler25(k):
#     if k < 2:
#         return 1
#     ϕ = (1 + 5**0.5) / 2
#     return ceil((k + log10(5) / 2 - 1) / log10(ϕ))

# T = int(input())
# for i in range(T):
#     n = int(input())
#     try:
#         result = euler25(n)
#         print(result)
#     except Exception as e:
#         print(f"Runtime error for n = {n}: {e}")
#     except TimeoutError as t:
#         print(f"Timeout error for n = {n}: {t}")


# class Solution:

#     def check_parenthesis_after(self, p1, p2, s):
#         if p1 in s:
#             index = s.index(p1)
#             if s[index+1] != p2:
#                 return False
#         return True
    
#     def check_parenthesis_before(self, p1, p2, s):
#         if p1 in s:
#             index = s.index(p1)
#             if s[index-1] != p2:
#                 return False
#         return True

#     def isValid(self, s: str) -> bool:
#         list_s = list(s)
#         temp = [
#           self.check_parenthesis_after('(', ')', list_s),
#           self.check_parenthesis_after('{', '}', list_s),
#           self.check_parenthesis_after('[', ']', list_s),
#           self.check_parenthesis_before(']', '[', list_s),
#           self.check_parenthesis_before('}', '{', list_s),
#           self.check_parenthesis_before(')', '(', list_s),
#         ]

#         if False in temp:
#             return False
#         return True

              
        


# class Solution:
#     def removeDuplicates(self, nums) -> int:
#         i = 0
#         while i < len(nums):
#             count = nums.count(nums[i])

#             if count > 1:
#                 for _ in range(count-1):
#                     nums.pop(nums.index(nums[i]))
#             i += 1

#         return len(nums)
    


class Solution:
    def strStr(self, haystack: str, needle: str):
        splited = haystack.split(needle)
        print(splited)
        if splited:
            try:
                substring = haystack.index(needle)
                print(substring)
                if substring >= 0:
                    return substring
            except ValueError:
                substring = None
        return -1




class Solution:
    def searchInsert(self, nums, target: int) -> int:
        if target in nums:
            return nums.index(target)
        temp = []
        i = 0
        while nums[i] < target:
            temp.append(nums[i])
            i += 1
        temp_len = len(temp)
        temp = None
        return temp_len
    
class Solution:
    def plusOne(self, digits: [int]) -> [int]:
        number = ""
        for i in digits:
            number += str(i)
        number = int(number) + 1
        return list(map(int, str(number)))

digits = [9, 9]

class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        # Create an array to store the number of ways to reach each step
        dp = [0] * (n + 1)
        
        # There is 1 way to reach the 0th step (base case)
        dp[0] = 1
        
        # There is 1 way to reach the 1st step (base case)
        dp[1] = 1
        print(dp)
        
        # Calculate the number of ways to reach each step from 2 to n
        for i in range(2, n + 1):
            # The number of ways to reach the current step is the sum of the ways
            # to reach the previous two steps (1 step + 1 step or 2 steps)
            dp[i] = dp[i - 1] + dp[i - 2]
            print(dp)
        
        # The result is the number of ways to reach the top (the nth step)
        return dp[n]
    

class Solution:
    def mergesort(self, arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            l = arr[:mid]
            r = arr[mid:]
            self.mergesort(l)
            self.mergesort(r)
            i = j = k = 0
            while i<len(l) and j<len(r):
                if l[i] < r[j]:
                    arr[k] = l[i]
                    i += 1
                else:
                    arr[k] = r[j]
                    j += 1
                k += 1
            while i < len(l):
                arr[k] = l[i]
                i += 1
                k += 1
            while j < len(r):
                arr[k] = r[j]
                j += 1
                k += 1

    def merge(self, nums1: [int], m: int, nums2: [int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        print(nums1[::-1])
        nums1_reversed = nums1[::-1]
        while i < len(nums1_reversed):
            if nums1_reversed[i] == 0:
                nums1_reversed.pop(i)
                i -= 1
            elif nums1_reversed[i] != 0:
                break
            i += 1
        nums1[:] = nums1_reversed[::-1]
        print(nums1)
        nums1.extend(nums2)
        nums1.sort()
       
        return nums1    


# s = Solution()
# nums1 = [-1,0,0,3,3,3,0,0,0]
# m = 3 
# nums2 = [1,2,2]
# n = 3
# print(s.merge(nums1, m, nums2, n))


class Solution:
    def singleNumber(self, nums: [int]) -> int:
        result = 0
        
        for num in nums:
            result ^= num
            print(result)
        
        return result
import re
    
class Solution:
    def isPalindrome(self, s: str) -> str:
        if s == " " or "":
            return True
        new_str = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        print(new_str)
        length = len(new_str)
        count = length // 2
        if length % 2 == 1:
            if new_str[:count] == new_str[count+1:][::-1]:
                return True
        else:
            if new_str[:count] == new_str[count:][::-1]:
                return True
        return False


# Enter your code here. Read input from STDIN. Print output to STDOUT
def find_series(n):
    sum_ = 0
    for i in range(1, n+1):
        sum_ += i**i
        print(sum_)
    return str(sum_)
    
def find_smallest_n_with_divisors(threshold):
    count = 0
    temp = []
    for i in range(1, 100):
        for j in range(1, 100):
            s = ((i*j)//(i+j))
            if (i*j)%(i+j) == 0:
                if threshold == s:
                    if i and j not in temp:
                        count += 1
                        temp.append(i)
                        temp.append(j)
    
    return count

def max_team_power_difference(N, powers):
    # Sort avengers in descending order of their power
    powers.sort(reverse=True)

    team_1_power = 0
    team_2_power = 0

    for i in range(N):
        if i % 2 == 0:
            team_1_power += powers[i]
        else:
            team_2_power += powers[i]

    return abs(team_1_power - team_2_power)
def solutiom():
    # Read the sequence
    sequence = input().strip()

    # Check for duplicate characters in the sequence
    if len(sequence) != len(set(sequence)):
        print("New Language Error")
    else:
        # Read the string to be converted
        string_to_convert = input().strip()
        
        # Create a dictionary to map characters to their positions in the sequence
        char_mapping = {}
        for i, char in enumerate(sequence):
            char_mapping[char] = i
        
        # Convert the string based on the sequence
        converted_string = ""
        for char in string_to_convert:
            if char.lower() in char_mapping:
                converted_string += char if char.islower() else char.lower()
        
        print(converted_string)


#  problem B
'''
'''
def problem(n:str, m:str) -> str:
    if len(n) != len(set(n)):
        return "New Language Error"
    def alpha_number_separation(n):
        alphabet1 = ""
        number1 = ""
        for i in n:
            if i.isalpha():
                alphabet1 += i
            elif i.isdigit():
                number1 += i
        return alphabet1, number1
    
    alphabet1, number1 = alpha_number_separation(n)
    alphabet2, number2 = alpha_number_separation(m)

    alphabet1 = alphabet1.lower()
    alphabet2 = alphabet2.lower()

    def conversion(alphabetOrNum1, alphabetOrNum2):
        temp_alOrNumber = []
        for i in alphabetOrNum2:
            if i in alphabetOrNum1:
                temp_alOrNumber.append(alphabetOrNum1.index(i))
            else:
                temp_alOrNumber.append(101)
        alOrNum_str = ""
        temp_alOrNumber.sort()
        for i in temp_alOrNumber:
            if i != 101:
                alOrNum_str += alphabetOrNum1[i]
        return alOrNum_str

    alpha_str = conversion(alphabet1, alphabet2)
    number_str = conversion(number1, number2)

    return alpha_str + " " +  number_str




# if __name__ == "__main__":
#     s_sequence = input()
#     c_sequence = input()
#     result = problem(s_sequence, c_sequence)
#     print(result)
    
    
# problem C

'''
'''
def problemC(number_str:str, action:str):
    number_list = list(map(int, number_str))
    i = 0
    j = 0
    while i < len(action):
        if action[i] == 'R':
            if j + 1 < len(number_list):
                j += 1
            else:
                break
        if action[i] == 'L':
            if j == 0:
                pass
            j -= 1
        if action[i] == 'T':
            number_list[j] += 1
        if action[i] == 'D':
            number_list[j] -= 1
        if action[i] == 'S':
            # Check if there's a valid index after 'S'
            if i + 1 < len(action) and action[i + 1].isdigit():
                swap_index = int(action[i + 1]) - 1
                if 0 <= swap_index < len(number_list):
                    number_list[j], number_list[swap_index] = number_list[swap_index], number_list[j]
                    i += 1  # Skip the digit following 'S'
                else:
                    # Handle invalid index
                    print("Invalid swap index")
        i += 1

    return ''.join(map(str, number_list))

            

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head:
            return head

        current = head
        temp = []
        
        while current:
            if current.val not in temp:
                temp.append(current.val)
            current = current.next

        new_head = ListNode(temp[0])
        current = new_head

        for val in temp[1:]:
            current.next = ListNode(val)
            current = current.next

        return new_head

    

def printLL(head):
    print(head.val)
    while head.next:
        print(head.next.val, end=" ")
        head = head.next



input_list = [1,1,2,3,3]
i = 1
head = ListNode(1)
while i < len(input_list):
    head.next = ListNode(input_list[i])
    head = head.next
    i += 1



# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]):
        temp = []
        while list1:
            temp.append(list1.val)
            list1 = list1.next
        while list2:
            temp.append(list2.val)
            list2 = list2.next
        temp.sort()
        head = ListNode(temp[0])
        current = head
        for i in range(1, len(temp)):
            current.next = ListNode(temp[i])
            current = current.next
        return head
        
list1 = [1, 2, 4]
list2 = [1, 3, 4]

# Create the head and current variables for list1 and list2
head1 = ListNode(list1[0])
current1 = head1

head2 = ListNode(list2[0])
current2 = head2

# Populate list1 and list2
for i in range(1, len(list1)):
    current1.next = ListNode(list1[i])
    current1 = current1.next

for i in range(1, len(list2)):
    current2.next = ListNode(list2[i])
    current2 = current2.next

# s = Solution()
# head = s.mergeTwoLists(head1, head2)
# current = head
# while current:
#     print(current.val, end = " ")
#     current = current.next


def problem(s:str, a:str)-> str:
    if a in s:
        return 'yes'
    return "no"

input1 = 'abab'
input2 = 'baaa'

class Solution:
    def middleNode(self, head: [ListNode]) -> [ListNode]:
        length = 0
        current = head
        while current:
            current = current.next
            length += 1
        i = 0
        current_even = head
        while i < (length // 2) + 1:
            current_even = current_even.next
            i += 1
        return current_even
    

class Solution:
    def isPalindrome(self, head: [ListNode]) -> bool:
        ll_str = ''
        current = head
        while current:
            ll_str += str(current.val)
            current = current.next
        print(ll_str)
        palindrome = [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99]
        if len(ll_str) < 3:
            if int(ll_str) in palindrome:
                return True
        mid = len(ll_str) // 2
        if len(ll_str) % 2 == 0:
            print(ll_str[:mid], ll_str[mid:])
            if ll_str[:mid] == ll_str[mid:][::-1]:
                return True
        else:
            print(ll_str[:mid], ll_str[mid+1:])
            if ll_str[:mid] == ll_str[mid+1:][::-1]:
                return True
        return False
    
a = [1,2,2,2,1]
def convert_ll(a:list):
    head = ListNode(a[0])
    current = head
    for i in range(1, len(a)):
        current.next = ListNode(a[i])
        current = current.next
    return head

def print_LL(head):
    current = head
    while current:
        print(current.val, end="-->")
        current = current.next

class Solution:
    def reverseList(self, head: [ListNode]) -> [ListNode]:
        temp = []
        current = head
        while current:
            temp.append(current.val)
            current = current.next
        print(temp)
        temp = temp[::-1]
        print(temp)
        head = ListNode(temp[0])
        current = head
        for i in range(1, len(temp)):
            current.next = ListNode(temp[i])
            current = current.next

        return head


class Solution:
    def sortedMerge(self, a, b, c, n, m):
        i = 0  # Index for array a
        j = 0  # Index for array b
        k = 0  # Index for array c

        while i < n and j < m:
            if a[i] < b[j]:
                c[k] = a[i]
                i += 1
            else:
                c[k] = b[j]
                j += 1
            k += 1

        # Copy the remaining elements from a and b if any
        while i < n:
            c[k] = a[i]
            i += 1
            k += 1

        while j < m:
            c[k] = b[j]
            j += 1
            k += 1

        c.sort()
        return c
    

s = Solution()
# print(s.sortedMerge([10, 5, 15], [20, 3, 2], [0,0,0,0,0,0], 3, 3))


class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None
    
class BST:
    def __init__(self):
        self.root = None

    def printBST(self):
        return self._printBST(self.root)
    
    def _printBST(self, root):
        if root:
            print(root.data, end='-->')
            if root.left:
                self._printBST(root.left)
            if root.right:
                self._printBST(root.right)
            
    def insertBST(self, data):
        if self.root is None:
            self.root = Node(data)
        elif data == self.root.data:
            return "Node is already present"
        else:
            self._insertBST(self.root, data)
    def _insertBST(self, node, data):
            if data > node.data:
                if  node.right:
                    self._insertBST(node.right, data)
                else:
                    node.right = Node(data)
            else:
                if node.left:
                    self._insertBST(node.left, data)
                else:
                    node.left = Node(data)
    def search(self, key):
        return self._search(self.root, key)
    
    def _search(self, node, key):
        if node is None:
            return f"Node is none."
        if node.data == key:
            return f"{key} is found"
        if key < node.data:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)


if __name__ == '__main__':
    names = ['Harry', 'Berry', 'Tina', 'Akriti', 'Harsh']
    new_name = []
    scores = [37.21, 37.21, 37.2, 41, 39]
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     names.append(name)
    #     scores.append(score)
    temp = sorted(list(set(scores)), reverse=False)
    second = temp[1]
    second_count = scores.count(second)
    if second_count > 1:
        index = 0
        for i in scores:
            if i == second:
                new_name.append(names[index])
            index += 1
    elif second_count == 1:
        new_name.append(names.index(second))
    new_name.sort()


def timeConversion(s):
    # Write your code here
    temp = s.split(":")
    if temp[2][2:] == "AM":
        if temp[0] ==  "12":
            temp[0] = "00"
            temp[2] = temp[2][:2]
            return ":".join(temp)
    else:
        if temp[0] != "12":
            temp[2] = temp[2][:2]
            temp[0] = str(int(temp[0]) + 12)
            return ":".join(temp)
    return s[:len(s)-2]
    
def flippingBits(n):
    # Write your code here
    a = str(format(n, '032b'))
    new_str = ""
    for i in range(len(a)):
        if a[i] == "1":
            new_str += "0"
        else:
            new_str += "1"
    decimal_number = int(new_str, 2)
    return decimal_number

def countingSort(arr):
    # Write your code here
    max_ = 100
    count_array = [0] * max_
    for i in range(len(arr)):
        value = arr[i]
        count_array[value] += 1
    print(sorted(a))
    return count_array
a =  [63, 54, 17, 78, 43, 70, 32, 97, 16, 94, 74, 18, 60, 61, 35, 83, 13, 56, 75, 52, 
      70, 12, 24, 37, 17, 0, 16, 64, 34, 81, 82, 24, 69, 2, 30, 61, 83, 37, 97, 
      16, 70, 53, 0, 61, 12, 17, 97, 67, 33, 30, 49, 70, 11, 40, 67, 94, 84, 60, 
      35, 58, 19, 81, 16, 14, 68, 46, 42, 81, 75, 87, 13, 84, 33, 34, 14, 96, 7, 59, 17, 
      98, 79, 47, 71, 75, 8, 27, 73, 66, 64, 12, 29, 35, 80, 78, 80, 6, 5, 24, 49, 82]

import string
def pangrams(s):
    # Write your code here
    s = s.lower()
    temp = ""
    alp_str = string.ascii_lowercase
    for i in s:
        if i in alp_str and i not in temp:
            temp += i
    if len(temp) == len(alp_str):
        return "pangram"
    else:
        return "not pangram"

ch = "We promptly judged antique ivory buckles for the next prize"


def birthday(s, d, m):
    # Write your code here
    i = 0
    count = 0
    if len(s) == 1:
        if m == 1:
            if d  == s[0]:
                return 1
    while i < len(s) and i+m < len(s):
        print(s[i:i+m])
        if sum(s[i:i+m]) == d:
            count += 1
        i += m
    return count
        


s = [2, 3, 4, 4, 2, 1, 2, 5, 3, 4, 4, 3, 4, 1, 3, 5, 4, 5, 3, 1, 1, 5, 4, 3, 5, 3, 5, 
        3, 4, 4, 2, 4, 5, 2, 3, 2, 5, 3, 4, 2, 4, 3, 3, 4, 3, 5, 2, 5, 1, 3, 1, 4, 2, 2, 4, 
        3, 3, 3, 3, 4, 1, 1, 4, 3, 1, 5, 2, 5, 1, 3, 5, 4, 3, 3, 1, 5, 3, 3, 3, 4, 5, 2]
d = 26
m = 8

# print(birthday(s, d, m))


# class A:
#     def __init__(self, gender):
#         self.__gender = gender
#     def _gender(self):
#         print(self.__gender)
#     def print_gender(self):
#         print(self.__gender)
# try:
#     s = A('male')
#     s._gender()
#     s.print_gender()
#     print(s.__gender)
# except AttributeError as e:
#     print(e)
# finally:
#     print("done with the function")

# class B:
#     def __init__(self_other, car):
#         self_other.car = car
#     def print_car(self_other):
#         print(self_other.car)
# s = B("Farrery")
# s.print_car()

# def f():
#     var = 1
#     for i in range(1, 11):
#         var_ = var * i
#         yield var_
#     return 
# for i in f():
#     print(i)

# import array
# a = array.array('i', [1, 2, 3])
# print(a, type(a))

# def s(func):
#     def d():
#         print("dnvjndf")
#         func()
#         print("bhosda")
#     return d
# @s
# def b():
#     print("b")
# b()
# a = lambda b, c: b*c
# print(type(range(1, 9)))
# with open('testcase.txt', mode='r') as file:
#     print(file.readlines())

    
# import csv
# with open('MOCK_DATA.csv', mode='r') as file:
#     d = csv.reader(file)
#     for i in d:
#         print(i)
# a = " ".join(['996', 'Alli', 'Ebunoluwa', 'aebunoluwarn@google.fr', 'Female', '131.251.27.160'])
# print(a)  
# b = a.split(" ")
# print(b)   
# def a(*args, **kwargs):
#     r = {}
#     var = 0
#     for i in args:
#         var += i
#     for keys, values in kwargs.items():
#         r[keys] = values
#     return var, r

# print(a(1, 2, 6, 8 ,7, 6, 7, arg1 = "argument 1", arg2 = "argument 2", arg3 = "argument 3"))

# class p:
#     def __init__(self):
#         self.car = "mxjd"
# class c(p):
#     def __init__(self):
#         self.car2 = "sjnvcjdn"
#         super().__init__()
# s = c()
# print(issubclass(c, p))
# print(s.car)

# class a:
#     def __init__(self):
#         self.__car = "djfndj"
#     def printf(self, s):
#         print(s)
#     @property
#     def getattribute(self):
#         return self.__car
#     @getattribute.setter
#     def getattribute(self, new_car):
#         self.__car = new_car

# z = a()
# print(z.getattribute)
# z.getattribute = "Frrery"
# print(z.getattribute)

import threading
def s():
    print("laure ho tum")
def b():
    print("bhosdiwale ho tum")
t1 = threading.Thread(target=s)
t2 = threading.Thread(target=b)
# t1.start()
# t2.start()
# t1.join()
# t2.join()

# x = "sfjdenfgj"
# assert x == "sfjdenfgj"
# print(x)
class Person:
    '''
    dsdeghjerngb
    fedfgjreger
    defker
    jhfdshfuduf
    '''
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def have_birthday(self):
        self.age += 1
        print(f"Happy Birthday! I am now {self.age} years old.")

s = Person("Fuck", 56)
# print(s.__sizeof__())
# print("Fuck".swapcase())


N = int(input())
array = list(map(int, input().split(' ')))
for i in array:
    average = (sum(array)/len(array))
print(int(average))
    
    
    
