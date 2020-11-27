#성우는 1분에 1~5 이동 가능.
#성우 에서 민건 집까지 거리 : N
N = int(input())

#몇분만에 찾을 수 있는가
answer = int(N / 5) ;
plus = N % 5;
if(plus!=0):
  print(answer+1)
else:
   print(answer)
