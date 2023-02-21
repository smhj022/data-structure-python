# # class Solution:
# #     # @param A : list of integers
# #     # @param B : integer
# #     # @return a list of integers
# #     def solve(A, B):

# #         import math 

# #         sub_array_size = 2 * B + 1
# #         ans_array = []

# #         center_sub_array = math.floor(sub_array_size/2)

# #         end_loop = len(A) - center_sub_array

# #         for i in range(center_sub_array, end_loop):

# #             match_count = 0
# #             center_elem = A[i]
# #             for j in range(1,center_sub_array+1):
                
# #                 if A[i + j] == A[i - j] != center_elem:
# #                     match_count += 1
# #                     center_elem = 1 - center_elem

# #             if match_count == center_sub_array:
# #                 ans_array.append(i)

# #         return ans_array


# # print(Solution.solve([ 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0 ], 2))


# # arr = [0,1,2,3,4,5,6,7,8]
# # ans = list()

# # for i in range(0, len(arr)):
# #     sub_array = list()
# #     for j in range(i,len(arr)):
# #         sub_array.append(arr[j])
# #     ans.append(sub_array)


# # print(ans)

# A = [0,1,2,3,4,5,6,7,8]

# for index in range(1, len(A)):
#     A[index] = A[index-1] + A[index]

# for start in range(len(A)):
#     for end in range(start, len(A)):

#         if start == 0:
#             sums = A[end]
#         else:
#             sums = A[end] - A[start - 1]

#         print(sums)


# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(A):

#         res = 0

#         for index in range(1,len(A)):

#             left_count = 0
#             right_count = 0

#             for left in range(index, -1, -1):

#                 if A[left] < A[index] :
#                     left_count += 1 

#             for right in range(index, len(A)):

#                 if A[right] > A[index]:
#                     right_count += 1

#             res += left_count*right_count

#         return res


# print(Solution.solve([1,2,3,4,5]))
# 

# print(1<<6, 2**6)

# class Solution:
#     # @param A : integer
#     # @param B : list of integers
#      # @return an long
#     def solve(A, B):

#         last = 0
#         ans = 0
#         for i in range(A):
#             if B[i] == 1:
#                 last = i+1
#             ans += last

#             print(i, last, ans)
#         return ans
    
# print(Solution.solve(5, [0, 1, 1, 0, 1 ]))
    

# def solve(A, B):

#     binary_str = format(int(A), 'b')
#     print(binary_str, len(binary_str) - B -1)
#     b_val = binary_str[len(binary_str) - B -1]

#     return b_val


# print(solve(13,2))

# def reverse(A):

#         res = 0
#         counter = 31

#         while (A > 0):

#             if (A & 1 == 1):

#                 res += 2 ** counter

#             counter -= 1
#             A = A >> 1

#         return res

# print(reverse(3))


# print(int(format(10,'b'),5))


# # arr = [2,4,3,7]
# arr = [6,2,3,4,5]
# p = 49
# ans = 0
# for i in range(len(arr)):
#     ans += (arr[i] * 10**(len(arr)-1-i)) % p
#     print(ans)
# print(ans%p)
    

# def expand(A, center1, center2):

#     sub_str = str()

#     while (center1 >= 0 and center2 < len(A) and A[center1] == A[center2]):

#         center1 -= 1
#         center2 += 1

#     center1 += 1
#     center2 -= 1

#     return center2 - center1 + 1 , A[center1:center2+1]

# def longestPalindrome(A):

#     n = len(A)
#     ans = A[0]
#     sub_str_len = 1

#     # for odd length sub string
#     for i in range(n):

#         center1 = i
#         center2 = i

#         length , sub_str = expand(A,center1,center2)
#         print(center1,center2, sub_str)
#         if length > sub_str_len:

#             ans = sub_str

#     # for even length substring
#     for i in range(n-1):

#         center1 = i 
#         center2 = i + 1

#         length , sub_str = expand(A,center1,center2)
#         print(center1,center2, sub_str)
#         if length > sub_str_len:

