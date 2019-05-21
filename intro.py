# # # # #name = "bolaji lawanson"
# # # # #print(name[0])
# # # # #num1 = "55"
# # # # #print(type(num1))
# # # # #num2 = int(num1)
# # # # #print(type(num2)
# # # #
# # # # '''x = 'blue'
# # # # y = 'green'
# # # # z = x
# # # # #print(x,y,z)
# # # #
# # # # z = y
# # # # #print(x,y,z)
# # # # x = z
# # # # print(x,y,z)
# # # #
# # # # route = 1000
# # # # print(route, type(route))
# # # # route = "north"
# # # # print(route, type(route))
# # # # '''
# # # # #collection data type
# # # # #1. Lists: -mutable
# # # # '''
# # # # days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
# # # # days[0] = "Aje"
# # # # print(days)
# # # #
# # # # words = ['book', False, 'Wednesday', 234 ]
# # # # words[2] = True
# # # # print(words)
# # # #
# # # # countries = ('Nigeria', 'The UK', 'Togo', 'australia', 1)
# # # # print(countries)
# # # #
# # # # name = "bolaji"
# # # # print(len("bolaji"))
# # # # print(len(['monday', 'tuesday', 'false']))
# # # # true = "God is good"
# # # # x = ["zebra", 49, -987, "monkey", true]
# # # # x.append("more")
# # # # print(x)'''
# # # #
'''
print("Welcome to Lapo MFBank")
p = float(input("please enter the amount you want "))
print("you requested %f " %p)
r = float(input("what is your company's rate? "))
r_frac = r/100
print("Your company's rate %f " %r_frac)
t = int(input("for how many years? "))
tim =  t * 12
t = print(tim)

TI = float(p*r_frac*tim)/100
print("your total interest is %f " %TI)
TR = (p + TI)
print("your total repayment is %f " %TR)
MR = (TR/(tim * 12))
print("your time in monthly repayment is %f " %MR)
'''
# # #
# # #
# # # a = ["today", "tomorrow", True, 0.5, False]
# # # b = ["today", "tomorrow", True, 0.5]
# # # print(a is b)
# # # print(a is not b)
# # # # #this is going to give us false because of the is function
# # # a=b
# # # print(a is b)
# # # print(a is not b)
# # #
# # # #comparison
# # # a = 2
# # # b = 6
# # # print(a < b)
# # # print(a > b)
# #
# # #in python we can change comparison operators:
# # # a=9
# # # print(0 <= a <= 10)
# #
# # #print("three" < 4 )
# # #python is dynamically typed. we don't need to supply
# #
# #
# # #membership opertor
# # p = (4, "monkey", 10, -33, True)
# # print(2 in p)
# # print(2 not in p)
# #
# # q = "today is tuesday"
# # print("today" in q)
# #
# # a = "monday"
# # b = "tuesday"
# # print(a and b)
# # print(a or b)
#
# #                   control flow statement
# #the if else statement:
#
# if condition1:
#     pass
# elif condition2:
#     pass
# ...
# else:
#     pass

# a = 10
# b = 3
# c = 7
# if(a>b and b<c):
#     print("very so")
# elif(a<b or c>b):
#     print("Not really true")
# else:
#     "Adunno"
#

#look up books on data structures and algorithm

# countries = ["Nigeria", "Ghana", True, 1000, "America"]
# i=0
# while i<len(countries):
#     print(countries[1])
#     i += 1
#
#
# countries = ["Nigeria", "Ghana", True, 1000, "America"]
# for cou in countries:
#     print(cou)

# vowel = ["A E I O U"]
# consonant = ["B C D F G H J K L M N P Q R S T V W X Y Z"]
# for vowel in vowel:
#     print("these letters are vowels " +vowel+ " thank you")
# for consonant in consonant:
#     print("these letters are consonant " +consonant+ " thank you")
#
# for i in "abcdefghijklmnopqrstuvwxyz":
#     if i in "aeiou":
#         print(i, "is a vowel")
#     else:
#         print(i, "is a consonant")
from datetime import date

