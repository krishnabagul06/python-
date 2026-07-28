# WAP for login page to check the user enter correct username and password where username is "krishna" and passwoed is "indore"

username=input("Enter the username:")
password=input("Enter the password:")
if username=="krishna" and password=="indore":
    print("Login successful")
elif username=="krishna" and password!="indore":
    print("Incorrect password")
elif username!="krishna" and password=="indore":
    print("Incorrect username")
else:
    print("incorrect username and password")