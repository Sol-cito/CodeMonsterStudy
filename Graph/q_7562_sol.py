import sys
from _collections import deque

for i in range(int(sys.stdin.readline().rstrip())):
    L = int(sys.stdin.readline().rstrip())
    arr = [[0 for i in range(L)] for i in range(L)]
    now = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    arr[now[0]][now[1]] = 1
    que = deque([now])
    x, y = map(int, sys.stdin.readline().rstrip().split(" "))
    directions = [[-2, -1], [-1, -2], [-2, 1], [-1, 2], [2, -1], [1, -2], [2, 1], [1, 2]]
    while que:
        poll = que.pop()
        if poll[0] == x and poll[1] == y:
            print(arr[x][y] - 1)
            break
        for dir in directions:
            next_x, next_y = poll[0] + dir[0], poll[1] + dir[1]
            if 0 <= next_x < L and 0 <= next_y < L and arr[next_x][next_y] == 0:
                arr[next_x][next_y] = arr[poll[0]][poll[1]] + 1
                que.appendleft([next_x, next_y])
