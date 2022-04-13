n = int(input())
s,t = input().split()
x = ""
for i in range(n):
    x += s[i]
    x += t[i]
print(x)