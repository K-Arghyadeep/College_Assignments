#question9
days_late = int(input("Enter the number of late days:\t"))

if(days_late < 6):
    print("Fine of 50 paisa")
elif(days_late >5 and days_late < 11):
    print("Fine of 1 rupee")
elif(days_late > 10 and days_late < 31):
    print("Fine of 5 rupees")
else:
    print("Membership cancelled")
