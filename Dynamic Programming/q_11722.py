if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split(' ')))
    dp = [1]
    res = 1
    for i in range(1, len(arr)):
        dp.append(1)
        for j in reversed(range(i)):
            dp[i] = arr[j] > arr[i] and max(dp[i], dp[j] + 1) or dp[i]
            res = max(res, dp[i])
    print(res)
