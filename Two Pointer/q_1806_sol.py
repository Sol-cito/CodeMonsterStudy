import sys

N, S = map(int, sys.stdin.readline().rstrip().split(" "))
arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
res = N + 1
sum, p = arr[0], 1
for i in range(len(arr)):
    while p < len(arr) and sum < S:
        sum += arr[p]
        p += 1
    if sum >= S:
        res = min(res, p - i)
    sum -= arr[i]
print(res if res != N + 1 else 0)
