# Question 1: You are given an integer A, print 1 to A using using recursion.

# Decreasing Order
def increasing(N):

    if N == 0:
        return
    
    print(N)

    return increasing()(N-1)

# Increasing Order

def decreasing(N):

    if N == 0:
        return
    
    decreasing(N - 1)

    print(N)


# Question 2: Write a recursive function that, given a string S, prints the characters 
# of S in reverse order.

def reverse_str(S):

    if len(S) == 1:
        print(S)
        return 
    
    k = S[-1]
    print(k)
    S = S[:-1]
    return reverse_str(S)

reverse_str("Suyash")
