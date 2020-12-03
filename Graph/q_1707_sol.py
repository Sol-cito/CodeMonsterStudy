from collections import deque
import sys


def bfs(start, dic, visit):
    que = deque([start])
    group1, group2 = set([start]), set()
    while que:
        polled = que.popleft()
        for i in range(len(dic.get(polled))):
            if polled in group1:
                if dic.get(polled)[i] in group1: return False
                group2.add(dic.get(polled)[i])
            else:
                if dic.get(polled)[i] in group2: return False
                group1.add(dic.get(polled)[i])
            if dic.get(polled)[i] not in visit:
                que.appendleft(dic.get(polled)[i])
                visit.add(dic.get(polled)[i])
    return True


if __name__ == '__main__':
    for i in range(int(sys.stdin.readline())):
        res = True
        V, E = map(int, sys.stdin.readline().split(" "))
        dic = {i + 1: [] for i in range(V)}
        for j in range(E):
            a, b = map(int, sys.stdin.readline().split(" "))
            dic.get(a).append(b)
            dic.get(b).append(a)
        visit = set()
        for j in range(1, V + 1):
            if j not in visit:
                visit.add(j)
                res = res and bfs(j, dic, visit)
        print("YES" if res else "NO")
