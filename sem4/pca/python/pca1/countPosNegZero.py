#question 10
user_input = input("Enter a number \nEnter 'end' to quit\n")
p_count = 0
n_count = 0
z_count = 0
while(user_input != "end"):
    user_input = int(user_input)
    if(user_input > 0):
        p_count += 1
    elif(user_input < 0):
        n_count += 1
    else:
        z_count += 1
    user_input = input("Enter a number \n Enter nothing to quit\n")

print("Number of positive number: ",p_count)
print("Number of negative number: ",n_count)
print("Number of zero: ",z_count)
