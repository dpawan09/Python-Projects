print("enter three no.")
a = int(input())
b = int(input())
c = int(input())

#Method 1
if a>b:
    if a>c:
        print("largest no. is:",a)
    else:
        print("largest no. is:",c)
else:
    if b>c:
        print("largest no. is:",b)
    else:
        print("largest no. is:",c)

#Method 2
lg=a
if b>a:
    lg = b

if c>a:
    lg = c

print("largest is:",lg)

#Method 3
if a > b and a > c:
    print("Largest number is:", a)
elif b > c:
    print("Largest number is:", b)
else:
    print("Largest number is:", c)

#Method 4
print("The largest number is:", max(a, b, c))
