if __name__ == '__main__':
    T = int(input())
    dp = [1, 1, 1]
    for i in range(T):
        N = int(input())
        for j in range(len(dp), N) :
            dp.append(dp[j - 2] + dp[j - 3])
        print(dp[N-1])