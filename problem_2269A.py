t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    x = a - (b - 1)

    card = (2 ** x) + (2 * (b - 1))

    print(card)

 