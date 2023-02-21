
class Reverse:

    def reverse(arr, start, end):
        # first element of an arr
        i = start
        # last element of an arr
        j = end

        while (i <= j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
        
        return arr



reversed_array = Reverse.reverse([1,2,3,4,5], 0, 4)
# print(reversed_array)


# Question based on reverse array -> an array A and a integer B we need to rotate the array by integer B
#  Example A = [1 2 3 4 5] B=2

# result [1 2 3 4 5] -> [5 1 2 3 4] -> [5 4 1 2 3]

class RotateArray:

    def rotate(arr, K):

        N = len(arr)
        rev_obj = Reverse

        K = N - K

        arr = rev_obj.reverse(arr, 0, N-1)
        # print(arr)
        arr = rev_obj.reverse(arr, K, N-1)
        # print(arr)
        arr = rev_obj.reverse(arr, 0, K-1)
        # print(arr)
        

        return arr


# print(RotateArray.rotate([1, 2, 3, 4, 5],2))


class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return a list of list of integers

    def reverse(self,arr, start, end):
        # first element of an arr
        i = start
        # last element of an arr
        j = end

        while (i <= j):
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1
        
        return arr

    def solve(self, A, B): 

        N = len(A)
        res = list()

        for elem in B:

            elem = N - elem
            arr = list()
            
            for i in range(len(A)):
                arr.append(A[i])

            arr = self.reverse(arr, 0, N-1)
            arr = self.reverse(arr, elem, N-1)
            arr = self.reverse(arr, 0, elem-1)

            res.append(arr)
            print(res)
        
        return res


print(Solution().solve([1,2,3,4,5], [2,3]))
