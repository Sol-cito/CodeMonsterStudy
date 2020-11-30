if __name__ == '__main__':
    N = int(input())
    if N % 2 == 1:
        print(0)
    else:
        dp = [1]
        for i in range(int(N / 2)):
            dp.append(dp[len(dp) - 1] * 3)
            for j in range(i):
                dp[len(dp) - 1] += dp[j] * 2
        print(dp[len(dp) - 1])