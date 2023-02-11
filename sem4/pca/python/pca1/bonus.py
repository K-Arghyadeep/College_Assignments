#Question2
sex = input("Enter the sex of the employee (m or f): ")
salary = int(input("Enter the salary of the employee: "))

def payment(s,b):
    bonus_amount = s * (b/100)
    print("Salary = ",s)
    print("Bonus  =  {:.1f}".format(bonus_amount))
    print("*********************************")
    print("Amount to be paid: {:.1f}".format(s+bonus_amount))

if( sex == "m"):
    if(salary < 10000):
        payment(salary,7)
    else:
        payment(salary,5)
elif(sex == "f"):
    if(salary < 10000):
        payment(salary,12)
    else:
        payment(salary,10)
else:
    print("Wrong Input")
