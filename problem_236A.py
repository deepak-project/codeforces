a = sorted(input())
c = []
 
for i in range(len(a)-1):
    b = a.copy()
    if a[i] != a[i+1]:
        c.append(b.pop(i))
c.append(b[-1])
if len(c)%2 == 0:
    print("CHAT WITH HER!") 
else:
    print("IGNORE HIM!")
print(c)