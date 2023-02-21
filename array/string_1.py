# Question 1: Longest Substring array *******


# Given a string A of size N, find and return the longest palindromic substring in A.

# Substring of string A is A[i...j] where 0 <= i <= j < len(A)

# Palindrome string:
# A string which reads the same backwards. More formally, A is palindrome if reverse(A) = A.
# Incase of conflict, return the substring which occurs first ( with the least starting index).

class Solution:
	# @param A : string
	# @return a strings

	def expand(self, A, center1, center2):

		sub_str = str()

		while (center1 >= 0 and center2 < len(A) and A[center1] == A[center2]):

			center1 -= 1
			center2 += 1

		return center2 - center1 - 1 , A[center1+1:center2]

	def longestPalindrome(self, A):

		n = len(A)
		ans = A[0]
		sub_str_len = 1

		# for odd length sub string
		for i in range(n):

			center1 = center2 = i

			length , sub_str = self.expand(A,center1,center2)

			if length > sub_str_len:

				ans = sub_str
				sub_str_len = length

		# for even length substring
		for i in range(n-1):

			center1 = i 
			center2 = i + 1

			length , sub_str = self.expand(A,center1,center2)

			if length > sub_str_len:

				ans = sub_str
				sub_str_len = length

		return ans
	

# print(Solution().longestPalindrome("aaabaaabaa"))


# Question 3: Function to_lower

# You are given a function to_lower() which takes a character array A as an argument.

# Convert each character of A into lowercase characters if it exists. If the lowercase of a character does not exist, it remains unmodified.
# The uppercase letters from A to Z are converted to lowercase letters from a to z respectively.

# Return the lowercase version of the given character array.



class Solution:
    # @param A : list of characters
    # @return a list of characters
    def to_lower(self, A):
	    
        for i in range(len(A)):
            
            order_val = ord(A[i])
            if 65 <= order_val <= 90:
		    
                A[i] = chr(ord(A[i])^(1<<5))
		
        return A

print(Solution().to_lower(["a"]))
