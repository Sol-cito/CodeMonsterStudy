if __name__ == '__main__':
    N = int(input())
    dp = [0] * 100001
    for i in range(1, N + 1):
        dp[i] = i
        for j in range(2, i):
            if i - j * j < 0:
                break
            if dp[i - j * j] + 1 < dp[i]:
                dp[i] = dp[i - j * j] + 1
    print(dp[N])
