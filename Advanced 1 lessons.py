# Advanced 1
# # # OOP (whats OOP ?)
# class BigObject:
#     # code
#     pass
#
#
# obj1 = BigObject()
# obj2 = BigObject()
# obj3 = BigObject()
# print(type(obj1))

# class PlayerCharacter:
#     membership = True
#
#     def __init__(self, name='ananymous', age=0):
#         if (age > 18):
#             self.name = name
#             self.age = age
#
#     def shout(self):
#         print (f'my name is {self.name}')
# return 'done'

# def run(self, hello):
#     print (f'my name is {self.name}')


# player1 = PlayerCharacter('tom', 10)
# player2 = PlayerCharacter()
# player1.attack = 150
# player2.attack = 50
# print(player1.shout())

# print(player1.name)
# print(player1.age)
# print(player1.run())
# print(player1.attack)
# print(player1.membership)
# print(player1.shout())
# print (player1.run('hello'))

# print(" ")
#
# print(player2.name)
# print(player2.age)
# print(player2.run())
# print(player2.attack)
# print(player2.membership)
# print(player2.shout())

# class PlayerCharacter:
#     membership = True
#
#     def __init__(self, name='ananymous', age=0):
#         # if (age > 18):
#         self.name = name
#         self.age = age
#
#     def shout(self):
#         print (f'my name is {self.name}')
#
#     @classmethod
#     def adding_things(cls, num1, num2):
#         return cls('Teddy', num1 + num2)
#
#     @staticmethod
#     def adding_things(num1, num2):
#         return num1 + num2
#     # player1 = PlayerCharacter('tom', 20)
#     # print(player1.adding_things(2,3))
#
#
# player3 = PlayerCharacter.adding_things(2, 3)
#
# print(player3.age)

# # # private???
# class PlayerCharacter:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     def run(self):
#         print ('run')
#
#     def speak(self):
#         print (f'my name is {self._name}, and Iam {self._age} yeats old.')
#
#
# player1 = PlayerCharacter('Arman', 25)
# print (player1.speak())

# users
# # # INHERITANCE
# class User:
#     def sign_in(self):
#         print ('logged in')
#
#     def attak(self):
#         print ('do nothing')
#
#
# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#
#     def attak(self):
#         # User.attak(self)
#         print (f'attaking with power of {self.power}')
#
#
# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
#
#     def attak(self):
#         print (f'attaking with arrows: arrows left {self.num_arrows}')
#
#
# #
# #
# Wizard1 = Wizard('Merlin', 50)
# archer1 = Archer('Robin', 100)
#
# print (Wizard1.attak())
#
# for char in [Wizard1, archer1]:
#     char.attak()
#
# def player_attak(char):
#     char.attak()
#
#
# player_attack(Wizard1)
# player_attack(archer1)
#
# print(isinstance(Wizard1, object))
#
# Wizard1.attak()
# archer1.attak()
# archer1.sign_in()

# # #  Exercse
# class SuperList(list):
#     def __len__(self):
#         return 1000
#
#
# super_list1 = SuperList()
# print (len(super_list1))
# super_list1.append(5)
# print (super_list1[0])
# print (issubclass(SuperList,list))

# # #  MULTIPLE INHERITANCE
# class User:
#     def sign_in(self):
#         print ('logged in')
#
#     def attak(self):
#         print ('do nothing')
#
#
# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
#
#     def attak(self):
#         # User.attak(self)
#         print (f'attaking with power of {self.power}')
#
#
# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows
#
#     def attak(self):
#         print (f'attaking with arrows: arrows left {self.num_arrows}')
#
#     def run(self):
#         print ('Ran really fast')
#
#
# class BoostMan(Wizard, Archer):
#     def __init__(self, name, power, arrows):
#         Archer.__init__(self, name, arrows)
#         Wizard.__init__(self, name, power)
#
#
# b1 = BoostMan('Arman', 1000, 2000)
# print (b1.sign_in())

# # # M R O -  Method Resolution Order
# class A:
#     num = 10
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     num = 1
#
#
# class D(B, C):
#     pass
#
# print (D.mro())
# # #  Exercse
# class X: pass
#
#
# class Y: pass
#
#
# class Z: pass
#
#
# class A(X, Y): pass
#
#
# class B(Y, Z): pass
#
#
# class M(B, A, Z): pass
#
# print (M.mro())
