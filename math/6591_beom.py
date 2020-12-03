def get_combination(nk):
    n = nk[0]
    k = min(n-nk[1],nk[1])
    if (n,k) in combination:
        return combination[(n,k)]
    if k <= 3:
        value = 1
        for i in range(k):
            value = value * (n-i) / (i+1)
    else:
        value = get_combination((n-1,k-1)) + get_combination((n-1,k))
    combination[(n,k)] = int(value)
    return int(value)

combination = {}
input_str = input()
while input_str != "0 0": 
    print(get_combination(tuple(map(lambda x: int(x),input_str.split()))))
    input_str = input()
