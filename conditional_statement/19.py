# WAP to enter a number and count how many even digits and odd digits are there in the number.

n=input("Enter a number:")
even_count = 0
odd_count = 0
for digit in n:
    if int(digit) % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
print("Even digits: ",even_count)
print("Odd digits: ",odd_count)