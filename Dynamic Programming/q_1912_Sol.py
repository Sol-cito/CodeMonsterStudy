if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split(" ")))
    res = sum = arr[0]
    for i in range(1, len(arr)):
        """sum = arr[i] > arr[i] + sum and arr[i] or arr[i] + sum
        위 3항 연산자로 하면 오답처리됨. 왜냐하면, and / or  사용하는 3항연산자의 경우 만약
        arr[i] 이 0이 나온다면 0은 컴퓨터가 False로 인식하므로 제대로 된 조건식이 성립하지 않음.
        반례 ) 3 / -2 0 -2  --> 출력 : -2, 정답 : 0
         """
        sum = arr[i] if arr[i] > arr[i] + sum else arr[i] + sum
        # 위 3항 연산자 (if, else) 구조 : 결과 - if일때 - else일때의 결과
        res = max(res, sum)
    print(res)
