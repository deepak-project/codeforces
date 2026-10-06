a, n = list(map(int, input().split()))

for i in range(n):
    if a%10 == 0:
        a = a//10
    else:
        a = a - 1

print(a)