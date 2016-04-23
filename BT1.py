number = int(input('Input a number between 5 and 10:'))
while number < 5 or number > 10:
    number = int(input('Input a number between 5 and 10:'))
for i in range(1, number + 1):
    for j in range(1, i + 1):
        print(j, end='')
    print('')