'''
try:
    x = int(input("Enter a number"))
    ansa = x / 2
    print(ansa)y
except ValueError as err:
    print(err)
'''

'''
name = "John "
name += "Mike"
print(name)

List1 = ["Mango", "Orange", "Cashew", "Onion"]
List2 = ["Tomato", "20"]
print(type(List2))
print(List1 + List2)
List2 += ["cherry", "Bananas"]
print(List2)
'''
#
# List1 = ["Mango", "Orange", "Cashew", "Onion"]
# print(List1 +
'''
total = 0
count = 0
while True:
    try:
        line = input("enter a number")
        if line:
            try:
                number = int(line)
            except ValueError as Ve:
                print(Ve)
                continue
            total += number
            count += 1
        print(total)
    except EOFError:
        break
'''
#def add(a,b):
    #a=float(input("Enter the first  number"))
    #b=float(input("enter the second number"))
    #sum = (a + b)
 #   print(a + b)
#add(6,90)
#add(2,3)
#Using Functions:

# def get_int():
#         try:
#             i = int(input("Enter a number "))
#             print("Your age is ",i)
#         except ValueError as Ve:
#             print(Ve)
# get_int()

'''secret_word = "giraffe"
guess = ""

while guess != secret_word:
    guess = input("enter guess: ")
print("you win")
'''



#More complex guessing game:


'''
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not (out_of_guesses):
    if guess_count < guess_limit:
        guess = input("enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("out of guesses, you lose! ")
else:
    print("YOU WIN ! ")
'''
'''
list1 = ['Mathematics', 'Language', 'Science', 2000, False, 'Health Education']
#access the nth item
print(list1[2])

#updating the list
list1[4] = True
print(list1)
#deleting items from a list
del list1[2]
print(list1)

#multiplication and concatenation
list2 = list1 + ['Agric', '10.7']
print (list2)
print(['Agric', '10.7'] * 3)

#length of list
print(len(list1))

print('Agric' in list2)

#Iteration
print("start iteration")
for x in list1:
    print(x)

i=0
for x in list1:
    if(list1.index(x) <= 2):
        print(x)
'''

'''
for x in list1:
    print(x) 
'''
'''
list1 = ['Mathematics', 'Language', 'Science', 2000, True, 'Health Education']
for x in list1:
    if(list1.index(x) <= 4):
        print(x, end=' and ')
    else:
        print(x)
'''
'''
#indexing
list1 = ['Mathematics', 'Language', 'Science', 2000, True, 'Health Education']
print(list1[-2])
print(list1)
print("slicing start")
print(list1[2:])
print(list1[:2])
print(list1[1:4])

#max:
list2 = ['Monday', 'Tuesday', 'Friday', 'Wednesday']
print(min(list2))
print(max(list2))

#convert a tuple to a list
tuple1 = (234, 'c++', False, 'python')
list3 = list(tuple1)
print(list3)

#append()
list3 = [234, 'c++', False, 'Python']
list4 = list3.append('cee#')
list5 = list3 + ['c#']
print(list5)
print(list4)
'''
'''#count:
list6 = [234, 'c++', False, 'Python', 'c++', 'c#' ]
print(list6.count("c++"))

print([234, 'c++', False, 'Python', 'c++', 'c#'].count("Python"))
print([234, 'c++', False, 'Python', 'c++', 'c#'].count("jython"))

#extending a range into a list
'''
'''print(range(5)
for i in range(5):
    print(i, end="")
'''
'''
list7 = list(("a", "b", "c", "d"))
print(list7)
new = list7.extend(range(5))
print(list7)
print(new)
'''
'''
name = input("what is your name")
age = input("how old are you")
family = input("number of family")
friend_names = input("names of friends")

print("Hello my name is" + name + " I am " + age + " years old, and i am from a family of " + family + \
      ' my friends are ' + friend_names + ".")
'''
'''
import datetime
currentDate: date = datetime.date.today()
print(currentDate.strftime('%d %b %y'))
'''
'''
import datetime
currentDate : date
print(currentDate)
'''
'''
import datetime
currentDate = datetime.date.today()
userInput = input('please enter your birthday ')
birthday = datetime.datetime.strptime(userInput, '%m/%d/%Y')
print(birthday)
'''
#simply prints the argument passed to it
# def writer(word):
#    # print("please pass an argument")
#     print(word)
# writer('Hello class')
#
# #converts celsius to farenheit:
# def faren(T_in_celsius):
#     return(T_in_celsius *(9/5)) + 32
# print(faren(20), 'farenheit')
'''
faren_list= []
celsius_list = [20, 5, 10.6, 7, 9]
for items in celsius_list:
    faren_list.append(faren(items))
print(faren_list)
'''
'''
empty = []
for item in[20, 5, 10.6, 7, 9]:
    empty.append(faren(item))
print(empty)
'''
#change a list passed to it:

