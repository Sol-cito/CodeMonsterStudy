from functools import reduce

def bin(max_val,base, x):
    lo = 0
    hi = max_val
    while lo < hi:
        mid = (lo + hi) // 2
        if convert(n_ary(mid,base)) < x:
            lo = mid + 1
        else:
            hi = mid
    return [convert(n_ary(max(lo-1,0),base)),convert(n_ary(lo,base))]
def convert(n):
    return int(reduce(lambda x,y : str(x) + str(y),list(map(lambda x: normal[int(x)],n.zfill(n_digit)))))
def n_ary(number, base):
    if base <= 1:
        return "".zfill(n_digit)
    q, r = divmod(number, base)
    n = str(r)
    return n_ary(q, base) + n if q else n

target = int(input())
broken_num = int(input())
broken = []
if broken_num != 0:
    broken = list(map(int,input().split()))
if broken_num == 10:
    print(abs(100-target))
else:
    normal = list(filter(lambda x : x not in broken,range(10)))
    n_digit = len(str(target))
    max_val = (10-broken_num)**n_digit
    v= bin(max_val,len(normal),target)
    candidate = []
    if n_digit > 1:
        candidate.append(int((n_digit-1)*str(max(normal))))
    candidate.append(int((n_digit+1)*str(min(normal))))
    candidate += v
    short = lambda x : len(str(x)) + abs(x-target)
    a = list(map(short,candidate)) + [abs(100-target)]
    print(min(a))


