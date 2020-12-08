import sys

P, Q = map(int, sys.stdin.readline().rstrip().split(" "))
c1, c2 = map(int, sys.stdin.readline().rstrip().split(" "))
arr_p = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
arr_q = sorted(list(map(int, sys.stdin.readline().rstrip().split(" "))))
p1 = p2 = 0
dist = 4 * 10 ** 8 + 1
res = []
while p1 < len(arr_p) or p2 < len(arr_q):
    if abs(arr_p[p1] - arr_q[p2]) < dist:
        res = []
        dist = abs(arr_p[p1] - arr_q[p2])
    if abs(arr_p[p1] - arr_q[p2]) == dist:
        res.append([arr_p[p1], arr_q[p2]])
    if p1 < len(arr_p) - 1 and arr_p[p1] <= arr_q[p2]:
        p1 += 1
    elif p2 < len(arr_q) - 1 and arr_p[p1] > arr_q[p2]:
        p2 += 1
    else:
        break
print(abs(c1 - c2) + dist, len(res))
