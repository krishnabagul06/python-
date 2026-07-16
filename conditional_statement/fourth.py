# WAP to find the greater between three numbers

a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
c=int(input("Enter third number: "))
if a>b and a>c:
    print(a,"is greater than",b,"and",c)
elif b>a and b>c:
    print(b,"is greater than",a,"and",c)
elif a==b and b==c:
    print("All three numbers are equal")
else:
    print(c,"is greater than",a,"and",b)
