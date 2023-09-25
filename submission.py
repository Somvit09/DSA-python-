'''ques 1 - You are having an array of 5s and 7s. Modify the array to arrange 5s on left side and 7s 
on right side of the array. 
 
input - 57555775 
output- 55555777 '''

def modify(arr):
    return "".join(str(i) for i in sorted(arr))

a = '57555775'
arr = []
for i in a:
    arr.append(int(i))

print(modify(arr))

'''ques 2 - reverse the numerical array without changing the position of characters. 
 
input -  [1,2,A,8,G,3,X,M,9] 
output-  [9,3,A,8,G,2,X,M,1] '''

def reverse_array(arr):
    digits = [str(ch) for ch in arr if ch.isdigit()]
    non_digits = [ele for ele in arr if not ele.isdigit()]
    rev_ne = digits[::-1]
    rev_array = []
    di_in = 0
    for i in arr:
        if i.isdigit():
            rev_array.append(rev_ne[di_in])
            di_in += 1
        else:
            rev_array.append(i)
    return rev_array
arr = ['1','2','A','8','G','3','X','M','9']
print(reverse_array(arr))



'''
ques 4 - Given an array A[] of N positive integers which can contain integers from 0 to N where 
elements can be repeated or can be absent from the array.  
 
Your task is to count frequency of all elements from 1 to N. 
 
input- 2033445 
output- 01221 '''

def count_frequency(string):
    arr = []
    for i in string:
        arr.append(int(i))
    count_array = [0] * (max(arr) + 1)
    for i in arr:
        count_array[i] += 1
    result = "".join(str(i) for i in count_array[1:])
    return result

a = "2033445"
print(count_frequency(a))

'''
ques 6- Write a Python function called "sort_dictionary_by_value" that takes a dictionary as 
input and returns a new dictionary where the keys are the original dictionary keys sorted by their 
corresponding values in ascending order. 
 
Example: 
Input: {'a': 4, 'b': 2, 'c': 6, 'd': 1} 
Output: {'d': 1, 'b': 2, 'a': 4, 'c': 6} 
'''

def sorted_dictionary(a):
    sorted_dict = {k: v for k, v in sorted(a.items(), key=lambda item: item[1])}
    return sorted_dict

a = {'a': 4, 'b': 2, 'c': 6, 'd': 1} 
print(sorted_dictionary(a))


'''Ques 7- Write a Python function called "invert_dictionary" that takes a dictionary as input and 
returns a new dictionary where the keys and values are swapped. 
 
Example: 
Input: {'a': 1, 'b': 2, 'c': 3} 
Output: {1: 'a', 2: 'b', 3: 'c'} '''

def invert_dictionary(a):
    inverted_dictionary = {v:k for k, v in a.items()}
    return inverted_dictionary
a = {'a': 1, 'b': 2, 'c': 3}
print(invert_dictionary(a))


'''ques 3 - Reverse the whole string without reversing the individual words in it. Words are 
separated by exclamation mark. 
 
input -  I!am!a!coder 
output-  coder!a!am!I '''

def inverse_string(string):
    word = string.split("!")
    reversed_string = "!".join(word[::-1])
    return reversed_string

a = "I!am!a!coder"
print(inverse_string(a))


'''ques 5 - Given an array arr[] and a number K where K is smaller than size of array, the task is to 
find the Kth smallest element in the given array. 
 It is given that all array elements are distinct. 
 
761245 
input - k=3 
output- 4 '''



def quickselect(arr, k):
    if not arr or k <= 0 or k > len(arr):
        return None

    def partition(left, right):
        pivot = arr[right]
        i = left - 1
        for j in range(left, right):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[right] = arr[right], arr[i + 1]
        return i + 1

    def kth_smallest(left, right, k):
        if left <= right:
            pivot_index = partition(left, right)
            if pivot_index == k - 1:
                return arr[pivot_index]
            elif pivot_index > k - 1:
                return kth_smallest(left, pivot_index - 1, k)
            else:
                return kth_smallest(pivot_index + 1, right, k)

    return kth_smallest(0, len(arr) - 1, k)

# Example usage:
string = '761245'
arr = []
for i in string:
    arr.append(int(i))
k = 3
result = quickselect(arr, k)
print(result)  # Output: 4
