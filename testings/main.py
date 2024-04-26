# def process_display(func):

#     def wrapper(*args, **kwargs):

#         print("{} started execution".format(func. func_name))

#         func(*args)

#         print("() finished execution". format (func.func_name))

#     return wrapper

# @process_display 
# def names_processor():

#     names =list(filter(lambda x: x if x.startswith('B') or x.startswith('R') else None, ["Brian", "Roy", "William", "Rex", "Peter", "Alex", "Boyle", "Ronald"]))



#     return names

# try:

#     names=names_processor()

# except TypeError: 
#     print("TypeError occured")

# except AttributeError: 
#     print("AttributeError Occured")

# else:

#     print(names) 
# finally:

#     print("Finally executed")

# def generate_string(mystr):
#     for i in mystr: 

#         yield i

# def text (mytext): 
#     for i in mytext:

#         yield i*2

# mystr="abcde"

# print("".join(text (generate_string (mystr))))

# class Vehicle:

#     name="BMW"

# def _str_(self):



#     name="Audi"

#     return name

# def __init__(self): 
#     self.name="Mercedes"

# v=Vehicle()

# print (v.name)

# class Stock:

#     stockprice=700

#     def __init__(self):


#         self.__stockprice=1000

#     def sell_stock (self):

#         print("Price of the stock is {}".format(self.__stockprice))

#     def broker_bargain(self,price): 
#         self.__stockprice=price

# s=Stock()

# s.sell_stock()

# s.__stockprice= 1500 
# s.sell_stock()

# s.broker_bargain(1700) 
# s.sell_stock()

# try:

#     with open ("abc.txt", "w") as f:

#         for i in range(2):

#             f.write("Hello World\n") 
#             f=open("abc.txt", "w")

#         for i in range(3):

#             f.write("Hello Universe\n")

#             f.close()

#         with open("abc.txt") as f: 
#             print(f.readline())

# except IOError:

#     print("Error reading the file")

from functools import reduce

numbers = [1,2,3,4,5] 

print(reduce((lambda x, y: x*y), numbers))