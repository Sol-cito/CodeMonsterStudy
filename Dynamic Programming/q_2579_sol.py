if __name__ == '__main__':
    N = int(input())
    arr = [int(input()) for i in range(N)]
    j1 = j2 = arr[0]
    rest = 0
    for i in range(1, len(arr)):
        temp = rest
        rest = max(j1, j2)
        temp2 = j1
        j1 = temp + arr[i]
        j2 = temp2 + arr[i]
    print(max(j1, j2))