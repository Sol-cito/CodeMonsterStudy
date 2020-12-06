from _collections import deque
import sys


def bfs(arr):
    que = deque([[0, 0, 1, 1]])
    arr[0][0] = -1
    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    while que:
        pop = que.pop()
        if pop[0] == len(arr) - 1 and pop[1] == len(arr[0]) - 1:
            return pop[3]
        for dir in directions:
            next_x = pop[0] + dir[0]
            next_y = pop[1] + dir[1]
            if 0 <= next_x < len(arr) and 0 <= next_y < len(arr[0]):
                if pop[2] == 1 and arr[next_x][next_y] in (0, 2):
                    que.appendleft([next_x, next_y, 1, pop[3] + 1])
                    arr[next_x][next_y] = -1
                elif pop[2] == 1 and arr[next_x][next_y] == 1:
                    que.appendleft([next_x, next_y, 0, pop[3] + 1])
                    arr[next_x][next_y] = -1
                elif pop[2] == 0 and arr[next_x][next_y] == 0:
                    que.appendleft([next_x, next_y, 0, pop[3] + 1])
                    arr[next_x][next_y] = 2
    return -1


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
arr = [[int(i) for i in sys.stdin.readline().rstrip()] for i in range(N)]
print(bfs(arr))
