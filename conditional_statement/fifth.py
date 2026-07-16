# WAP where user can enter a cost price and selling price and check user get profit , loss or no profit no loss 

cp=int(input("Enter cost price:"))
sp=int(input("Enter selling price:"))
if sp>cp:
    print("You got profit of rupees",sp-cp)
elif cp>sp:
    print("you got loss of rupees",cp-sp)
elif cp==sp:
    print("no profit no loss")
          