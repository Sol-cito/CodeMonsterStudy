if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(map(int, input().split(" "))))
    x = int(input())
    res, p = 0, n - 1
    for i in range(n):
        while i < p and arr[i] + arr[p] > x:
            p -= 1
        if arr[i] + arr[p] == x and i != p: res += 1
    print(res)
