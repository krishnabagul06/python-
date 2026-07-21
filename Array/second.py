import array as arr

a=arr.array("i",[ ])
sum=0
n=int(input("Enter the limit of array:"))
print("Enter the elements of array;")

for i in range(n):
    x=int(input())
    a.append(x)

for m in a:
    print(m)
    sum=sum+m
print("Sum of array elements is:",sum)