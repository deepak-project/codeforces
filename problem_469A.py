n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
x.pop(0)
y.pop(0)
z = x + y
print(z)
 
i = 1
while i < n+1:
    if i in z:
        if i == n:
            print("I become the guy.")
        i +=1
    else:
        print("Oh, my keyboard!")
        break

 