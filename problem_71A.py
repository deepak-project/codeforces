def word(words):
    a = words
    if len(a) > 10 :
        return f"{a[0]}{(len(a)-2)}{a[-1]}"
    else:
        return a



t = int(input())

 
for _ in range(t):
    words = input()
    print(word(words))