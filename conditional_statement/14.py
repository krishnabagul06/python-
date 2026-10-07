# WAP to pritn the series of square of a number up to the n number

n=int(input("Enter a number:"))
# for i in range(1,n+1):
#     print(i**2,end=" ") # print(i*i,end=" ")
i=1
while(i<=n):
    print(i*i,end=" ")
    i+=1