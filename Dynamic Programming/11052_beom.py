n = int(input())
packs = list(map(lambda x: int(x),input().split()))

highest_price = {0 : 0 , 1 : packs[0]}
for num in range(2,n+1):
    highest_price[num] = max([packs[num-1]] + list(map(lambda i : highest_price[i+1] +  highest_price[num-i-1],list(range(num//2)))))

print(highest_price[n])