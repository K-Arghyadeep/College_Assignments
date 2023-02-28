userInput = int(input('Enter a number.\t'))
reversedNum = 0
while userInput > 0:
    digit = userInput % 10
    reversedNum = (reversedNum * 10) + digit
    userInput //= 10
print(reversedNum)