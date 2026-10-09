# WAP to enter a number and count how many digit are repeated in the number and say no if htese is not any repeated digit.

n = input("Enter a number: ")

count = 0

for digit in set(n):            # set(n) gives us the unique digits. For example, 112233 becomes {1, 2, 3} (as string digits).
    if n.count(digit) > 1:
        count = count + 1

if count > 0:
    print("Repeated digits:", count)
else:
    print("No repeated digit")