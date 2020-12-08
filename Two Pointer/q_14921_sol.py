import sys

N = int(sys.stdin.readline().rstrip())
arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
res = 0
dist = 200000001
p1, p2 = 0, len(arr) - 1
while p1 < p2:
    if abs(arr[p1] + arr[p2]) < dist:
        dist = abs(arr[p1] + arr[p2])
        res = arr[p1] + arr[p2]
    if arr[p1] + arr[p2] < 0:
        p1 += 1
    elif arr[p1] + arr[p2] > 0:
        p2 -= 1
    else:
        print(0)
        exit()
print(res)
