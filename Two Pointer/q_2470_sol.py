import sys

N = int(sys.stdin.readline().rstrip())
arr = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
p1, p2 = 0, len(arr) - 1
dist = 2000000001
res = []
while p1 < p2:
    sum = arr[p1] + arr[p2]
    if abs(sum) < dist:
        dist = abs(sum)
        res = [arr[p1], arr[p2]]
    if arr[p1] + arr[p2] < 0:
        p1 += 1
    elif arr[p1] + arr[p2] > 0:
        p2 -= 1
    else:
        break
print(res[0], res[1])
