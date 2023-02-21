
# Question: find the count of numbers that dont not have a number greater than himself

arr = [1, 2, 4, 3, 7, 5, -2, 0, 7, 3, 5, 4, 7]

max = arr[0]
max_count = 0

for num in arr:
    if num > max:
        max = num
        max_count = 1
    elif num == max:
        max_count += 1

print(max_count)
print(max)

print(len(arr)-max_count)


# Question 2 : Find the count of pair (i , j) where i, j  are the indices of an array and i is always 
# less than j such that arr[i] + arr[j] = K where K is a given number.

arr = [3, 5, 2, 1, -3, 7, 8, 15, 6, 13]
count = 0
K = 10
iter = 0

for I in arr:
    for J in arr[iter+1:]:
        if I + J == K:
            count += 1
        print(I, J)
    iter += 1
    

print(f"Count of pair (i,j) is {count}")


# Question : Reverse the given array without using extra spaces

# with extra space
arr = [1, 2, 3, 4]
rev_arr = list()
print(len(arr))

for i in range(1, len(arr)+1):
    rev_arr.append(arr[len(arr)-i])

print(rev_arr)


# Without extra space
import math

arr = [1, 2, 3, 4, 5, 6, 7]

# Reverse function of an array
def reverse(array, start=0, end=len(arr)-1):
    # first element of an array
    i = start
    # last element of an array
    j = end

    while (i <= j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i += 1
        j -= 1
    
    return arr

print(f"The reverse array is: {reverse(arr)}")

for i in range(0, math.floor(len(arr)/2)):
    arr[i] = arr[i] + arr[len(arr)-i-1]
    arr[len(arr)-i-1] = arr[i] - arr[len(arr)-i-1]
    arr[i] = arr[i] - arr[len(arr)-i-1]

print(arr)


# Question : Rotate the array k times (given) clockwise 

# Approach 1

arr = [1, 2, 3, 4, 5]
k=3
n = len(arr)
new_arr = [0] * n

print(n)

for i in range(0, len(arr)):
    j = (i+k)%len(arr)
    new_arr[j] = arr[i]

print(new_arr)

# Approach 2

# TODO


# Homework Question 1 : Given an array A and an integer B, find the number of occurrences of B in A.


arr = [1, 2, 5, 2, 6, 2]

k = 2



def findCountInArray(array, num):
    count = 0
    for elem in array:
        if elem == k:
            count += 1

    return count

print(findCountInArray(arr, K))

# Find Second largest element of an array

# arr = [2,3,6,1,4,7,4,12,4,33]

# largest = arr[0]

# for elem in arr[1:]:
    


