name = input('Enter name :')
age = int(input('Enter age :'))

if(age > 18):
    print('You are eligible for age')
else:  
    print('{}, You come after {} years'.format(name,18-age))
