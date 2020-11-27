if __name__ == '__main__':
    f = list(map(int, input().split(' ')))
    N, K = f[0], f[1]
    arr = list(map(int, input().split(' ')))
    res = sum = sum(arr[:K])
    p1 = 0
    for i in range(K, len(arr)):
        sum = sum - arr[p1] + arr[i]
        res = max(res, sum)
        p1 += 1
    print(res)
