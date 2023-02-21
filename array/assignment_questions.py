###############################  Carry Forward ###############################


# Question 1:

# You have given a string A having Uppercase English letters.

# You have to find how many times subsequence "AG" is there in the given string.

# NOTE: Return the answer modulo 109 + 7 as the answer can be very large.


class Sequence_count:

    def solve(A):

        A_length = len(A)

        g_count = 0
        ans_count = 0

        for i in range(A_length-1, -1, -1):
            
            if A[i] == "G":
                g_count += 1
            
            if A[i] == "A":
                ans_count = ans_count + g_count 

        return(ans_count)


# print(Sequence_count.solve("GAB"))



# Question 2:

# Given an integer array A containing N distinct integers, you have to find all the leaders in array A.

# An element is a leader if it is strictly greater than all the elements to its right side.

# NOTE:The rightmost element is always a leader.


class Leader:

    def solve(A):

        A_length = len(A)
        max_num = A[A_length-1]
        leaders = [max_num]

        for i in range(A_length-2, -1, -1):

            if A[i] > max_num:
                leaders.append(A[i])
                max_num = A[i]
        return leaders


# print(Leader.solve( A = [1, 2]))



# Question 3

# Given an array A, find the size of the smallest sub array such that it 
# contains at least one occurrence of the maximum value of the array
# and at least one occurrence of the minimum value of the array.

class MinMax:

    def solve(A):

        min_elem = A[0]
        max_elem = A[0]

        for elem in A:

            if elem < min_elem:
                min_elem = elem

            if elem > max_elem:
                max_elem = elem

        if max_elem == min_elem:
            return 1
            
        print(min_elem, max_elem)

        max_ind = -1
        min_ind = -1
        ans = len(A)

        for i in range(len(A)-1,-1,-1):

            if A[i] == max_elem:
                max_ind = i
                print(max_ind)
                if min_ind != -1:
                    ans = min_ind - max_ind + 1 

            if A[i] == min_elem:
                min_ind = i
                print(min_ind)
                if max_ind != -1:
                    ans = max_ind - min_ind + 1 

        return ans


# print(MinMax.solve(A=[2]))

# Question 4


# A wire connects N light bulbs.
# Each bulb has a switch associated with it; however, due to faulty wiring, 
# a switch also changes the state of all the bulbs to the right of the current bulb.

# Given an initial state of all bulbs, find the minimum number of switches
#  you have to press to turn on all the bulbs.
# You can press the same switch multiple times.

# Note: 0 represents the bulb is off and 1 represents the bulb is on.


class Bulb:

    def solve(A):
        
        switch_count = 0
        on_count = 0

        for i in range(1,len(A)-1):
            if A[i] == 1:
                on_count += 1

        if on_count == len(A) or len(A) ==0:
            return 0

        bulb_state = A[0]

        for i in range(1,len(A)):

            if bulb_state != A[i]:
                bulb_state = A[i]
                switch_count += 1
        
        if A[0] == 0:
            switch_count = switch_count + 1

        return switch_count

# print(Bulb.solve(A=[0,1]))



# Question 5


# You are given an integer array A of size N.

# You have to pick B elements in total. Some (possibly 0) elements from left end of array
#  A and some (possibly 0) from the right end of array A to get the maximum sum.

# Find and return this maximum possible sum.

# NOTE: Suppose B = 4, and array A contains 10 elements, then

# You can pick the first four elements or can pick the last four elements, or can pick 1 
# from front and 3 from the back, etc. You need to return the maximum possible sum of 
# elements you can pick.



class BothSide:

    def solve(A,B):
        n = len(A)
        pf = [0] * n
        sf = [0] * n

        for i in range(0, n):

            if i == 0:
                pf[i] = A[i]
                sf[n-1-i] = A[n-1-i]
            else:
                pf[i] = A[i] + pf[i-1]
                sf[n-1-i] = A[n-1-i] + sf[n-i]

        perf_sum = pf[B-1]
        suf_sum = sf[n-B]

        ans = max(perf_sum,suf_sum)
        # print(ans)

        for i in range(0,B):

            start_elem_count = i
            end_elem_count = B - i

            if start_elem_count == 0:
                total_sum = sf[n-B]
                # print(start_elem_count,end_elem_count,total_sum)

            else:
                perf_sum = pf[i-1]
                suf_sum = sf[n-end_elem_count]
                total_sum = perf_sum + suf_sum
                # print(i-1,n-end_elem_count)
                # print(start_elem_count,end_elem_count,perf_sum,suf_sum,total_sum)

            ans = max(ans, total_sum)

        return ans

