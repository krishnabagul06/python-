n = int(input("Enter a number: "))

original = n

# Count number of digits
power = len(str(n))

sum = 0

while n > 0:
    digit = n % 10
    sum = sum + digit ** power
    n = n // 10

if original == sum:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")