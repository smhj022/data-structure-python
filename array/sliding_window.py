# SLIDING WINDOW
# 
# If the length of an array is N then the first sub array of length K will be : [0, K-1]

#  and the last sub array will be: [N-K, N-1]


# Question: Find the sum of all the sub array of length K in an array of size N

arr = [1,2,3,4,5,6,7,8]

k = 3
n = len(arr)
start_ind = 0
end_ind = k-1

# n is length and end_ind is indices so we need to run while loop until
# end_ind is less then the n(length) if length is 5 then we need to stop at 4
while end_ind < n:
    sum = 0
    # end_ind + 1 because we need to go to end_ind
    for i in range(start_ind, end_ind+1):
        sum = sum + arr[i]
    # print(sum)
    
    start_ind += 1
    end_ind += 1


# Prefix Sum approach

arr = [1,2,3,4,5,6,7,8]

k = 3
n = len(arr)
start_ind = 0
end_ind = k-1

def pf(arr):
    pf_arr = [0] * len(arr)
    for i in range(1,len(arr)):
        pf_arr[i] = pf_arr[i-1] + arr[i] 
    return pf_arr

pf_arr = pf(arr=arr)

while end_ind < n:
    if start_ind == 0:
        pass
        # print(pf_arr[end_ind])
    else:
        pass
        # print(pf_arr[end_ind]-pf_arr[start_ind-1])
    start_ind += 1
    end_ind += 1

    # print(sum)

# Carry Forward approach

arr = [1,2,3,4,5,6,7,8]

k = 3
n = len(arr)
start_ind = 0
end_ind = k-1
sum = 0

for i in range(0, k):
    sum += arr[i]

# print(sum)

while end_ind < n-1:
    sum = sum - arr[start_ind] + arr[end_ind+1]

    # print(sum)
    start_ind += 1
    end_ind += 1

    


# Question 2: Given an array and integer B find the swaps required to bring all the number 
# which is less than or equal to B together

arr = [1,12,10,3,14,10,7]
# arr = [5,17,100,11]
b = 8
n = len(arr)
swap = n
sub_array_size = 0

for i in range(0, len(arr)):
    if arr[i] <= b:
        sub_array_size += 1


start_ind = 0
end_ind = sub_array_size - 1

while end_ind < n:
    swap_count = 0
    for i in range(start_ind, end_ind+1):
        if arr[i] > b:
            swap_count += 1
    if swap > swap_count:
        swap = swap_count
    
    start_ind += 1
    end_ind += 1
    
# print(swap)

# Sliding window approach

# arr = [1,12,10,3,14,10,7]
 # arr = [5,17,100,11]
# b = 8

arr = [8,3,10,20,22,13,1,2,55,5,15]
b = 5
n = len(arr)
swap = n
sub_array_size = 0

for i in range(0, n):
    if arr[i] <= b:
        sub_array_size += 1

start_ind = 0
end_ind = sub_array_size - 1
swap = 0

for i in range(0, end_ind+1):
    if arr[i] > b:
        swap += 1

start_ind += 1
end_ind += 1
ans = swap

while end_ind < n:
    if arr[start_ind-1] > b:
        swap -= 1
    if arr[end_ind] > b:
        swap += 1
    if ans > swap:
        ans = swap

    start_ind += 1
    end_ind += 1

# print(ans)



# Assignment Question: Find the sub array that has least average. we need to print the index of 
# sub array that has least average among all the sub array.


arr = [3,7,90,20,10,50,40]
b = 3
n = len(arr)
start_ind = 0
end_ind = b - 1

sum = 0

for i in range(0, b):
    sum += arr[i]

least_sum = sum
least_ind = 0 

start_ind += 1
end_ind += 1


while end_ind < n:
    sum = sum + arr[end_ind] - arr[start_ind-1]
    if sum < least_sum:
        least_sum = sum
        least_ind = start_ind + 1
    
    start_ind += 1
    end_ind += 1

# print(least_sum/b)
# print(least_ind)

# ########################################################################################


## Interview Problems ##

# Question: Given an binary array, we can at most replace a single 0 to 1.
# Find the max length of consecutive 1's in the array.

# Example:  arr = [1,1,1,0,1,1,0,1]

# replace 1st 0 to 1 then --> max length of one will become 6
# replace 2nd 0 to 1 then --> max length of one will become 4 

# ans will be max(6,4) --> 6

arr = [0,1,1,1,0,1,1,0,0]

length_size = 0
ans = 0
count_1 = 0

# counting the no of 1's in the array
for i in range(0, len(arr)):
    if arr[i] == 1:
        count_1 += 1

