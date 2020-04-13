def solution(X, Y, D):
    dist = Y - X
    if dist % D == 0:
        return dist // D
    else:
        return (dist // D ) + 1


print(solution(0, 99999999, 100000000))