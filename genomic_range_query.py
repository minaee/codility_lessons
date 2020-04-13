def get(c):
    if c == 'A':
        return 1
    elif c == 'C':
        return 2
    elif c == 'G':
        return 3
    elif c == 'T':
        return 4

def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P

def solution(S, P, Q):
    n = len(S)
    m = len(P)

    s = [0] * n
    for i in range(n):
        s[i] = get(S[i])

    sums = prefix_sums(s)
    print(sums)
    print( sums[5] - sums[4] )
    result = [0] * m

    for i in range(m):
        temp = sums[Q[i]] - sums[P[i]-1]
        temp

S = "CAGCCTA"
P = [2, 5, 0]
Q = [4, 5, 6]
solution(S, P, Q)

# result = [0] * m
# for i in range(m):
#     temp = 50
#     for j in range( P[i], Q[i]+1):
#         if temp > get(S[j]):
#             temp = get(S[j])
#     result[i] = temp
# print("result: ", result)
# return result