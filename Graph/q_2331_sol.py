import sys

A, P = map(str, sys.stdin.readline().rstrip().split(" "))
arr = [A]
dic = {A: 1}
while 1:
    num = 0
    for i in arr[len(arr) - 1]:
        num += int(i) ** int(P)
    arr.append(str(num))
    if str(num) in dic:
        print(dic[str(num)] - 1)
        exit()
    else:
        dic[str(num)] = len(arr)