# if all elements are 1's then return length of the array
if count_1 == len(arr):
    print(len(arr))
else:
    for i in range(0, len(arr)):

        if arr[i] == 0:

            right_sum = 0
            left_sum = 0

            # counting 1's on right
            for j in range(i+1, len(arr)):
                if arr[j] == 0:
                    break
                right_sum += 1

            # counting 1's on left
            for k in range(i-1, -1, -1):
                if arr[k] == 0:
                    break
                left_sum += 1
            
            # print(i,right_sum,left_sum)

            length_size = right_sum + left_sum + 1

            if ans < length_size:
                ans = length_size

    # print(ans)


# PART 2: in the above question instead of replace we can only swap a 0 with 1


arr = [0,1,1,1,0,1,1,0,0]

length_size = 0
ans = 0
count_1 = 0

# counting the no of 1's in the array
for i in range(0, len(arr)):
    if arr[i] == 1:
        count_1 += 1

# if all elements are 1's then return length of the array
if count_1 == len(arr):
    print(len(arr))
else:
    for i in range(0, len(arr)):

        if arr[i] == 0:

            right_sum = 0
            left_sum = 0

            # counting 1's on right
            for j in range(i+1, len(arr)):
                if arr[j] == 0:
                    break
                right_sum += 1

            # counting 1's on left
            for k in range(i-1, -1, -1):
                if arr[k] == 0:
                    break
                left_sum += 1

            length_size = right_sum + left_sum + 1

            # in case of swap
            if count_1 < length_size:
                length_size -= 1 

            if ans < length_size:
                ans = length_size

    # print(ans)



# question 3: Given a[N] elements, calculate the no. of triplets i,j,k such that
# i<j<k and a[i] < a[j] < a[k] 

# for example = > a = [2 6 9 4 10]

# no. of triplets 1)  2,6,9
#                 2)  2,6,10
#                 3)  2,4,10 
#                 4)  2,9,10
#                 5)  6,9,10
# 

# Aam zindagi
# 

arr = [2,6,9,4,10]
n=len(arr)
triplets_count = 0

for i in range(0,n-2):
    for j in range(i,n-1):
        for k in range(j,n):
            if arr[i]<arr[j] & arr[j]<arr[k]:
                triplets_count += 1

print(triplets_count)


# mentos zindagi

arr = [2,6,9,4,10]
n=len(arr)
triplets_count = 0

for i in range(0, n):

    right_count=0
    left_count=0

    for j in range(i, n):
        if arr[i] < arr[j]:            
            right_count += 1

    for k in range(i,-1,-1):
        if arr[i] > arr[k]:
            left_count += 1

    triplets_count = triplets_count + left_count*right_count 
  
print(triplets_count)


# Interview Problem 2:

# ***Question*** : Given an array we need to find the count of all the special indices such that on deleting
# the special indices the sum of odd indices elements is equal to the even position indices. 

arr = [4, 3, 2, 7, 6, -2]
n = len(arr)
even_pf_arr = [0] * n
odd_pf_arr = [0] * n 
count = 0

# for loop to find pf sum array for odd and even position
# 
#  even_pf_arr = [4, 4, 6, 6, 12, 12]
#  odd_pf_arr = [0, 3, 3, 10, 10, 8]
for i in range(0, n):
    if i%2 == 0:
        even_pf_arr[i] = even_pf_arr[i-1]+arr[i]
        odd_pf_arr[i] = odd_pf_arr[i-1]
    else:
        even_pf_arr[i] = even_pf_arr[i-1]
        odd_pf_arr[i] = odd_pf_arr[i-1]+arr[i]
        
# In this for loop we are finding the sum of odds and evens indices
# Logic : As after deleting the indices after the deleted indices 
# the position of odd and even will change

# In this loop we are iterating and deleting the i and finding the sum of odd 
# and even position indices
for i in range(0, len(arr)):

    odd_sum = 0
    even_sum = 0

    # handling edge case 
    if i == 0:
        even_sum = odd_pf_arr[n-1] - odd_pf_arr[i]
        odd_sum = even_pf_arr[n-1] - even_pf_arr[i]
    else:
        # odd sum equal to sum of odd indices before the deleted indices and 
        # even indices after the deleted indices
        odd_sum = odd_pf_arr[i-1] + even_pf_arr[n-1] - even_pf_arr[i]

        # even sum equal to sum of even indices before the deleted indices and 
        # odd indices after the deleted indices
        even_sum = even_pf_arr[i-1] + odd_pf_arr[n-1] - odd_pf_arr[i]

    # if even and odd sum are equal we count.
    if even_sum == odd_sum:
        count += 1
        print(i)


print(count)
