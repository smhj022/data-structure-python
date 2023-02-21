def learn_recursion(N):

    if N <= 0:
        return 0
    learn_recursion(N-1)
    print(N)
    return ""


print(learn_recursion(5))


class Solution():
    # @param A : integer
    # @param B : integer
    # @return an integer
    def power(self, A, B):

        if B == 1 or A == 1:
            return A

        return A * self.power(A, B-1)


print(Solution().power(2, 3))
