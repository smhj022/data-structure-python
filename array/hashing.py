
class Hashing:

    def count_occurance(arr):

        res_dict = dict()

        for i in range(len(arr)):

            if not arr[i] in res_dict.keys():

                res_dict[arr[i]] = 1

            else:

                res_dict[arr[i]] += 1

        return res_dict
    
# print(Hashing.count_occurance([1,1,1,1,2,2,3,2,3,]))

# Problem Description
# Given an array A. You have some queries given by the array B.

# For the i-th query, find the frequency of B[i] in the array A.

class Solution1:

    def frequency_count(A,B):

        freq_dict = Hashing.count_occurance(A)

        res = list()

        for i in B:

            if i not in freq_dict.keys():

                res.append(0)

            else:

                res.append(freq_dict[i])

        return res
    
# print(Solution1.frequency_count([1, 2, 1, 1], [1,2]))


# Good Question: Given an integer array A of size N, find the first repeating element in it.

# We need to find the element that occurs more than once and whose index of the 
# first occurrence is the smallest.

# If there is no repeating element, return -1.


class Solution2:

    def first_repeating_element(A):
    
        elem_set = set()

        res = -1

        for i in range(len(A)-1,-1,-1):

            if A[i] not in elem_set:

                elem_set.add(A[i])

            else:
                res = A[i]
            
        print(elem_set)
            
        return res
    


print(Solution2.first_repeating_element([10, 3, 5, 4, 3, 5, 6]))


# Good Question
# Question:Given an array of integers A, find and return whether the given array contains a 
# non-empty subarray with a sum equal to 0.

# If the given array contains a sub-array with sum zero return 1, else return 0.


class Solution3:

    def find_non_empty_sa(A):


        pf_arr = [0] * len(A)

        for i in range(len(A)):
            if i == 0:
                 pf_arr[i] = A[i]
            else:
                pf_arr[i] = pf_arr[i-1] + A[i]

        hash_set = set()
        print(pf_arr)

        for i in range(len(A)):
            if pf_arr[i] == 0:
                return 1
            elif not pf_arr[i] in hash_set:
                hash_set.add(pf_arr[i])
            else:
                return 1
            
        return 0
    
print(Solution3.find_non_empty_sa([-1,1]))


# Question: Given an array A of N integers.
# Find the length of the longest subarray in the array which sums to zero.


class Solution4:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):

        n = len(A)
        pf = [0] * n

        for i in range(n):
            if i == 0: 
                pf[i] = A[i]
            else:
                pf[i] = pf[i-1] + A[i]

        res = 0
        hashmap = dict()

        for i in range(n):

            if pf[i] == 0 and res < i:
                # special case as there is 0 in pf array
                res = i + 1        
            elif pf[i] not in hashmap:
                # value is first occurance 
                hashmap[pf[i]] = i
            else:
                # diff between start and end occurance
                s = hashmap[pf[i]]
                e = i
                l = s - e
                if res < l:
                    res = l
        return res
        

# Question 5: Given an Array of integers B, and a target sum A.
# Check if there exists a pair (i,j) such that Bi + Bj = A and i!=j.

# A = 8   B = [3, 5, 1, 2, 1, 2] return 1
# A = 21   B = [9, 10, 7, 10, 9, 1, 5, 1, 5] return 0


class Solution5:
    # @param A : integer
    # @param B : list of integers
    # @return an integer
    def solve(self, A, B):

        B_hashmap = dict()

        for i in range(len(B)):

            if B[i] not in B_hashmap:
                B_hashmap[B[i]] = 1
            else:
                B_hashmap[B[i]] += 1

        
        for i in range(len(B)):

            bi = B[i]
            bj = A - bi

            if bi == bj and B_hashmap[bj] >= 2:
                return 1

            elif bi != bj and bj in B_hashmap:
                return 1

        return 0
    

# Question 6 : You are given an array of N integers, A1, A2 ,..., AN and an integer B. Return the of count of distinct numbers in all windows of size B.

# Formally, return an array of size N-B+1 where i'th element in this array contains number of distinct elements in sequence Ai, Ai+1 ,..., Ai+B-1.

# NOTE: if B > N, return an empty array.


class Solution:
	# @param A : list of integers
	# @param B : integer
	# @return a list of integers
	def dNums(self, A, B):
            
            sub_hashmap = dict()

            for i in range(B):
                if A[i] not in sub_hashmap:
                    sub_hashmap[A[i]] = 1
                else:
                    sub_hashmap[A[i]] += 1


            s = 1
            e = B
            n = len(A)
            res = list()

            res.append(len(sub_hashmap))

            while e < n:

                if sub_hashmap[A[s-1]] == 1:

                    del sub_hashmap[A[s-1]]

                elif sub_hashmap[A[s-1]] >= 1:

                    sub_hashmap[A[s-1]] -= 1

                if A[e] in sub_hashmap:

                    sub_hashmap[A[e]] += 1
                else:
                    sub_hashmap[A[e]] = 1

                res.append(len(sub_hashmap))

                s += 1
                e += 1

            return res

            
