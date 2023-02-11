#question4
user_input = int(input("Enter the number: "))
digit_sum = 0
while(user_input>0):
    digit_sum += (user_input%10)
    user_input = user_input // 10
print("The sum of the digits = ",digit_sum)
