import sys

res = 0


def recursion(N, arr, string):
    if len(string) == len(N):
        global res
        res = min(res, len(string) + abs(int(string) - int(N)))
        return
    for i in arr:
        recursion(N, arr, string + str(i))


N, M = str((sys.stdin.readline().rstrip())), int(sys.stdin.readline())
notAllowed = list(map(int, sys.stdin.readline().rstrip().split(" "))) if M > 0 else []
if M == 10:
    print(abs(int(N) - 100))
    exit()
arr = list(i for i in range(10) if i not in notAllowed)
res = abs(int(N) - 100)
recursion(N, arr, "")
oneMore = oneLess = ""
for i in range(len(N) + 1):
    oneMore += str(arr[1]) if len(arr) > 1 and i == 0 and arr[0] == 0 else str(arr[0])
    oneLess += str(arr[len(arr) - 1]) if i < len(N) - 1 else ""
if len(oneLess) == 0: oneLess = "100"
print(min(res, len(oneMore) + abs(int(oneMore) - int(N)), len(oneLess) + abs(int(oneLess) - int(N))))
