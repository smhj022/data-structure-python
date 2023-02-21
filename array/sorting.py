# Question 1 : Noble Integer [data is distinct]

# Given N elements in an array calculate no. of nobel integer.
# An element in an array is said to be nobel if 
#    No. of element < element = element itself

#  Example = [-1 -5 3 5 -10 4]
#            [ 2  1 3 5   0  4] ==> count of no. of element less than the element itself

# here 3,5 and 4 are the nobel element

def find_noble_dist(arr):

    arr.sort(reverse = False)
    ans = 0
    for i in range(len(arr)):
        if arr[i] == i:
            ans += 1

    return ans

# print(find_noble_dist([-1, -5, 3, 5, -10, 4]))

# Question 2: In the above question [data can repeat] 

def find_noble(arr):

    arr.sort(reverse = False)
    ans = 0
    pre_elem = 0
    pre_same_elem_count = 0

    if arr[0] == 0:
        ans += 1
        pre_elem_count = 1

    for i in range(1,len(arr)):
        if arr[i-1] == arr[i]:
            if arr[i] == i - pre_elem_count:
                ans += 1
            pre_same_elem_count += 1
        elif arr[i] == i:
            ans += 1
            pre_same_elem_count = 1
    return ans

# print(find_noble([0,0,2,2,5,5,5,5,8,8,10,10,10,14]))

# [-10,1,1,1,4,4,4,7,10]


# ################################################################################################

############################ ASSIGNMENT QUESTIONS ################################################   

# Given an array A of N integers. Sort the array in increasing order of the value at the tens 
# place digit of every number.

# If a number has no tens digit, we can assume value to be 0.
# If 2 numbers have same tens digit, in that case number with max value will come first
# Solution should be based on comparator.


def sort_tens_place(arr):
    import math

    for i in range(len(arr)):

        arr[i] = math.floor((arr[i]%100)/10)

    print(arr)
    
    for i in range(1, len(arr)):
        for j in range(1, len(arr)):

            if arr[j-1] > arr[j]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp

    return(arr)


print(sort_tens_place([10, 12, 68, 34, 91]))

print(chr(65))

x = "A"
print(65^(1<<5))