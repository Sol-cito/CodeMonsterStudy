from collections import deque

if __name__ == '__main__':
    N, M = map(int, input().split(" "))
    arr = [list(input()) for i in range(N)]
    arr[0][0] = '-1'
    dis = 1
    que = deque([dis, 0, 0])
    dir = [[0, 1], [1, 0], [-1, 0], [0, -1]]
    while que:
        x, y, dis = que.pop(), que.pop(), que.pop()
        if x == N - 1 and y == M - 1:
            res = dis
            break
        for i in dir:
            nextX = x + i[0]
            nextY = y + i[1]
            if 0 <= nextX < N and 0 <= y + i[1] < M and arr[nextX][nextY] == '1':
                arr[nextX][nextY] = '-1'
                que.appendleft(nextX)
                que.appendleft(nextY)
                que.appendleft(dis + 1)
    print(dis)
