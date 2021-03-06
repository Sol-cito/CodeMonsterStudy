import sys

def search(dic):
    visit = [0] * len(dic)
    res = 0
    for i in range(1, len(dic) + 1):
        cur = i
        if visit[cur - 1] == 0:
            start = cur
            cnt = 0
            while visit[cur - 1] == 0:
                visit[cur - 1] = 1
                cur = dic.get(cur)
                cnt += 1
            while start != cur:
                start = dic.get(start)
                cnt -= 1
            res += cnt
    return res


for i in range(int(sys.stdin.readline().rstrip())):
    nArr = list(i for i in range(1, int(sys.stdin.readline().rstrip()) + 1))
    dic = dict(zip(nArr, list(map(int, sys.stdin.readline().rstrip().split(" ")))))
    res = len(nArr)
    print(len(nArr) - search(dic))


# def search(dic, target, visit, cycle, cnt):
#     cycle[target] = cnt
#     if visit[target - 1] == 0 and dic.get(target) == target:
#         visit[target - 1] = -1
#         return 1
#     elif visit[dic.get(target) - 1] != -1:
#         visit[target - 1] = -1
#         return search(dic, dic.get(target), visit, cycle, cnt + 1)
#     else:
#         visit[target - 1] = -1
#         if cycle.get(dic.get(target)) is not None and cycle.get(dic.get(target)) != 0:
#             return cnt - cycle.get(dic.get(target)) + 1
#         else:
#             return 0
#
#
# for i in range(int(sys.stdin.readline().rstrip())):
#     nArr = list(i for i in range(1, int(sys.stdin.readline().rstrip()) + 1))
#     dic = dict(zip(nArr, list(map(int, sys.stdin.readline().rstrip().split(" ")))))
#     res = len(nArr)
#     visit = [0] * len(nArr)
#     for num in nArr:
#         if visit[num - 1] != -1:
#             res -= search(dic, num, visit, {}, 1)
#     print(res)
