# WAP to enter the marks of 4 subject and check the marks is correct not less then 0 and not greater than 100 

hin=int(input("Enter the marks of Hindi:"))
if hin<0 or hin>100:
    print("Hindi marks is incorrect")

eng=int(input("Enter the marks of English:"))
if eng<0 or eng>100:
    print("English marks is incorrect")

math=int(input("Enter the marks of Math:"))
if math<0 or math>100:   
    print("Math marks is incorrect")

sci=int(input("Enter the marks of Science:"))
if sci<0 or sci>100:
    print("Science marks is incorrect")

sum=hin+eng+math+sci
per= sum/4
print(" Total marks is:",sum)
print(" Percentage is:",per)


