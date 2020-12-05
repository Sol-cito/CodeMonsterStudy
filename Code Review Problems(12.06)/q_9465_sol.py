if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [list(map(int, input().split(" "))), list(map(int, input().split(" ")))]
        t1, t2, rest, res = arr[0][0], arr[1][0], 0, 0
        for j in range(1, len(arr[0])):
            temp = rest
            rest = max(t1, t2)
            temp2 = t2
            t2 = max(t1, temp) + arr[1][j]
            t1 = max(temp, temp2) + arr[0][j]
            res = max(rest, t1, t2)
        print(res)

