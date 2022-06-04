x = int(input())
y = str(x)
z = list(y)
y = set(y)
if len(y)==len(z):
    print("Unique Number")
else:
    print("Not Unique Number")