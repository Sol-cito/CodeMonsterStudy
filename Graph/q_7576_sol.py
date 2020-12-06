import sys
from _collections import deque


def bfs(arr, numOfZero):
    que = deque()
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 1:
                que.appendleft([i, j, 0, numOfZero])
                arr[i][j] = -1
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while que:
        pop = que.pop()
        for dir in directions:
            next_x = pop[0] + dir[0]
            next_y = pop[1] + dir[1]
            if 0 <= next_x < len(arr) and 0 <= next_y < len(arr[0]) and arr[next_x][next_y] == 0:
                numOfZero -= 1
                if numOfZero == 0: return pop[2] + 1
                que.appendleft([next_x, next_y, pop[2] + 1, numOfZero])
                arr[next_x][next_y] = -1
    return -1


M, N = map(int, sys.stdin.readline().rstrip().split(" "))
arr = [list(map(int, sys.stdin.readline().rstrip().split(" "))) for i in range(N)]
numOfZero = 0
for low in arr:
    numOfZero += len(list(filter(lambda x: x == 0, low)))
if numOfZero == 0:
    print(0)
else:
    print(bfs(arr, numOfZero))
