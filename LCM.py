a,b = map(int,input().split())

for i in range(1,b+1):
    if (i*a)%b==0:
        print(a*i)
        break