# How to enter a element in array at a run time 

import array as arr

a=arr.array("i",[ ])
n=int(input("Enter the limit of array:"))
print("Enter the elements of array:")

#  loop to enter the array element
for i in range(n):
    x=int(input())
    a.append(x)

# loop for printing array elemment (way 1)
print("Array elements are : ")
for m in a:
    print(m)

# loop for printing array element (way 2)
print("Array elements are : ")
for i in range (n):
    print(a[i])
