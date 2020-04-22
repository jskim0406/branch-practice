for i in range(100):
    if i%3 == 0 and i%5 !=0:
        print('fiz')
    elif i%5 == 0 and i%3 != 0:
        print('buz')
    elif i%15 == 0:
        print('fizbuz')
    else:
        print(i)



