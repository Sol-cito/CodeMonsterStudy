from collections import deque


def search(arr, N):
    res = 0
    visit = [[0 for i in range(N)] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                bfs(i, j, arr, N, visit)
                res += 1
    return res


def bfs(x, y, arr, N, visit):
    visit[x][y] = 1
    que = deque([[x, y]])
    dir = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    while que:
        poll_x, poll_y = que.popleft()
        for i in range(len(dir)):
            nextX = poll_x + dir[i][0]
            nextY = poll_y + dir[i][1]
            if 0 <= nextX < N and 0 <= nextY < N and visit[nextX][nextY] == 0 and arr[x][y] == arr[nextX][nextY]:
                visit[nextX][nextY] = 1
                que.appendleft([nextX, nextY])


if __name__ == '__main__':
    N = int(input())
    arr = [list(input()) for i in range(N)]
    print(search(arr, N))
    for i in range(N):
        for j in range(N):
            if arr[i][j] in ('R', 'G'):
                arr[i][j] = 'R'
    print(search(arr, N))
