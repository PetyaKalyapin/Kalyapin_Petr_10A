a = int(input())
b = a // 100
c = a % 100 // 10
d = a % 10
a1 = b + c
b1 = c + d
n = 0
if a1 > b1:
    n = str(a1)+str(b1)
else:
    n = str(b1)+str(a1)
print(int(n)) 
