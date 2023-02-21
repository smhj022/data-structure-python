
#####################################Sub Array###############################################

# Question 1: Given an array find the length of the smallest array which contains both
# max and min of array

# example [1 2 3 1 3 4 6 4 6 3] 
#  min = 1 , max = 6 , sub_array = [1 3 4 6], length = 4


# Conventional Approach 

arr = [1, 2, 3, 1, 3, 4, 6, 4, 6, 3]

min_value = min(arr)

max_value = max(arr)

n = len(arr)
ans = len(arr)

for i in range(0,n):
    if min_value == max_value:
        ans = 1
        break
    if arr[i] == min_value:
        for j in range(i,n):
            if arr[j] == max_value:
                sub_array_length = j - i + 1
                if ans > sub_array_length:
                    ans = j - i + 1
                break

    if arr[i] == max_value:
        for j in range(i,n):
            if arr[j] == min_value:
                sub_array_length = j - i + 1
                if ans > sub_array_length:
                    ans = j - i + 1
                break
    
# print(ans)

# Boss approach

arr = [1, 2, 3, 1, 3, 4, 6, 4, 6,3]

n = len(arr)
ans = len(arr)

min_value = min(arr)
max_value = max(arr)

max_value_index = -1
min_value_index = -1

for i in range(n-1,-1,-1):
    if arr[i] == max_value:
        max_value_index = i
        if min_value_index != -1:
            sub_array_length = min_value_index - max_value_index + 1
            # print(max_value_index,min_value_index,sub_array_length)
            if ans > sub_array_length:
                ans = sub_array_length

    if arr[i] == min_value:
        min_value_index = i
        if max_value_index != -1:
            sub_array_length = max_value_index - min_value_index + 1
            # print(max_value_index,min_value_index,sub_array_length)
            if ans > sub_array_length:
                ans = sub_array_length

# print(ans)


# Question 2: Find all the sub_array of an array

arr = [1,2,3,4,5,6]
sub_array = list()


for i in range(0,len(arr)):
    for j in range(i,len(arr)):
        sub = list()
        for k in range(i,j):
            sub.append(arr[k])

        sub_array.append(sub)

# print(len(sub_array))



# Question 3: print the sum of all the sub array of an array

arr = [6, 8, -1, 7]



for i in range(0,len(arr)):
    sum = 0
    for j in range(i,len(arr)):
        sum = sum + arr[j]
        
        # print(sum)



# arr_ = [3,8,4,7,9,4,3,2,10,6]

# sum = 0

# for i in range(3,len(arr_)):
#     sum = sum + arr_[i]
#     print(sum)


# Question 4: print the sum of all the sub arrays sum of an array

# Ye hai aam zindagi

arr = [6, 8, -1, 7]
ans = 0

for i in range(0,len(arr)):
    sum = 0
    for j in range(i,len(arr)):
        sum = sum + arr[j]
        ans = ans + sum
    
# print(ans)

# ye hai mentos zindagi

arr = [6, 8, -1, 7]

# Observation : As we need to find the sum of all the sub arrays all the no of an array added multiple
# times. so we need to find how many no of times the no. is added to get the sum.

# let as observe the no. of time different indices no. added in the above array.

# #  sub arrays that include indices position 0 are:

# [0] [0,1] [0,1,2] [0,1,2,3] -> 4 times

#  sub arrays that include indices position 1 are:
# 
# [1] [1,2] [1,2,3] [0,1] [0,1,2] [0,1,2,3] -> 6 times

#  sub arrays that include indices position 2 are:

# [1,2] [1,2,3] [0,1,2] [0,1,2,3] [2] [2,3] -> 6 times

# #  sub arrays that include indices position 3 are:

# [0,1,2,3] [1,2,3] [2,3] [3] -> 4 times

# from observation we can find (i + 1) * (n - i) where n is length of an array


# code

n = len(arr)
sum = 0

for i in range(0,len(arr)):
    sum = sum + arr[i] * (i + 1) * (n - i)

# print(sum)



# You are given an array A of length N and Q queries given by the 2D array B of size Q*2. Each 
# query consists of two integers B[i][0] and B[i][1].
# For every query, the task is to find the count of even numbers in the range A[B[i][0]…B[i][1]].

arr = [2, 1, 8, 3, 9]
query_arr = [[0,3], [2,4]]

count = 0

for i in range(0, len(arr)):
    if arr[i]%2 == 0:
        count += 1
    arr[i] = count 

print(arr)
ans = []

for query in query_arr:
    left = query[0]
    right = query[1]
    print(left,right)
    
    if left == right:
        ans = 0
    
    if left==0:
        ans.append(arr[right])
    else:
        ans.append(arr[right]-arr[left-1])

print(ans)
