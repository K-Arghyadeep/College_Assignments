count = 0
thisList = []
for i in range (0,101):
    if i%6==0 and i%4!=0:
        count+=1
        thisList.append(i)
print('Number of numbers divisible by 6 and not 4 between 0 and 100 are ',count)
print(thisList)