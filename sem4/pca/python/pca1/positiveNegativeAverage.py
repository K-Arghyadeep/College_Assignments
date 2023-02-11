#question3
print("Enter -1 to exit...")
user_input = int(input("Enter a number:"))
p_sum = 0
p_count = 0
n_sum = 0
n_count = 0

while(user_input != -1):
    if(user_input > 0):
        p_sum += user_input
        p_count += 1
    elif(user_input < 0):
        n_sum += user_input
        n_count += 1
    user_input = int(input("Enter a number:"))

print("The average of negative numbers is: ", (n_sum/n_count))
print("The average of positve is: {:.9f}".format (p_sum/p_count))
