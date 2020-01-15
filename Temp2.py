for i in range(0, 50):
    if (i % 3) == 0 and (i % 7) == 0:
        print('DataAnalyst')
        continue
    
    elif (i % 3):
        print('Data')
        continue
    
    elif (i % 7):
        print('Analyst')
        continue
    
    elif not (i % 3):
        print(i)
        continue
    
    print(i)
pass