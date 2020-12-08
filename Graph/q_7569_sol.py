import sys
from _collections import deque

def bfs(to, arr, que, M, N, H):
    directions = [[0, 0, 1], [0, 1, 0], [0, -1, 0], [0, 0, -1], [1, 0, 0], [-1, 0, 0]]
    while que:
        pop = que.pop()
        for dir in directions:
            nh, nr, nc = pop[0] + dir[0], pop[1] + dir[1], pop[2] + dir[2]
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M and arr[nh][nr][nc] == 0:
                arr[nh][nr][nc] = -1
                que.appendleft([nh, nr, nc, pop[3] + 1])
                to -= 1
                if to == 0: return pop[3] + 1
    return -1


M, N, H = map(int, sys.stdin.readline().rstrip().split(" "))
arr = [[list(map(int, sys.stdin.readline().split(" "))) for i in range(N)] for i in range(H)]
to = 0
que = deque()
for i in range(M):
    for j in range(N):
        for k in range(H):
            if arr[k][j][i] == 0:
                to += 1
            elif arr[k][j][i] == 1:
                que.appendleft([k, j, i, 0])
if to == 0:
    print(0)
else:
    print(bfs(to, arr, que, M, N, H))
