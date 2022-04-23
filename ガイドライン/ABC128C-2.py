n,m  = map(int, input().split())
ls = []
for i in range(m):
    ls.append(list(map(int,input().split())))
lsp = list(map(int, input().split()))

x = 0
for i in range(2**n):
    for j in range(m):
        y = 0
        for k in ls[j]:
            y += ((i >> k)&1)
            if y%2 != lsp[j]:
                