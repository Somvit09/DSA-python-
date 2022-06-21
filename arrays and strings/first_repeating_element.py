def firstRepeated(arr, n):
    max_ = max(arr)

    temp = [0 for i in range(max_ + 1)]  # the idea is to use
    # temporary array as hashmap
    # Arrays.fill(temp, 0);

    for x in range(n):
        num = arr[x]
        temp[num] += 1

    for x in range(n):
        num = arr[x]
        if temp[num] > 1:
            return x+1

    return -1

arr = [1, 5, 3, 4, 3, 5, 6]
n = 7
print(firstRepeated(arr, n))