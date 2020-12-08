import sys

# 1. for문 한바퀴 돌면서 안익은 토마토(0) 개수를 구하고, queue에 토마토(1) 좌표를 담음 -> [x좌표, y좌표, z좌표, 일수]
# 2. queue를 bfs하면서 토마토를 익히고, 안익은 토마토 개수에서 익힌 토마토 개수를 뺌
# 3. 안익은 토마토 개수가 0이 되면 그 일수를 반환함.
# 4. while이 끝났는데도 안익은 토마토 개수가 1개가 넘으면 -1 반환, 아니면 일수 반환

M, N, H = map(int, sys.stdin.readline().rstrip().split(" "))
arr = [[list(map(int, sys.stdin.readline().split(" "))) for i in range(N)] for i in range(H)]
