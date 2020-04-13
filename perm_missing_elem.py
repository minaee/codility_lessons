def solution(A):
    length = len(A)
    if length == 0:
        return 1
    elif length == 1:
        for i in range(2):
            if i+1 not in A:
                return i+1
    elif length > 1:
        for i in range(length + 1):
            if i + 1 not in A:
                return i+1


arr = [1,2]
print(solution(arr))