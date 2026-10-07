n=int(input("Enter a number:"))
m=n
s=0
while(n!=0):
    rem=n%10
    s=s*10+rem
    n=n//10
if(s==m):
    print("The number is palindrome number")
else:
    print("The number is not palindrome number")