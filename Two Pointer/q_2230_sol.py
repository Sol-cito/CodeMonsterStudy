if __name__ == '__main__':
    N, M = map(int, input().split(" "))
    arr = [int(input()) for i in range(N)]
    arr.sort()
    p1 = p2 = 0
    res = arr[N - 1] - arr[0]
    for i in range(len(arr)):
        while p2 < N - 1 and arr[p2] - arr[p1] < M:
            p2 += 1
        res = arr[p2] - arr[p1] if M <= arr[p2] - arr[p1] < res else res
        p1 += 1
    print(res)
