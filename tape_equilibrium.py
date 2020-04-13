def solution(A):
    # write your code in Python 3.6
    length = len(A)
    minn = 1000000000
    if length == 1:
        return abs(A[0])
    elif length == 2:
        if A[0] < 0:
            return abs(A[0] - A[1])
        else:
            if A[1] < 0:
                return abs(A[1] - A[0])
            else:
                return abs(A[0] - A[1])

    forward = [None]*length
    backward = [None]*length
    # print(backward)
    temp = 0
    for i in range(length):
        temp = temp + A[i]
        forward[i] = temp
    print("forward: ", forward)

    temp = 0
    # print("inja")
    for i in range(length-1, -1, -1):
        # print("i: ", i)
        temp = temp + A[i]
        backward[i] = temp
        # print("backward: ", backward)
    print("backward: ", backward)

    if length > 2:
        for i in range(1, length):
            qabl = forward[i-1]
            # print("qabl: ", qabl)
            bad = backward[i]
            # print("bad: ", bad)
            temp = 0
            if qabl < 0:
                temp = abs(qabl - bad)
            else:
                if bad < 0:
                    temp = abs(bad - qabl)
                else:
                    temp = abs(qabl - bad)
            # print("temp: ", temp)
            if temp < minn:
                minn = temp
            else:
                continue
        return minn


A = [1000, -1000]
b = [1]
c = [-2]
d = [-1, -2, -3]
e = [3, 1, 2, 4, 3]
print(solution(A))
print(solution(b))
print(solution(c))
print(solution(d))
print(solution(e))
