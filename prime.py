pr = int(input("Enter a number \n"))
c = 0
for i in range(1, pr + 1):
    if pr % i == 0:
        c += 1
if c == 2:
    print("given number is a prime number")
else:
    print("given number is not a prime number")