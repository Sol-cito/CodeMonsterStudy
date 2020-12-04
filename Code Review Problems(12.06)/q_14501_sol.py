import sys

if __name__ == '__main__':
    N = int(sys.stdin.readline().rstrip())
    arr = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for i in range(N)]
    res = 0
    dp = [0] * N
    for i in range(N):
        val = 0
        for j in range(i, -1, -1):
            val = max(val, dp[j]) if j + arr[j][0] <= i else val
        dp[i] = val + arr[i][1] if i + arr[i][0] <= N else val
        res = max(res, dp[i])
    print(res)
