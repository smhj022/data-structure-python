# Carry Forward


# Question 1: Find the count of pair of a and g in a char array such that
# ṭhe indices i<j 

# Example:  array = [a,g,e,s,a,g,s,g,m]

# pair = (0,1) (0,5) (0, 7) (4,5) (4,7)


char_arr = ["a","d","g","a","g","a","g","f","g"]

pair_count = 0
g_count = 0

for i in range(len(char_arr)-1, -1, -1):
    
    if char_arr[i] == "g":
        g_count += 1

    if char_arr[i] == "a":
        pair_count = pair_count + g_count

# print(pair_count)


# Question 2: Find the count of leader in an array.
# Leader -> A Leader is such it should be greater than all the elements on its right.
#  So the last element is always a leader

leader_array = [15, -1, 7, 2, 5, 4, 2, 3]

leader_count = 1
curr_leader = leader_array[len(leader_array)-1]

for i in range(len(leader_array)-2, -1, -1):
    if leader_array[i] > curr_leader:
        leader_count += 1
        curr_leader = leader_array[i]

# print(leader_count)


# Question 3: Given an array find the length of the smallest array which contains both
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
            print(max_value_index,min_value_index,sub_array_length)
            if ans > sub_array_length:
                ans = sub_array_length

    if arr[i] == min_value:
        min_value_index = i
        if max_value_index != -1:
            sub_array_length = max_value_index - min_value_index + 1
            print(max_value_index,min_value_index,sub_array_length)
            if ans > sub_array_length:
                ans = sub_array_length

print(ans)

