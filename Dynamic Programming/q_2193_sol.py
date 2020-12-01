if __name__ == '__main__':
    N = int(input())
    dp = [1, 1]
    for i in range(N):
        dp.append(dp[len(dp) - 1] + dp[len(dp) - 2])
    print(dp[N - 1])
