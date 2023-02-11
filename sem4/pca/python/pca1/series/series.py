#question 5
term = int(input("Enter the value:"))
sum = 0

for i in range(1,term+1):
    sum += (pow(i,i)/i)

print("The sum of the series is {:.1f}".format(sum))
