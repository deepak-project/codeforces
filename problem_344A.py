t = int(input())
l = []
for _ in range(t):
    l.append(int(input()))

ans = 1
for i in range(t-1):
    if l[i] != l[i+1]:
        ans+=1
print(ans)



 