n = int(input())
x = 0
ls = []
for a in range(1,n//2+1):
    b = n-a
    while True:
        if a == 0 and b==0:
            break
        x += a%10+b%10
        a = a//10
        b = b//10
        ls.append(x)
    x = 0
print(ls)
