wls = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
n = int(input())
s = input()
x = ""
for c in s:
    y = wls.index(c)
    y += n
    z = y%26
    x += wls[z]
print(x)