#             ans = sub_str

#     return ans

	
# print(longestPalindrome("aaaabaaa"))



# class Solution:
#     # @param A : list of integers
#     # @return an integer
#     def solve(A):

#         n = len(A)
#         pf = [0] * n

#         for i in range(n):
#             if i == 0: 
#                 pf[i] = A[i]
#             else:
#                 pf[i] = pf[i-1] + A[i]

#         res = 0
#         hashmap = dict()

#         for i in range(n):
#             if pf[i] == 0 and res < i:
#                 res = i          
#             elif pf[i] not in hashmap:
#                 hashmap[pf[i]] = i
#             else:
#                 l = i -  hashmap[pf[i]]
#                 if res < l:
#                     res = l

#         return res
    
# print(Solution.solve([ 9, -20, -11, -8, -4, 2, -12, 14, 1 ]))



# def is_pal(ch, s, e):

#     if (s>=e):
#         return

#     is_pal(ch, s+1, e-1)

#     if ch[s] != ch[e]:
#         return False
    
#     return True

# print(is_pal("daaddaad", 0,7))


# class Solution:
# 	# @param A : list of integers
# 	# @param B : integer
# 	# @return a list of integers
# 	def dNums(A, B):

#             sub_hashmap = dict()

#             for i in range(B):
#                 if A[i] not in sub_hashmap:
#                     sub_hashmap[A[i]] = 1
#                 else:
#                     sub_hashmap[A[i]] += 1


#             s = 1
#             e = B
#             n = len(A)
#             res = list()

#             res.append(len(sub_hashmap))

#             print(sub_hashmap)

#             while e < n:
#                 print(s,e)
#                 if sub_hashmap[A[s-1]] == 1:

#                     del sub_hashmap[A[s-1]]

#                 elif sub_hashmap[A[s-1]] >= 1:

#                     sub_hashmap[A[s-1]] -= 1

#                 if A[e] in sub_hashmap:

#                     sub_hashmap[A[e]] += 1
#                 else:
#                     sub_hashmap[A[e]] = 1

#                 s += 1
#                 e += 1

#                 print(res)

#                 res.append(len(sub_hashmap))

#             return res

            

# print(Solution.dNums([ 1, 2, 1, 3, 4, 3 ], 3))



# class Solution:
    # @param A : list of integers
    # # @param B : integer
    # # @return an integer
    # def solve(A, B):

    #     count = 0
    #     A_hashmap = dict()
    #     B_plus_aj = set()

    #     for i in range(len(A)):

    #         if A[i] in A_hashmap:
    #             A_hashmap[A[i]] += 1
    #         else:
    #             A_hashmap[A[i]] = 1

    #         B_plus_aj.add(B+A[i])

    #     # print(A_hashmap)
    #     # print(B_plus_aj)

    #     for elem in B_plus_aj:

    #         if elem in A_hashmap:

    #             count += A_hashmap[elem]

    #     return count

    #     return count%((10**9) + 7)     

                 


# print(Solution.solve([ 2, 1, 2, 1, 2, 1, 2, 1, 2 ], 1))


# def power(a,n):

#     if n == 0:
#         return 1
    
#     n -= 1

#     return  power(a,n) * a

# print(power(2,5))



# class Solution:
#     # @param A : list of integers
#     # @param B : integer
#     # @return a list of integers
#     def solve(A, B):

#         pf = [A[0]]

#         for i in range(1,len(A)):
#             pf.append(pf[i-1] + A[i])

#         # hashset = set()
#         print(pf)

#         for i in range(len(pf)):

#             ai = pf[i]
#             aj = B + ai
#             print(ai,aj)
#             if aj in pf:
#                 return A[i+1:pf.index(aj)+1]

#         return -1
        
# print(Solution.solve([1,2,3,4,5],5))




# strs = ["flower","flow","flight"]

# print(sorted(strs))


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashset = set()

        for elem in nums:

            if elem not in hashset:

                hashset.add(elem)

        return list(hashset)

print(Solution().removeDuplicates([1,1,2]))