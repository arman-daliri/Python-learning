# # # DECORATORS # # #
# Decorators super charge our functions
# Decorator Pattern
# def my_decorater (func):
#     def wrap_func (*args, **kwargs):
#         func (*args, **kwargs)
#
#     return wrap_func
#
#
# @my_decorater
# def hello (greeting, emoji = ':('):
#     print (greeting, emoji)
#
#
# # @my_decorater
# # def bye ():
# #     print ("see you later")
#
#
# hello ('hiiii')

# Decorator Performance
# from time import time
#
#
# def performance (fn):
#     def wrapper (*args, **kwargs):
#         t1 = time ()
#         result = fn (*args, **kwargs)
#         t2 = time ()
#         print (f'took {t2 - t1} s')
#         return result
#
#     return wrapper
#
#
# @performance
# def long_time ():
#     for i in range (1000000000):
#         i + 2
#
#
# long_time ()
##############################################################

# # # ERRORS HANDELING # # #
# def adadad()
#     pass      # it gave syntaxError

# def adadada():
#     1 + name
# adadada()       # it gave NameError

# erorr handeling exampel
# while True:                         # this help to make sure about a true answer
#     try:                            # this help to handel an error
#         age = int (input ('what is your age? '))
#         10 / age                    # this is a bugy code
#         # raise valueError('hey cut it out') # It makes our own error , it can be any type of error
#     except ValueError:              # this is a handel code for error
#         print ('Please enter a number')
#         continue                    # throw the code to the try part
#     except ZeroDivisionError:       # this is a handel code for error
#         print ('please enter a number higher than zero.')
#         break                       # go to try part
#     else:
#         print ('Thank you!!!')
#         break
#     finally:
#         print ('Ok , finally im done.')

###############################################################
# # # Generators # # #
# Range is a generator ,, what range does?
print (range (100))
print (list (range (100)))  # this is doing the code in next line :::\

def make_list (num):
    result = []
    for i in range (num):
        result.append (i)
    return result


my_list = make_list (100)
print ((list (range (1000))))
"""
NOTE !!!
 BUT IT IS CREATES MEMORY PLACE FOR EACH PART OF THE LIST
 THIS IS ONLY MAKE THE MEMORY FULL OF NUMBERS
 WE USE GENERATOR FOR DO THIS TASK FOR ONLY ONE TIME
 SO A GENERATOR IS A SUBSET OF AN ITERABLE
"""


def generator_function (num):
    for i in range (num):
        yield i * 2  # YIELD PAUSES THE FUNCTION AND COMES BACK IT WHEN WE DO SOMTHING TO IT WICH IS CALLED NEXT.


g = generator_function (100) # if we keep with 1 it giv us a StopIteration error
next (g)  # I = 1
next (g)  # I = 2
next (g)  # I = 3
print (next (g))

for item in generator_function (1000):
    print (item)



# # # Under the hood of GENERATORS # # #
# # # FOR LOOP
def s_for (iterable):
    iterator = iter (iterable)
    while True:
        try:
            print (iterator)
            print (next (iterator))
        except StopIteration:
            break


s_for ([1, 2, 3])

# # # Range
class MyGen ():
    current = 0

    def __init__ (self, first, last):
        self.first = first
        self.last = last

    def __iter__ (self):
        return self

    def __next__ (self):
        if MyGen.current < self.last:
            num = MyGen.current
            MyGen.current += 1
            return num
        raise StopIteration


gen = MyGen (0, 100)
for i in gen:
    print (i)

# # # EXERCISE FIBONACCI NUMBERS
def fib (number):
    a = 0
    b = 1
    for i in range (number):
        yield a
        temp = a
        a = b
        b = temp + b


for x in fib (20):
    print (x)


###LIST###
def fib2 (number):
    a = 0
    b = 1
    result = []
    for i in range (number):
        result.append (a)
        temp = a
        a = b
        b = temp + b
    return result


print (fib2 (20))
