import sys

def inputFunc():
    m = int(sys.stdin.readline().rstrip())
    arr = []
    for j in range(2):
        arr.append(list(map(int,input().split())))
    #print(arr)
    return arr

def findAns(arr):
    dyn = arr.copy()
    dyn[0][0] = arr[0][0]
    dyn[1][0] = arr[1][0]
    dyn[0][1] = arr[0][1]+arr[1][0]
    dyn[1][1] = arr[1][1]+arr[0][0]

    for j in range(2, len(arr[0]) ):
        # if 밑에 2칸 짜리가 더 크거나 1칸 뒤에것이 더 크거나
        if arr[1][j-2] > arr[1][j-1] :
            dyn[0][j] = arr[0][j] + arr[1][j-2]
        else:
            dyn[0][j] = arr[0][j] + arr[1][j-1]

        if arr[0][j-2] > arr[0][j-1] :
            dyn[1][j] = arr[1][j] + arr[0][j-2]
        else:
            dyn[1][j] = arr[1][j] + arr[0][j-1]

    #print("dyn: ",dyn)
    if(max(dyn[0]) > max(dyn[1])):
        return max(dyn[0])
    else:
        return max(dyn[1])

N = int(sys.stdin.readline().rstrip())
arr = []
ans = 0
for i in range(N):
    arr = inputFunc()
    ans = findAns(arr)
    print(ans)