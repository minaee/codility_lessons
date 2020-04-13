def solution(A):
    N = len(A)

    occurrence = {}
    for i in range(N):
        occurrence[A[i]] = 1
    print(occurrence)

    flag = 1
    for i in range(1, N+1):
        if occurrence.get(i) == 1:
            continue
        else:
            flag = 0

    return flag


# A = [4, 1, 3, 2]
A = [1,2,3,4]
# A = [4,3,2,1]
# A =
print(solution(A))