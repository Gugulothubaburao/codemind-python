a = int(input())
s = a**2
x = str(a)
y = str(s)

if y.endswith(x):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")