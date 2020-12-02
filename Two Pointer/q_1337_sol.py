if __name__ == '__main__':
    N = int(input())
    arr = sorted([int(input()) for i in range(N)])
    p = res = 0
    for i in range(len(arr)):
        while p < len(arr) and arr[p] < arr[i] + 5:
            p += 1
        res = max(res, p - i)
    print(5 - res)
