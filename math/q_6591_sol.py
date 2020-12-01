if __name__ == '__main__':
    while 1:
        N, K = map(int, input().split(" "))
        if N == 0: break
        res = 1
        for i in range(N, N - min(K, N - K), -1):
            res *= i
        for i in range(min(K, N - K), 1, -1):
            res /= i
        print(int(res))
