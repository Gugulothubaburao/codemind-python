m = int(input())
n = int(input())
i = m
for j in range(m,n+1):
    k = j
    while j!=0:
        s = j%10
        j = j//10
        if s == 0:
           break
        if k%s!=0:
           break
    else:
        print(k,end=" ")