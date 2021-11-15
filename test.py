for i in range(len(ls)):
    te.extend(abs(t-0.006*ls(i)-a))
print(te.index(min(te)))
