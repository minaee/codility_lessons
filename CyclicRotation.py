def solution(A, K):
    for i in range(K):
        A = rotation(A)
    return A


def rotation(A):
    length = len(A)
    B = [None]*(length)
    for i in range(length - 1):
        B[i+1] = A[i]
    B[0] = A[length-1]
    return B




arr = []
print(solution(arr, 123))