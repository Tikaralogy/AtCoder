n = int(input())
x = 0
while n >0:
    x += n%10
    n = n//10
print(x)