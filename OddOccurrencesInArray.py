def solution(A):
    ans = -1
    for item in A:
        occurrence = find_index(A, item)
        if occurrence > 1:
            continue
        else:
            ans = item
    return ans


def find_index(A,x):
    c = 0
    for i in range(0, len(A)):
        if A[i] == x:
            c += 1
    return c


arr = [1, 2, 3,85, 1, 2, 5, 3, 5]
print(solution(arr))




