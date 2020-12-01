def getList(arr, N):
    dp = [0] * len(arr)
    for i in range(N):
        length = 1
        for j in range(i):
            length = max(length, dp[j] + 1) if arr[i] > arr[j] else length
        dp[i] = length
    return dp

if __name__ == '__main__':
    N = int(input())
    arr = list(map(int, input().split(" ")))
    dp1 = getList(arr, N)
    arr.reverse()
    dp2 = getList(arr, N)
    res = 0
    for i in range(len(dp1)):
        res = max(res, dp1[i] + dp2[len(dp2) - 1 - i] - 1)
    print(res)