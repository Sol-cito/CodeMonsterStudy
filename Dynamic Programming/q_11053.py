if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split()))
    res = 1
    dp = [1]
    for i in range(1, len(arr)):
        maxVal = 0
        for j in range(0, i):
            if arr[j] < arr[i] : maxVal = max(maxVal, dp[j])
        dp.append(maxVal + 1)
        res = max(res, dp[i])
    print(res)