i = list(range(0, 50))

for i in range(0, 50):
    print(i+1)
    if (i % 3) == 0 and (i % 7) == 0:
        print('DataAnalyst')
        continue
    
    elif (i % 3):
        print('Data')
        continue
    
    elif (i % 7):
        print('Analyst')
        continue
    
    if not (i % 3):
        print(i)
        continue
    
    if not (i % 7):
        print(i)
        print('\n')
        continue
        print(i+1)