# print(BothSide.solve([1,2,3,4,5],3))


# Given an array of integers A, a sub array of an array is said to be good if it 
# fulfills any one of the criteria:
# 1. Length of the sub array is be even, and the sum of all the elements of the sub array 
# must be less than B.
# 2. Length of the sub array is be odd, and the sum of all the elements of the sub array 
# must be greater than B.

# Your task is to find the count of good sub arrays in A.



arr = [13, 16, 16, 15, 9, 16, 2, 7, 6, 17, 3, 9]
b = 65
n = len(arr)
# pf arr of the array
pf = [0] * n
ans = 0

class ConditionalSubArrayCount:
    def solve(arr,b):
        for i in range(n):
            if i == 0:
                pf[i] = arr[i]
            else:
                pf[i] = pf[i-1] + arr[i]


        for i in range(n):
            summ = 0
            for j in range(i, n):
                
                if i == 0:
                    summ = pf[j]
                else:
                    summ = pf[j] - pf[i-1]

                if (i-j+1)%2 == 0 and summ < b:
                    ans += 1
                elif (i-j+1)%2 != 0 and summ > b:
                    ans += 1

        return ans

        
# ####################### 2D Array Questions ############################

# Question 1
# You are given a 2D integer matrix A, return a 1D integer array containing 
# column-wise sums of original matrix.
# mat = [[1,2,3,4],[5,6,7,8],[9,2,3,4]]  => [15, 10, 13, 16]

class ColumnSum:

    def solve(mat):

        ans = [0] * len(mat[0])
        for row in range(len(mat)):

            for elem_i in range(len(mat[0])):

                ans[elem_i] += mat[row][elem_i]

        return ans

print(ColumnSum.solve(mat = [[1,2,3,4],[5,6,7,8],[9,2,3,4]])) 


# Question 2
# Give a N * N square matrix A, return an array of its anti-diagonals. 
# Look at the example for more details.

# mat = [[1,2,3],
#        [4,5, 6],
#        [7,8,9]]
# return =  [1 0 0
#            2 4 0
#            3 5 7
#            6 8 0
#            9 0 0]


class AntiDiagonal:
    def solve(mat):
        ans = list()
        for j in range(len(mat[0])):
            i=0
            dia_array = [0] * len(mat)
            while j >= 0:
                dia_array[i] = mat[i][j]
                i+=1
                j-=1

            ans.append(dia_array)


        for i in range(1,len(mat)):
            j=len(mat[0])-1
            k=0
            dia_array = [0] * len(mat)
            while i < len(mat[0]):
                dia_array[k] = mat[i][j]
                i+=1
                j-=1
                k+=1

            ans.append(dia_array)

        return ans

# print(AntiDiagonal.solve([[1,2,3],[4,5,6],[7,8,9]]))

                

######################################Sliding Windows #############################


# Question 1:

# Given an array A of length N. Also given are integers B and C.

# Return 1 if there exists a subarray with length B having sum C and 0 otherwise


class SubArraySum:

    def solve(A,B,C):
        
        summ = 0
        for i in range(0,B):
            summ += A[i]

        if summ == C:
            return 1

        for i in range(1, len(A)-B+1):
            # print(i, i+B-1)
            summ = summ - A[i-1] + A[i+B-1]
            # if summ == C:
            #     return 1

        return 0

# print(SubArraySum.solve([4,3,2,6],2,5))


# Question 2:

# Given an integer A, generate a square matrix filled with elements 
# from 1 to A2 in spiral order and return the generated square matrix.

class SpiralArrayFromNum:

    def solve(A):

        spiral_mat = [[0]*A for i in range(A)]

        count = 1
        row = 0
        col= 0

        while A > 1:

            for i in range(A-1):
                
                spiral_mat[row][col] = count
                col += 1
                count += 1

            for i in range(A-1):
                
                spiral_mat[row][col] = count
                row += 1
                count += 1

            for i in range(A-1):

                spiral_mat[row][col] = count
                col -=1
                count += 1

            for i in range(A-1):

                spiral_mat[row][col] = count
                row -= 1
                count += 1
            print("hello")
            A -= 2
            row += 1
            col += 1

            if A == 1:
                spiral_mat[row][col] = count


        return spiral_mat

print(SpiralArrayFromNum.solve(5))