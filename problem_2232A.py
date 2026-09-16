import numpy as np

a = np.array([3, 1, 4, 1, 5,   9,   2, 6, 5, 3, 5])

b = np.sort(a)
 
def number(b):
    if len(b)%2 == 0:
        m = len(b)//2
        t = 0
        for i in range(m):
            if b[(m-1) - i] == b[i + m]:
                t +=1
            else:
                break
        n = m - t

    if len(b)%2 == 1:
        m = len(b)//2
        t = 0
        for i in range(m):
            if b[(m-1) - i] == b[i + (m+1)]:
                t +=1
            else:
                break
        n = m - t

    return print(n)

number(b)
            