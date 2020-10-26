# # # if , elif , else
# name = input('whats your name?')
# last_name = input('whats your last name?')
# li = input('Do you have a licence ?, tell us yes or no ?')
# age = input('how old are you?')
# if li =='yes' and age > '70':
#     print(name+' '+last_name+' please take care and stay calm, you are out of age range, engine stop.')
# elif  li == 'yes' and age>'18':
#     print(name + ' ' + last_name + ' your welcome, drive wel, have a good time.')
# else:
#     print('!!!Error , you are not able to drive, engine off!!!')

# # # Ternary Operators
# is_freand = False
# can_message = "message allowed" if is_freand else "not allowed to message"
# print(can_message)

# # # shor Circuting -- OR , AND
# is_freand = True
# is_user = True

# if is_freand or is_user:
#     print('Best freands for ever')

# # # Logical Operators
# print(4 > 5)#false
# print(4 < 5)#true
# print(4 == 5)#false
# print(1 >= 0)#true
# print(1 <= 0)#false
# print(0 != 0)#false
# print(not (True))#false- mitonim not tture bedun parantez biyarim

# # # is vs ==
# # # # #== is for being the condition
# print(True == 1)   #True
# print('' == 1)     #False
# print([] == 1)     #False
# print(10 == 10.0)  #True
# print([] == [])    #True
# print('1' == 1)    #False

# # # # # #is  is for the type, the memory location and the action of oprators
# print(True is 1)   # False
# print('' is 1)    # False
# print([] is [])     # False
# print(10 is 10.0)  # False
# print([] is [])    # False
# print('1' is 1)    # False

# # # For loop ----- pending
# for item in (1,2,3,4,5):
#     print(item)
#     print(item)
#     print(item)
# print(item)
# for item in (1,2,3,4,5):
#     for x in ['a','b','c']:
#         print(item, x )
# user = {
#     'name' : 'arman',
#     'age' : 23,
#     'can_swim' : False
# }
# for item in user.items():
#     print(item)

# for item in user.values():
#     print(item)

# for item in user.keys():
#     print(item)

# for item in user.items():
#     key, value = item;
#     print(key, value)

# for k, v in user.items():
#     print(k, v)

# # for item in 50:   erorr na shomara mide
# #     print(item)

# # # loop exercise
# my_list = [1,2,3,4,5,6,7,8,9,10]

# cont = 0
# for item in my_list:
#     cont = cont + item

# print(cont)

# # # RANGE
# for maxiter in range(1, 11):
#     print(maxiter)

# for _ in range(1, 11):
#     print(_)

# for _ in range(0, 10, 2):
#     print(_)

# for _ in range(10, 0, -1):
#     print(_)

# for _ in range(0, 10):
#     print(list(range(11)))

# # # enumrate
# for i,char in enumerate('helllooo'):
#     print(i, char)

# for i,char in enumerate(list(range(100))):
#     if char == 50:
#         print(f'index of 50 is: {i}')

# # # WHILE LOOP
# # i = 0
# # while i < 50:
# #     print(i)
# # i = 0
# while i < 50:
#     print(i)
#     break
# i = 0
# while i < 50:
#     print(i)
#     i += 1
# i = 0
# while i < 50:
#     print(i)
#     i += 1
# else:
#     print('done with all the work')
# i = 0
# while i < 50:
#     print(i)
#     i += 1
# else:
#     print('done with all the work')
# i = 0
# while i < 50:
#     print(i)
#     i += 1
#     break
# else:
#     print('done with all the work')

#
# for row in picture:
#     for pixel in row:
#         if (pixel == 1):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')

# some_list = ['a','b','c','b','d','m','n','n']
#
# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1 :
#         if value not in duplicates:
#             duplicates.append(value)
#
# print(duplicates)

# def say_hello (name, emoji):
#   print(f'helllloooooo {name} {emoji}')
# say_hello('Arman', ':D')
# say_hello('Adel', ':D')
# say_hello('akram', ':D')

# def say_hello (name, emoji):
#   print (f'helllloooooo {name} {emoji}')
# say_hello (emoji=':D' , name='Arman')

# def say_hello (name='aaa', emoji=':|'): # Defalt parametr
#   print (f'helllloooooo {name} {emoji}')
# say_hello ()

# def sum(num1, num2):
#   return num1 + num2
# print(sum(10,15))

# def super_func(*args, **kwargs):
#     total = 0
#     # print(kwargs)
#     for item in kwargs.values():
#         total += item
#     return sum(args) + total
#
# print(super_func(1,2,3,4,5, num1=5, num2=10))

# #Rule: params, *args, default parameters, **kwargs

# # # Exercise functions
# def highest_even(li):
#     even = []
#     for item in li:
#         if item % 2 == 0:
#             even.append(item)
#     return max(even)
#
# print(highest_even([10,30,20,1,2,3,6,5,4,7,8,9,50,40]))
# print(highest_even([25,23,27,29,31,35,37,39,10,2,11,80]))

# # # Scope rules
# a = 1
#
# def confusion():
#     ab=5
#     return ab
#
# print (confusion())# ab is scope of confusion
# print (a)# a is scope of a parameter before def

# """
# RULS OF SCOPE
# 1- start with local
# 2- parent local? it means a global def or any thing before the value or any thing else
# 3- Global whatever the file have it, that is global scope
# 4- bult in python functions
# """


# def outer():
#     x = 'local'
#
#     def inner():
#         nonlocal x
#         x = 'nonlocal'
#         print ("inner : ", x)
#
#     inner()
#     print("outer : ", x)
#
#
# outer()
