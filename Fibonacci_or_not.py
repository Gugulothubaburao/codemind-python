a = int(input())
b = 0
c = 1

for i in range(1,a):
    s = b+c
    b = c
    c = s
    
    if a==s:
        print(True)
        break
else:
    print(False)