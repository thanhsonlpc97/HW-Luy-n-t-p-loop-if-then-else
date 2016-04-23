number = int(input("Please input an odd number"))
if number % 2 == 0:
    number = int(input("That's a bloody even number, please input for real this time"))
countnum = len(str(number))
strconst = ''
for i in range(1, countnum + 1):
    strconst += ' '
count = 0
if countnum == 1:
    while number > 0:
        for i in range(1, number + 1):
            print("%d" % number, end='')
        number -= 2
        print('')
        strnum = ''
        for i in range (0, count + 1):
            strnum += ' '
        print('%s' % strnum, end='')
        count += 1
else:
    while number > 0:
        countnum1 = len(str(number))
        strnum = ''
        if countnum1 < countnum:
            for i in range(1, countnum - countnum1+1):
                strnum += ' '
        for j in range(1, number + 1):
            print("%s%d" % (strnum, number), end='')
        count += 1
        number -= 2
        print('')
        for m in range(1, count + 1):
            for n in range(1, len(strconst)):
                print("%s" % strconst, end='')
