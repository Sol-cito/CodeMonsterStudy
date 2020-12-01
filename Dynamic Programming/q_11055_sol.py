if __name__ == '__main__':
    A = int(input())
    arr = list(map(int, input().split(" ")))
    dp, res = [arr[0]], arr[0]
    for i in range(1, len(arr)):
        m = arr[i]
        for j in range(i):
           m = max(m, dp[j] + arr[i]) if arr[j] < arr[i] else m
        dp.append(m)
        res = max(res, m)
    print(res)