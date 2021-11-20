a,b = map(int, input().split())
x = []
total = 0
s = 0
for i in range(a,b+1):
    while True:
        if i == 0:
            break
        x.append(i%10)
        i = i//10
    for j in range((len(x)-1)//2):
        if x[j]==x[len(x)-j-1]:
            s +=1
    if s == ((len(x)-1)//2+1):
        total += 1
    s == 0
    x = []
print(total)
