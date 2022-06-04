def add(n):
    sum = 0
    while n>0:
      r = n%10
      sum = sum+r**2
      n = n//10
    if sum>9:
        sum = add(sum)
    return sum
        
a = int(input())
x = add(a)
print(x==1)