n = int(input())
ls = list(map(int, input().split()))
import itertools
mylist1 = list(range(n))
ls1 = list(itertools.combinations(mylist1, 2))
x = 0
for l in ls1:
    x += ls[l[0]]*ls[l[1]]
print(x)