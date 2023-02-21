# prefix sum

# Concept of Brute Force

# For a given array A we need to find the sum of all the elements between 
# L to R defined in Query Array Q.

arr = [1, 3, -5, 6, 2, 1, 5, 4, 7, 12, 4, 5, -4]

Q = [[2,4], [5,7], [1,9], [0, 12], [7,7]]

def cumulative_array(arr):
    cum_sum = arr[0]
    cum_array = []
    cum_array.append(cum_sum)

    for i in range(1,len(arr)):
        cum_sum = cum_sum + arr[i]
        cum_array.append(cum_sum)
    return cum_array

print(cumulative_array([1,2,3,4]))


def solve(arr, q_arr):

    cum_array = cumulative_array(arr)
    print(cum_array)
    q_ans = []
    for q in q_arr:
        print(cum_array[q[1]], cum_array[q[0]])
        if q[0] == 0:
            q_ans.append(cum_array[q[1]])
        else:
            q_ans.append(cum_array[q[1]] - cum_array[q[0]-1]) 

    return q_ans

print(solve(arr,Q))



# # Equilibrium Index
# 

eqi_arr = [-3,2,4,-1]


def find_equilibrium_count(arr):
    eqi_count = 0

    for i in range(0, len(arr)):
    
        cum_arr = cumulative_array(arr)

        if i == 0:
            left_sum = 0
        else:
            left_sum = cum_arr[i-1]
        
        if i == len(arr)-1:
            right_sum = 0
        else:
            right_sum = cum_arr[len(arr)-1] - cum_arr[i]

        if right_sum == left_sum:
            eqi_count += 1
        
    return eqi_count

print(find_equilibrium_count(arr=eqi_arr))
 


# Question: Given an array A and Query Q [L,R], we need to find the number of even numbers between
# L ans R

arr = [2, 4, 3, 7, 9, 8, 6, 5, 4, 9]

Q_query = [[2,4], [5,7], [1,9], [7,7], [0,9]]

def find_even_odd(arr):
    oe_arr = []
    for num in arr:
        if num%2 == 0:
            oe_arr.append(1)
        else:
            oe_arr.append(0)
    return oe_arr

def solve_3(arr, Q_query):

    pf_arr = find_even_odd(arr)
    q_ans = []
    cum_pf_arr = cumulative_array(pf_arr)

    print(pf_arr)
    print(cum_pf_arr)
    for q in Q_query:
        if q[0] == 0:
            q_ans.append(cum_pf_arr[q[1]])
        else:
            q_ans.append(cum_pf_arr[q[1]] - cum_pf_arr[q[0]-1]) 

    return q_ans

print(solve_3(arr, Q_query))



# Assignment

# Given an array of integers A, find and return the product array of the same size where the ith 
# element of the product array will be equal to the product of all the elements divided by the 
# ith element of the array.

# Note: It is always possible to form the product array with integer (32 bit) values. 
# Solve it without using the division operator.

# arr = [1, 2, 3, 4, 5]
arr = [5,1,10,1]

def assign(arr):

    n = len(arr)
    pf = [0] * n
    sf = [0] * n

    pf[0] = arr[0]
    sf[n-1] = arr[n-1] 

    for i in range(1,n):

        pf[i] = arr[i] * pf[i-1]
        sf[n-1-i] = arr[n-1-i] * sf[n-i]

    print(pf)
    print(sf)


    m_array = [0] * n

    m_array[0] = sf[1]
    m_array[n-1] = pf[n-2]

    for i in range(1,n-1):

        m_array[i] = pf[i-1] * sf[i + 1]

    return m_array

print(assign(arr=arr))
