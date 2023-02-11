#question6
user_input = int(input("Enter number: "))
p_count = 0
c_count = 0

def check(ui):
    count = 0
    for i in range(1,ui+1):
        if(ui%i == 0):
            count += 1
    if(count==2):
        return 1
    else:
        return 0

while(user_input != -1):
    flag = check(user_input)
    if(flag == 1):
        p_count += 1
    else:
        c_count += 1
    user_input = int(input("Enter number: "))

print("Total composite: ",c_count)
print("Total prime: ",p_count)
