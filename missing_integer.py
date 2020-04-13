def solution(A):
    length = len(A)

    last_positive_int = 10000000
    dict = { }

    for i in range(length):
        if A[i] > 0:
            dict[A[i]] = 1
    print(dict)

    for i in range(1, length+1):
        # print("i: ", i)
        # print("dict.get(i): ", dict.get(i))
        # print("last_positive_int: ", last_positive_int)
        if dict.get(i) == 1:
            # last_positive_int = i+1
            continue
        else:

            if last_positive_int > i:
                last_positive_int = i

            # if A[i] < last_positive_int:

    if last_positive_int == 10000000:
        return length+1
    else:
        return last_positive_int


# A = [-1, -2, -3, -4, -2,  -100000]
# A = [1, 3, 6, 4, 1, 2]
A = [6,5,4,3,2,1]
print(solution(A))

