def sum(operations):
    l = 0
    m = 0
    for i in range(len(operations)):
        if (operations[i] == "X++") or (operations[i] == "++X"):
            l+=1
        else:
            m-=1  
    return l + m   





n = int(input())
operations = []
for _ in range(n):
    operations.append(input())
print(sum(operations))
 