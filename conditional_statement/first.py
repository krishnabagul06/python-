# WAP to enter a number between 1 to 5 and print its word formate (use only if statement)

n=int(input("Enter a number between 1 to 5: "))
if n==1:
    print("One")
if n==2:
    print("Two")
if n==3:
    print("Three")
if n==4:
    print("Four")
if n==5:
    print("Five")
if n<1 or n>5:
    print("Invalid input")