def clever_solution(N, K, arr):
    ryonArr = [i for i in range(len(arr)) if arr[i] == 1]
    dist = N + 1
    for i in range(len(ryonArr) - K + 1):
        dist = min(dist, ryonArr[i + K - 1] - ryonArr[i] + 1)
    print(dist if dist <= N else -1)


def twoPointer_solution(N, K, arr):
    p1 = p2 = ryons = 0
    dist = N + 1
    while p1 < len(arr):
        while p2 < len(arr) and ryons < K:
            if arr[p2] == 1: ryons += 1
            p2 += 1
        if ryons == K: dist = min(dist, p2 - p1)
        if arr[p1] == 1: ryons -= 1
        p1 += 1
    print(dist if dist <= N else -1)


if __name__ == '__main__':
    N, K = map(int, input().split(" "))
    arr = list(map(int, input().split(" ")))
    twoPointer_solution(N, K, arr)
    clever_solution(N, K, arr)
