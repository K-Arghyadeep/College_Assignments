print('Please enter 10 Persons age....')
count = 0
for i in range(1,11):
    age = int(input(f'{i} Person age: '))
    if age > 49 and age < 61:
        count += 1
print('Number of persons in the age group 50 to 60 is ',count)
