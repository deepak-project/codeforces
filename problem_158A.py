n = list(map(int, input().split()))
a = list(map(int, input().split()))
k = n[1]
b = a[k-1]
c = []
for i in range(len(a)):
    d = a.copy()
    if d[i] >= b:
        c.append(d.pop(i))
while 0 in c:
    c.remove(0)
print(len(c))