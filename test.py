#no 1 question
for index in range(100):
    if index <= 100:
        print("kayode oshodi")
    else:
        print('thank you')

#no 2 question
for num in range(21):
    num_square = num*num
    print(f'{num}---{num_square}')

#no 3 question
numberofasterics = [12, 2, 2, 12]
for count in numberofasterics:
    if count == 12:
        print('*' * count )
    else:
        print('*'+'          '+'*')


square = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for count in square:
    print(f'*' * count)
