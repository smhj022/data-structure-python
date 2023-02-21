# Finding multiples of an number


# Simple approach

from math import sqrt
import math

num = 100
multiples = list()
multiple_count = 0
for i in range(1, num+1):
    if num % i == 0:
        multiples.append(i)
        multiple_count += 1

print(multiple_count, "-->", multiples)


# Observation approach

# lets say N = i * j

# then we can say N = i * N/i since j = N/i
#
#   if Num is 24

#     i    N/i
#     1    24
#     2    12
#     3    8
#     4    6
# ------------------- repeatation start
#     6    4
#     8    3
#     12   2
#     24   1

#  So by the following observation we can write a code as
# so max value of i is <= sqrt(N) ---> i will iterate from 1 to N
num = 100
multiple_count = 0
multiples = list()
i = 1
while i*i < num:
    if num % i == 0:
        multiple_count += 2
    i += 1

if i*i == num:
    multiple_count += 1

print(multiple_count)


# PRIME NUMBER


class Solution1:
    # @param A : long
    # @return an integer
    def solve(self, A):
        if A == 0:
            return 0
        for i in range(2, int(sqrt(A)) + 1):
            if A % i == 0:
                return 0
        return 1


# SQUARE ROOT of an number

# class Solution2:
#     def solve(self, A):
#         power()
#         return 0
