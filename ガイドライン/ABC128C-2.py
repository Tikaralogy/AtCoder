n,m  = map(int, input().split())
ls = []
for i in range(m):
    ls.append(list(map(int,input().split())))
lsp = list(map(int, input().split()))

x = 0
for i in range(2**n):
    