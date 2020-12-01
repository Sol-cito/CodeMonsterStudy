if __name__ == '__main__':
    N = int(input())
    p1, p2, sum, res = 1, 1, 1, 0
    for i in range(N):
        while p2 < N and p2 - p1 < N and sum < N:
            p2 += 1
            sum += p2
        res = res + 1 if sum == N else res
        sum -= p1
        p1 += 1
    print(res)
