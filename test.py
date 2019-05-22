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


for ro in range(4):
    if ro == 0:
        print(f'     ' + f'*' + f'     ')
    elif ro == 1:
        print(f'    ' + f'*' + f' ' + f'*' + f'    ')
    elif ro == 2:
        print(f'   ' + f'*' + f' ' + f'*' + f' ' + f'*' + f'  ')
    else:
        print(f'  ' + f'*' + f'     ' + f'*' + f'  ')



n = int(input('please enter an integer: '))
i = 0
result = 1
while i < n:
    result = result * 3
    i += 1
print(f'f({n})= {result}')


#factorial
def factorial(n):
    if n == 1:
        return n
    else:
        return n*factorial(n-1)

num = int(input("Enter a number: "))
if num < 0:
    print("sorry, factorial dose not exist for negetive numbers")
elif num == 0:
    print("The factorial of 0 is 1 ")
else:
    print(f"the factorial of {num} is {factoria l(num)} ")