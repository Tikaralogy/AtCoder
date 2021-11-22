n,x = map(int, input().split())
ls = list(map(int, input().split()))
ls.sort()
t = 0
print(ls)
while True:
    if x == 0 and ls == []:
        break
    if ls==[] and x >0:
        t -=1
    x -= ls[0]
    t +=1
    ls = ls[1:]
print(t)

