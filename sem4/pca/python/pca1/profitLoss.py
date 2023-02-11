#question8
cp = int(input("Enter the cost price: "))
sp = int(input("Enter the selling price: "))

if(cp>sp):
    print("Loss")
    print("Incurred loss of :", cp - sp)
    print("Loss percentage is : ",(((cp - sp)/cp)*100),"%")
elif(sp>cp):
    print("Profit")
    print("Incurred profit of :", sp - cp)
    print("Profit percentage is : ",(((sp - cp)/cp)*100),"%")
else:
    print("Break-even")
