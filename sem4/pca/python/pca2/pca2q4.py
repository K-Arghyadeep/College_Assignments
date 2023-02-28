userInput= input('type "m" for mill cloth\ntype "h" for handloom items\t')
userInputAmount = int(input('Enter the purchase amount\t'))
discountedAmount = 0

match userInput:
    case 'm':
        if userInputAmount>0 and userInputAmount<101:
            discountedAmount = userInputAmount
        elif userInputAmount>101 and userInputAmount<201:
            discountedAmount = userInputAmount-(userInputAmount*.05)
        elif userInputAmount>201 and userInputAmount<301:
            discountedAmount = userInputAmount-(userInputAmount*.075)
        elif userInputAmount>300:
            discountedAmount = userInputAmount-(userInputAmount*.1)
        else:
            print('invalid Cost')
    case 'h':
        if userInputAmount>0 and userInputAmount<101:
            discountedAmount = userInputAmount-(userInputAmount*.05)
        elif userInputAmount>101 and userInputAmount<201:
            discountedAmount = userInputAmount-(userInputAmount*.075)
        elif userInputAmount>201 and userInputAmount<301:
            discountedAmount = userInputAmount-(userInputAmount*.1)
        elif userInputAmount>300:
            discountedAmount = userInputAmount-(userInputAmount*.15)
        else:
            print('invalid Cost')
    case _:
        print('invalid choice selection')
print('Amount to be paid is : ',discountedAmount)