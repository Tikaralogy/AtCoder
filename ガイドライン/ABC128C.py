n,m  = map(int, input().split())
ls = []
for i in range(m):
    ls.append(list(map(int,input().split())))
lsp = list(map(int, input().split()))

x = 0
for i in range(2**n):
    a = bin(i)[2:]
    y = str(0)*(n-len(a))+a
    a = 0
    print(y)
    for i in range(m):
        z = 0
        for a in ls[i][1:]:
            z += int(y[a-1])
        if z%2 == lsp[i]:
            a += 1
        if a == m:
            x += 1
print(x)