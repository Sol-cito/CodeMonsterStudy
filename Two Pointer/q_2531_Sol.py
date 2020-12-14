import sys

#  pointer 2개를 가지고 하나는 끝, 하나는 시작점에 위치시킴
#  길이가 k가 될 때 까지 쭉쭉 나감.
#  길이가 k가 되었으면 rear pointer를 전진시키는데, 전진시키면서 set에 각 초밥을 담는다.
#  set에 중복된 초밥이 걸리면 그 떄 rear 포인터를 멈춤.

N, d, k, c = map(int, sys.stdin.readline().rstrip().split(" "))
arr = [int(sys.stdin.readline().rstrip()) for i in range(N)]
print(arr)
