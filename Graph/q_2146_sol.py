import sys
from _collections import deque


def bfs(arr, visit, x, y):
    que = deque()
    directions = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    que.appendleft([x, y])
    while que:
        pop = que.pop()
        for dir in directions:
            nx, ny = pop[0] + dir[0], pop[1] + dir[1]
            if 0 <= nx < len(arr) and 0 <= ny < len(arr[0]) and visit[nx][ny] != 1 \
                    and (arr[nx][ny] <= 1 or arr[nx][ny] < arr[pop[0]][pop[1]]):
                arr[nx][ny] = arr[pop[0]][pop[1]] + 1 if arr[nx][ny] != 1 else arr[nx][ny]
                visit[nx][ny] = 1
                que.appendleft([nx, ny])


N = int(sys.stdin.readline().rstrip())
arr = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for i in range(N)]
visit = [[0 for i in range(N)] for i in range(N)]
for i in range(N):
    for j in range(len(arr[0])):
        if arr[i][j] == 1:
            visit[i][j] = 1
            bfs(arr, visit, i, j)
print(arr)
