n = int(input())
ls = list(map(int,input().split()))
ls.sort()
t = sum(ls[i] for i in range(n,3*n-1,2))
print(t)