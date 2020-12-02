if __name__ == '__main__':
    G = int(input())
    p1, p, res = 1, 2, 0
    while p1 < p:
        while p <= 100000 and p * p - p1 * p1 < G:
            p += 1
        if p * p - p1 * p1 == G:
            res += 1
            print(p)
        p1 += 1
    if res == 0: print(- 1)
