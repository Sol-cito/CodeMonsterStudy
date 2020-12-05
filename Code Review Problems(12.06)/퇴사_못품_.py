days,tp = int(input()) , []
for i in range(days):
    tp.append( list(map(int,input().split())))
def price(i):
    if i < days:
        if tp[i][0] + i <= days:
            return max(tp[i][1]+price(i+tp[i][0]),price(i+1))
        else:
            return 0
    else:
        return 0
print(price(0))
