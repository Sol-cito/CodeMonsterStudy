from functools import reduce
a = reduce(lambda x,y:(int(x)*int(y))**0.5,input().split())
print(a,a)
