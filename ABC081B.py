n = int(input())
int_list = list(input().split())
x =0
for i in range(n):
    while int_list[i]%2 ==0:
        for a in int_list:
            a%2==0
            x +=1
            del int_list[0:n-1]
            int_list.append(a/2)
print(x)