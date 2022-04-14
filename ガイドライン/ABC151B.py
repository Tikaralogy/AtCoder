n,k,m = map(int,input().split())
ls = list(map(int, input().split()))
x = n*m-sum(ls)
if x>k:
    print(-1)
elif x<0:
    print(0)
else:
    print(x)