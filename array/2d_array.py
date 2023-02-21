# Question 1: print row wise sum of an matrix


mat = [[1,5,9],[2,8,2],[7,6,2]]

for rows in mat:
    sum = 0
    for j in rows:
        sum = sum + j

    # print(sum)


# Question 2: print the diagonal from right to left and left to right


mat = [[1,5,9],[2,8,2],[7,6,2]]

n = len(mat)
i = 0
j = 0


while i < n:
    # print(mat[i][j])
    i += 1
    j += 1

i = 0
j = n - 1

while i < n:
    # print(mat[i][j])
    i += 1
    j -= 1


# Question 3: Given a mat[n][m] print all the diagonals going from right to left

# Diagonals starting form 0th row and (m-1)th column
# 
# 

mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

n = len(mat)
m = len(mat[0])

print(len(mat[0]), len(mat))


for j in range(0, len(mat[0])):
    i = 0
    while (i < n and j >= 0):
        # print(i,j,"-->", mat[i][j])
        i += 1
        j -= 1

for i in range(1, n):
    j = m - 1

    while (i < n and j >= 0):
        # print(i,j,"-->", mat[i][j])
        i += 1
        j -= 1


# Question 4: Transpose the given array

mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]

for i in range(0, len(mat[0])-1):
    j = i + 1
    while j < len(mat[0]):
        temp = mat[i][j] 
        mat[i][j] = mat[j][i]
        mat[j][i] = temp

        j += 1

# print(mat)



# Question 5: Rotate the matrix by 90 degree clockwise

mat = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15], [16,17,18,19,20], [21,22,23,24,25]]

# to rotate the matrix by 90 degree first we transpose
for i in range(0, len(mat[0])-1):
    j = i + 1
    while j < len(mat[0]):
        # print(i,j)
        temp = mat[i][j] 
        mat[i][j] = mat[j][i]
        mat[j][i] = temp

        j += 1

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

for i in range(0,len(mat)):
    mat[i] = reverse(mat[i], 0, len(mat[i])-1)


# print(mat)






