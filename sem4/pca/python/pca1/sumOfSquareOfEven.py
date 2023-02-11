#question7
user_input = int(input("Enter the number: "))
sum = 0

for i in range (1,user_input+1):
    if(i % 2 == 0):
        sum += pow(i,2)

print("The sum of squares of even number less than equal to ",user_input," is ",sum)
