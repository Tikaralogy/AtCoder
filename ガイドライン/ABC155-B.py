n = int(input())
ls = list(map(int, input().split()))

for c in ls:
    if c%2==0:
        if c%3 != 0 and c%5 != 0:
            print("DENIED")
            exit()
print("APPROVED")