# WAP to enter a 2 number and print the greater between two number and also print equal if both number are same 

a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
if a>b:
    print(a,"is greater than b")
elif b>a:
    print(b,"is greater than a")
else:
    print("Both numbers are equal")