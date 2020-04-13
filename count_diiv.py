def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    # print("P: ", P)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


def solution(A, B, K):

    b = int(B / K)
    a = 0

    print("b: ", b)
    if A == B == 0:
        return 1
    elif A == B == 1:
        return int(B / K)
    elif A == B:
        if B % K == 0:
            return 1
        else:
            return 0
    elif  A > 1:
        a = int((A - 1) / K)
        print("a: ", a)
    else:
        b += 1

    return int(b - a)







print(solution(6, 11, 2))

# b = B / K
# a = 0
# if A > 0:
#     a = (A - 1) / K
# else:
#     b += 1
#
# return int(b - a)
