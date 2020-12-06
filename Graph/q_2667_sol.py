from _collections import deque
import sys


def bfs(arr, x, y):
    que = deque([[x, y]])
    arr[x][y] = '0'
    cnt = 1
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while que:
        poll = que.pop()
        for i in dir:
            next_x, next_y = poll[0] + i[0], poll[1] + i[1]
            if 0 <= next_x < len(arr) and 0 <= next_y < len(arr[0]) and arr[next_x][next_y] == '1':
                que.appendleft([next_x, next_y])
                arr[next_x][next_y] = '0'
                cnt += 1
    return cnt


N = int(sys.stdin.readline().rstrip())
arr = [[i for i in sys.stdin.readline().rstrip()] for _ in range(N)]
res, resArr = 0, []
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == '1':
            resArr.append(bfs(arr, i, j))
            res += 1
print(res)
for i in sorted(resArr):
    print(i)