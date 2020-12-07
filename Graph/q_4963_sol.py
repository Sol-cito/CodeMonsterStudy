import sys
from collections import deque


def bfs(arr, x, y):
    arr[x][y] = 0
    que = deque([[x, y]])
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, -1], [1, 1], [1, -1], [-1, 1]]
    while que:
        pop = que.pop()
        for dir in directions:
            next_x, next_y = pop[0] + dir[0], pop[1] + dir[1]
            if 0 <= next_x < len(arr) and 0 <= next_y < len(arr[0]) and arr[next_x][next_y] == 1:
                que.appendleft([next_x, next_y])
                arr[next_x][next_y] = 0


while 1:
    W, H = map(int, sys.stdin.readline().rstrip().split(" "))
    if W == 0 and H == 0: break
    res = 0
    arr = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for i in range(H)]
    for x in range(len(arr)):
        for y in range(len(arr[0])):
            if arr[x][y] == 1:
                bfs(arr, x, y)
                res +=1
    print(res)