'''def average():
    empty = []
    a = float(input('a: '))
    empty.append(a)
    b = float(input('b: '))
    empty.append(b)
    c = float(input('c: '))
    empty.append(c)
    d = float(input('d: '))
    empty.append(d)
    e = float(input('e: '))
    empty.append(e)

    sum = a+b+c+d+e

    print(empty)
    x = len(empty)
    print(float(sum/x))
average()'''

# def averager():
#     list1 = []
#     sum = 0
#     x=0
#     while(len(list1) < 5):
#         item = float(input("enter a number"))
#         list1.append(item)
#         x += 1
#     for item in list1:
#         sum += item
#     av = float(sum/len(list1))
#     print(av)
# averager()
# weight_lbs = input('Weight (lbs): ')
# weight_kg = int(weight_lbs) * 0.45
# print (weight_kg)
# first = 'john'
# last = 'smiith'
# message = first + ' [' + last + ']is a coder '
# msg = f'{first} [{last}] is a coder '
#
# print(msg)
# person = 'kayode is an intelligentzombie '
# print(person.replace('intelligentzombie', 'zombie'))

#creating sets
x = set("A Pyhthon set")
#print(x)
print(type(x))
#passed a list to the inbuilt set
y = set(["pyhton", "c++", "java", "javascript", "PHP"])
print(y)
#when a tuple contains repeated items is passed to the set () fxn
states = set(("Lagos", "Benin", "Onitsha", "kaduna", "Benin", "Bayelsa"))
print(states)

#note:we can't include mutable objects during set creations

#frozen set
food = frozenset (['egg', 'jam', 'bread', True])
print(food)

#using the curly brace
states = {"Lagos", "Benin", "Onitsha", "kaduna", "Benin", "Bayelsa"}

#set operations
#add
colors = {"red", "green", "blue"}
print(colors.add("brown"))
colors.add("red")
print(colors)

#clear()
states = {"Lagos", "Benin", "Onitsha", "kaduna", "Benin", "Bayelsa"}
#print(states.clear())
print(states)

#remove()
print(states.remove("Onitsha"))
print(states)

#copy()
more_states = {'ogun', 'imo', 'nasarawa', 'kaduna', 'adamawa'}
more_states_backup = more_states.copy()
print(more_states_backup)

#difference
A = {"Tomi", "Daniel", "Ejito", "salah"}
B = {"Daniel", "Mohammed", "Bolaji", "Kayode"}
#print(A - B)
print(A.difference(B))
#print(B - A)
print(B.difference(A))

# difference_update
# x = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
# y = {'c', 'f', 'b'}
# z = {'e', 'd', 't', 'o'}
# differ = x-y-z
# print(differ)
# print(x.difference_update(y))
# print(x)

#discard()
x = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
x.discard('d')
print(x)

#intersection
x = {'a', 'b', 'c', 'd', 'e'}
y = {'c', 'd', 'e', 'f', 'g'}
print(x.intersection(y))
print(x.union(y))


#disjoint()
print(x.isdisjoint(y))

#subset()
x = {'a', 'b', 'c', 'd', 'e'}
y = {'c', 'd'}
print(y.issubset(x))
print(y < x)
print(x.issubset(y))
print(x < y)
print(x > y)





