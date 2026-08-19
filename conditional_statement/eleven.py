# WAP to print the following series upto an n number and also print the sum of the series.

n=int(input("Enter a number:"))

i=1
sum=0
while(i<n):
    print(i,end=",")
    sum=sum+i
    i=i+1
print("\n total is",sum)