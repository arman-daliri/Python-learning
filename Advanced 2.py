# # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # Functional programming # # # # # #
# # # Pure functions
def ml2(li):
    nl = []
    for item in li:
        nl.append(item * 2)
    return nl


print (ml2([1, 2, 3]))

# # # # # # # # # # # # # # # # # # # # # # # # # #

# Same input always return Same output
# NO Side Effect

# # # # # # # # # # # # # # # # # # # # # # # # # #

# def ml2(li):
#     nl = []
#     for item in li:
#         nl.append(item * 2)
#     return print (nl)  # This line have side effect
#
#
# (ml2([1, 2, 3]))

# # # # # # # # # # # # # # # # # # # # # # # # # #

# nl = []  # This line have side effect
#
#
# def ml2(li):
#     for item in li:
#         nl.append(item * 2)
#     return nl
#
#
# nl = ""  # This line have side effect
# print (ml2([1, 2, 3]))

# # # # # # # # # # # # # # # # # # # # # # # # # #

# # # # Map , filter , Zip , reduce # # # #

# # # Map
my_list = [1, 2, 3]  # out of function


def ml2(item):
    return item * 2
    # nl = []
    # for item in li:
    #     nl.append(item * 2)
    # return nl


# print (map(ml2, [1,2,3]))
print (list(map(ml2, my_list)))


print (my_list)  # map have not effect to this list

# # # Filter
my_list = [1, 2, 3]


def ml2(item):
    return item * 2


def odd (item):
    return item % 2 != 0


print (list(filter(odd, my_list)))
print (my_list)

# # # ZIP
my_list = [1, 2, 3]
your_list = [10, 20, 30]
thire_list = [5, 4, 3]

print (list(zip(my_list, your_list, thire_list)))

print (my_list)
print (your_list)
print (thire_list)

# # # reduce
from functools import reduce

my_list = [1, 2, 3]


def acc(ac, item):
    print (ac, item)
    return ac + item


print (reduce(acc, my_list, 1))
print (my_list)

# # # # # # # # # # # # # # # # # # # # # # # # # #

# # # Lambda expressions
lambda param: action(param)
from functools import reduce

my_list = [1, 2, 3]
# I made previous  funcs  with lambda in next line not matter its filter or map o ... #
print (reduce(lambda ac, item: ac + item, my_list))
print (my_list)

# # # Exercise Lambda expressions
my_list = [5, 4, 3]

new = list(map(lambda num: num ** 2, my_list))
print (new)

# # # list sorting
a = [(0, 2), (4, 3), (9, 9), (10, -1)]
a.sort(key=lambda x: x[1])
print (a)

# # # # # # # # # # # # # # # # # # # # # # # # # #

# # # Comprehensions
#### LIST, set, dictionary
#### for list make it on a []
#### for set make it on a {}
ml = [char for char in 'python']
ml2 = {num for num in range(0, 101)}
ml3 = [num ** 2 for num in range(0, 101)]  # some of nums are not even yet
ml4 = [num ** 2 for num in range(0, 101)
       if num % 2 == 0]
print (ml)
print (ml2)
print (ml3)
print (ml4)

# # # # dictionary
simp_dic = {
    'a': 1,
    'b': 2
}
md = {k: v ** 2 for k, v in simp_dic.items()
      if v % 2 == 0}
md2 = {num: num * 2 for num in [1, 2, 3]}
print (md)
print (md2)

# # # Exercise Comprehensions
sl = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list(set([x for x in sl if sl.count(x) > 1]))
print (duplicates)
