import sys

N = int(sys.stdin.readline().rstrip())
arr = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
dist = 3000000001
res = []
for p1 in range(N - 2):
    p2, p3 = p1 + 1, N - 1
    while p2 < p3:
        if abs(arr[p1] + arr[p2] + arr[p3]) < dist:
            dist = abs(arr[p1] + arr[p2] + arr[p3])
            res = [p1, p2, p3]
        if arr[p1] + arr[p2] + arr[p3] < 0:
            p2 += 1
        elif arr[p1] + arr[p2] + arr[p3] > 0:
            p3 -= 1
        else:
            print(arr[p1], arr[p2], arr[p3])
            exit()
print(arr[res[0]], arr[res[1]], arr[res[2]])
