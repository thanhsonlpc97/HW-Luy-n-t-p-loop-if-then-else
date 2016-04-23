list3 = []
list5 = []
i = 1
while i < 100:
    if i % 3 ==0:
        list3 += [i]
    elif i % 5 == 0:
        list5 += [i]
    i += 1
print(list3 , ' ' , "chia hết cho 3")
print(list5 , ' ' , "chia hết cho 5")
