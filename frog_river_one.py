def solution(X, A):
    length = len(A)
    B = [0] * (X+1)
    C = [0] * (X + 1)
    # print(B)
    for i in range(length):
        B[A[i]] += 1
    # print("B: ", B)
    flag = True
    for i in range(1, len(B)):
        if B[i] == 0:
            flag = False
    # print("flag: ", flag)
    if not flag:
        return -1
    else:
        for i in range(length):
            if C[A[i]] == 1:
                continue
            else:
                C[A[i]] = 1
                if all(item == 1 for item in C[1:A[i]]) & all(item == 1 for item in C[A[i]+1:]):
                    return i

        print(C)






X = 5
A = [1, 3, 1, 5, 2, 4, 1, 2, 4, 2, 3, 5, 4]
print(solution(X, A))


# # write your code in Python 3.6
#     length = len(A)
#     B = [0] * (X+1)
#     # print(B)
#     for i in range(length):
#         B[A[i]] += 1
#     # print(B)
#     flag = True
#     for i in range(1, len(B)):
#         if B[i] == 0:
#             flag = False
#     # print(flag)
#     if flag == False:
#         return -1
#     else:
#         for i in range(length-1, -1, -1):
#             if B[A[i]] == 1:
#                 return i