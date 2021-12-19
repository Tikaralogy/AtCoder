n,m = map(int,input().split())
lsab = [] 
lsc = [] 
for i in range(m): 
	lsab.append(list(map(int,input().split())))
for i in range(m): 
	lsc.append(list(map(int,input().split())))
print(lsab)
print(lsc)
l = [3,2,1,4]
a = lsab[1]
print(a)
print([l[a[0]-1],l[a[1]-1]]) 
print([l[a[1]-1],l[a[0]-1]])

