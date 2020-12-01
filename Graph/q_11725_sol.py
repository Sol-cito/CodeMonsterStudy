from collections import deque

if __name__ == '__main__':
    N = int(input())
    dic = {i: [] for i in range(1, N + 1)}
    for i in range(1, N):
        arr = list(map(int, input().split(" ")))
        dic.get(arr[0]).append(arr[1]), dic.get(arr[1]).append(arr[0])
    que = deque([1])
    visit = [0] * N
    visit[0] = 1
    parent = {i: 0 for i in range(1, N + 1)}
    while que:
        polledNode = que.popleft()
        polledArr = dic.get(polledNode)
        for i in range(len(polledArr)):
            if visit[polledArr[i] - 1] == 0:
                que.append(polledArr[i])
                visit[polledArr[i] - 1] = 1
                parent[polledArr[i]] = polledNode
    for i in range(2, N + 1):
        print(parent.get(i))
