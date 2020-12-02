if __name__ == '__main__':
    N, M = int(input()), int(input())
    arr = sorted(list(map(int, input().split(" "))))
    p, res = N - 1, 0
    for i in range(0, p):
        sum = arr[i] + arr[p]
        while p > i and sum > M:
            p -= 1
            sum = arr[i] + arr[p] if i != p else sum
        res = res + 1 if sum == M else res
    print(res)
