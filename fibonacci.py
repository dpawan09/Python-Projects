n = int(input("enter limit for fibonacci series"))
a = 0
b = 1
print(a)
print(b)
for i in range(3, n + 1):
    c = a + b
    print(c)
    a=b
    b=c