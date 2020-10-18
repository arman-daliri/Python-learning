"""
# x=5
# y="hi"
# print(x)
# print(y)
#
# x=4
# x="TOMAS"
# x="BILL"
# print(x)
#
# x,z,y=5,2,8
# print(x,z,y)
#
# z,x,c,v,b=1,2,3,4,5
# print(z*x)
# print(c/v)
# print(b+z)
#
# x = "10"
# def myfunc():
#   global x
#   x = "2.2"
# myfunc()
# print("2"+ x)
# x ="5"
# print(type(x))
#
# x = "Hello World"
# #display x:
# print(x)
# #display the data type of x:
# print(type(x))
#
# x = 1j
# #display x:
# print(x)
# #display the data type of x:
# print(type(x))
#
# x = ["apple", "banana", "cherry"]
# #display x:
# print(x)
# #display the data type of x:
# print(type(x))
#
# x = ("apple", "banana", "cherry")
# #display x:
# print(x)
# #display the data type of x:
# print(type(x))
#
# x = range(800)
# #display x:
# print(x)
# #display the data type of x:
# print(type(x))
#
# x = 1
# y = 2.8
# z = 1j
# print(type(x))
# print(type(y))
# print(type(z))
#
# x=10
# y=50
# z=26265962326599496599956212326294912326594
# print(type(x))
# print(type(y))
# print(type(z))
#
# x = 35e3
# y = 12E4
# z = -87.7e100
# print(type(x))
# print(type(y))
# print(type(z))
#
# x = 3+5j
# y = 5j
# z = -5j
# print(type(x))
# print(type(y))
# print(type(z))
#
# x=float(20)
# y=int(35.2256)
# z=complex(12)
# print(x)
# print(y)
# print(z)
# print(type(x))
# print(type(y))
# print(type(z))
#
# import random
# print(random.randrange(1,10))
#
# x = int(1)
# y = int(2.8)
# z = int("3")
# print(x)
# print(y)
# print(z)
# print(type(z))
#
# x = str("s1")
# y = str(2)
# z = str(3.0)
# print(x)
# print(y)
# print(z)
# print(type(z))
#
# print("Lorem ipsum dolor sit amet, consectetur adipiscing elit,"
#       " sed do eiusmod tempor incididuntut "
#       "labore et dolore magna aliqua.")
#
#
# a="hello world"
# print(a[1])
#
# a="hello world"
# print(a[0:11])
#
#
# a="hello world"
# print(a[-11:1])
#
#
# a="hello world "
# print(len(a))
#
#
# a="   hello, world    "
# print(a.strip())
#
#
# a="hello world"
# print(a.lower())
#
#
# a="hello world"
# print(a.upper())
#
#
# a="hello , world"
# print(a.replace("h" , "j"))
#
# a="hello, world"
# print(a.split(","))
#
# txt = "The rain in Spain stays mainly in the plain"
# x="ain" in txt
# print(x)
#
# txt2 = "The rain in Spain stays mainly in the plain"
# y = "ain" not in txt2
# print(y)
#
# a="hello "
# b="world"
# c=a+b
# print(c)
#
# age=36
# text="My name is jhon , Iam {} yers old."
# print(text.format(age))
#
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))
#
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
# print(myorder.format(quantity, itemno, price))
#
# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)
#
# print(10 > 9)
# print(10 == 9)
# print(10 < 9)
#
# k=200
# d=33
# if d>k:
#     print("d is bigger than k")
# else:
#     print("d is not bigger than k")
#
# print(bool("hi"))
# print(bool(15))
#
# x="hello"
# y=15
# print(bool(x))
# print(bool(y))
#
# print(bool(False))
# print(bool(None))
# print(bool(0))
# print(bool(""))
# print(bool({}))
# print(bool([]))
# print(bool(()))
#
# class myclass():
#     def __len__(self):
#         return 0
# myobj = myclass()
# print(bool(myobj))
#
# def myFunction() :
#     return True
# print(myFunction())
#
# def myFunction() :
#     return False
#
# if myFunction() :
#     print("Yes!")
# else:
#     print("No!")
#
# x=200
# print(isinstance(x,int))
#
# #Divide remaining
# x=5
# y=2
# print(x%y)
#
# #POW
# x=2
# y=5
# print(x**y) #same as 2*2*2*2*2
#
# #Outside the split part
# x=15
# y=5
# print(x//y)
#
# x=4
# x=x^3
# print(x)
#
# x=5
# print(x>3 and x<10)
#
# x=5
# print(x>3 or x<4)
#
# x=5
# print(not(x>3 and x<10))
#
# x = ["apple", "bnana"]
# y = ["apple", "bnana"]
# z = x
# print(x is z)
# print(x is y)
# print(x == y)
#
# x = ["apple", "bnana"]
# y = ["apple", "bnana"]
# z = x
# print(x is not z)
# print(x is not y)
# print(x != y)
#
# # print((20 + 3) ** 3)
#
# print(bin(5))
# print(int('0b101', 2))
#
# iq = 190
# print(type(iq))
# print(bin(iq))
# user_iq = 187
# print(type(user_iq))
# print(bin(user_iq))
# user_age = iq/4
# a = user_age
# print(a)
#
# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)
#
# iq = 100
# user_age = iq / 5  #erorr
#
# some_value = 5
# some_value *= 10
# print(some_value)
#
# print(type("string"))
# """
# mamad = '''
# WOW
# O O
# ---
# '''
# """
# print(mamad)
#
# print(type(int(str(100))))
#
# weather = " \t it\'s \"kind of\" suny \n hope you have a good day! "
# print(weather)
#
# name = 'Arman'
# age = 55
# print(f'hi {name}. you are {age} years old')
#
# selfish = 'me me me'
#
# greet = 'helllooooo'
# print(greet[0:9])
# print(greet[0:len(greet)])
#
# qoute = 'to be or not to be'
# qoute2 = qoute.replace('be', 'me')
# print(qoute2)
# print(qoute)
#
# birth_year = input('what year were you born?')
#
# age = 2020 - int(birth_year)
#
# print(f'your age is : {age}')
#
# salary = input('how much you ern each year ? ')
# children = input('how many childeren do you have ? ')
#
# mony = int(salary) + 50000*int(children)
#
# print(f'your salary is : {mony}')
#
# name = input('whats your first name ? ')
# L_name = input('whats your last name ? ')
# pass_word = input('enter a pass word : ')
# login_info = name + ' , ' + L_name + ' , ' + pass_word
# print(f'your login info is : {login_info}')
#
# name = input('whats your first name ? ')
# pass_word = input('enter a pass word : ')
# password_length = len(pass_word)
# hidden_password = '*' * password_length
# print(f'{name}, your password, {hidden_password}, is {password_length} leetters long  ')
#
# li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# li2 = ['a', 'b', 'c']
# li3 = [1, 2.2, 'a', True]
# # data structure
#
# #list
# amazon_cart =['notebooks','pen']
# print(amazon_cart[0])
#
# # list slicing
# amazon_cart =[
#     'notebooks'
#     ,'pen'
#     ,'toys'
#     ,'grapes'
# ]
#
# amazon_cart[0]='laptop'
# new_cart = amazon_cart[:] #copy of list
# new_cart[1]='gum'
# print(amazon_cart)
# print(new_cart)
#
# #matrix
# m = [
#     [1,2,3],
#     [3,4,5],
#     [5,6,7]
# ]
# print(m[0][1])
#
# b = [1,2,3,4,5]
#
# #removing
# b.pop()
# print(b)
#
# b = ['a','b','c','d','e']
#
# print(b.index('d',0,4))
#
# # python key word
# b = ['d','a','b','c','d','e']
#
# print(b.count('d'))
#
# b = ['d','a','a','b','c','d','e']
# b.sort()
# b.reverse()
# print(b)
#
# b = ['d', 'a', 'a', 'b', 'c', 'd', 'e']
# b.sort()
# b.reverse()
# # print(b[:])
# # print(b)
# # print(list(range(101)))
#
# # sn = ' '.join(['hi', 'my', 'name', 'is', 'arman'])
# # print(sn)
#
# #list unpacking
# a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)
#
# # None
# weapens = None
# print(weapens)
#
# # dictionary
# # dict
# d5 = {
#     123: [1,2,3],
#     False: 'hello',
#     '[100]': True
# }
# my_list = {
#     'a': [1,2,3],
#     'b': 'hello',
#     'x': True
# },
#  # var = {
#  #     'a': [4, 5, 6],
#  #     'b': 'hello',
#  #     'x': True
#  # }
# print(my_list[0]['a'][2])
# print(d5[False])
#
# d = {
#     'basket' : [1,2,3] ,
#     'greet': 'Hello' ,
#     'age' : 20
# }
#
# d2 = dict(name='Arman')
# print(d.get('age', 55))
# print(d2)
# d.clear()
# d2= d.copy()
# print(d.clear())
# print(d.update({'ages':55}))
# print(d)]
#
# # mt = (1,2,3,4,5,6,7,8,9)
# # nt = mt[1:4]
# # x = mt[0]
# # y = mt[1]
# # x,y,z, *other = (1,2,3,4,5)
# # mt = (1,2,3,4,5,6)
# # print(len(mt)) # index and count
#
# # set
# # my_list = [1,2,3,4,5,5]
# my_set = {1,2,3,4,5,5}
# # my_set.add(100)
# # my_set.add(2)
# # print(my_set)
# # print(set(my_list))
# # print(1 in my_set)
# # print(len(my_set))
# # print(list(my_set))
#
# # n_set = my_set.copy()
# # my_set.clear()
# # print(n_set)
# # print(my_set)
#
# my_set = {3, 4, 5}
# your_set = {3, 4, 5, 6, 7, 8, 9, 10}
# print(my_set.difference(your_set))
# # my_set.discard(5)
# print(my_set)
# print(my_set.difference_update(your_set))
# print(my_set)
# print(my_set & your_set)
# print(my_set.isdisjoint(your_set))
# print(my_set | your_set)
# print(my_set.issubset(your_set))
# print(your_set.issuperset(my_set))
"""