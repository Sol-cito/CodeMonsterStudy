import sys

def inputFunc(N):
    arr = [[0,0]]
    for j in range(N):
        arr.append(list(map(int,input().split())))
    print(arr)
    return arr

N = int(sys.stdin.readline().rstrip())
arr = inputFunc(N)
dyn = [[0,0]]

for day in range(1, N+1):
    # dyn[N] 일때 가능한 거 찾기
    tmp = [0]
    dyn.append([0,0])
    for i in range(1,day+1):
        #돌면서, 직접적으로 계산했으 때 이 날에 끝나는 거 다 찾아서
        #print(i, "+", arr[i][0]," = ", arr[i][0]+i," ==?", day)
        if arr[i][0]+i == day:
            tmp.append( max(arr[i][1], dyn[i][1]))
    print(day,"날에 가능한 거 ",tmp)
    dyn[day][0] = day
    if day + arr[day][0] <= N+1 :
        dyn[day][1] += arr[day][1]+max(tmp)
    else:
        dyn[day][1] += max(tmp)
    print(dyn[day][0],"날의 최대는",dyn[day][1])

print(max(dyn))
        
    


