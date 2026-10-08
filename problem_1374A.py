t = int(input())

for _ in range(t):
    x,y,n = map(int, input().split())
    r = (n-y)//x
    print(x*r+y)


    