if __name__ == '__main__':
    for i in range(int(input())):
        N, M = list(map(int, input().split(" ")))
        a = sorted(list(map(int, input().split(" "))))
        b = sorted(list(map(int, input().split(" "))))
        p = res = 0
        for i in range(N):
            while p < M and a[i] > b[p]:
                p += 1
            res = res + p
        print(res)
