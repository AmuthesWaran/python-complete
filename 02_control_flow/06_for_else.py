flag = False
for number in range(3):
    print(f'{number}th time')
    # flag = True
    if flag:
        print('successful')
        break
else:
    print('runs only if loop gets completed')
