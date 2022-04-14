n = int(input())
s = input()
x = 0
l = len(s)
for i in range(l-2):
    if s[i]=="A":
        if s[i+1]=="B":
            if s[i+2]=="C":
                x += 1
print(x)