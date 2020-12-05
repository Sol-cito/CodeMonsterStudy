case_num = int(input())
for i in range(case_num):
    sticker_num = int(input())
    up = list(map(int, input().split()))
    down = list(map(int, input().split()))
    U, D, N = [up[0]], [down[0]], [0]
    for i in range(1, sticker_num):
        U.append(up[i] + max(D[i-1], N[i-1]))
        D.append(down[i] + max(U[i-1], N[i-1]))
        N.append(max(U[i-1], D[i-1], N[i-1]))
    print(max(U[-1], D[-1], N[-1]))
