num = int(input("enter the number for factorial"))
fac = 1
for i in range(num,0,-1):
    fac = fac * i
print(fac)