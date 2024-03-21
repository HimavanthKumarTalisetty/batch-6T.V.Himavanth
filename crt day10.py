# Eg:1
# We can achieve polymorphism in 2 ways
# 1.) Method overloading --> It is not possible in python
# 2.) Method overloading

# 1.) Method overloading
# Polymorphism in classes
'''
class bank:
    def ratio(self):
        print("All banks has repo rate")
class SBI(bank):
    def ratio(self):
        print("SBI rate is 9%")
class IOB(bank):
    def ratio(self):
            print("IOB ratio is 7.5%")
i = IOB()
i.ratio()
s = SBI()
s.ratio()        
'''
# Eg:2
'''
class USA:
    def language(self):
        print("English")
    def capital(self):
        print("Washing ton")
class India(USA):
    def language(self):
        print("None")
    def capital(self):
        print("New Delhi")
I = India()
I.language()
I.capital()
'''
# Eg:3
# Polymorphism using objects
# c1, c2 --> c1 = print(c1).print(c2)
# f1, f2
# M -->1
'''
class c1:
    def f1(self):
        print("Class 1")
class c2(c1):
    def f2(self):
        super().f1()
        print("Class 2")
obj1 = c2()
obj2 = c1()
'''
# M --> 2
'''
class c1:
    def f1(self):
        print("Class 1")
class c2(c1):
    def f2(self):
        print("Class 2")
obj1 = c2()
obj1.f1()
obj2 = c1()
obj2.f1()
'''
# eg:4
'''
class c1:
    def f1(self):
        print("Class 1")
class c2(c1):
    def f2(self):
        super().f1()
        print("Class 2")
obj1 = c2()
obj1.f1()
def display(a):
    a.f1()
display(obj1)
display(obj2)
'''
# * Changing the functionality of buitin functions
# Eg:5
'''
class shopping:
    def __init__(self, l1):
        self.items = l1
    def __len__(self):
        length = len(self.items)
        return length
s = shopping([1,2,3,4,5])
print(len(s))
'''
# eg:6
'''
a = int(input("Enter a number"))
b =int(input("Enter a number"))
print(a+b)
'''
# EG:-7
'''
a = 9
b = 6
print(a+b)
print(a.__sub__(b))
'''

# ! ---> Method overloading
# ! Eg:1
'''
class suming:
    def add(self, a, b):
        print(a+b)
    def add(self, a, b, c):
        print(a+b+c)
s = suming()
s.add(4, 5, 1)
'''

# Eg:2
'''
class summing:
    def add(self, a=None, b=None, c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
        elif a!=None and b!=None:
            print(a+b)
        else:
            print(a)
obj = summing()
obj.add(3)
obj.add(4, 6)
obj.add(9, 46, 5)
'''

# 1 ---> Abstraction
# The process of hiding the implimentation details is abstraction
'''
from abc import ABC, abstractmethod
class shapes(ABC):
    @abstractmethod
    def sides(self):
        print("All shapes have sides except circle")
class triangle:
    def sides(self):
        print("3 sides")
    def name(self):
        print("i am in triangle")
    def sides(self):
        pass
class square:
    def square(self):
        print("4 sides")
tr = triangle()
tr.sides()
tr.name()
'''
# ! Rule to define abstract class1
# 1.) A bstract class cannot be instantiated
# 2.) From abc import ABC, abstractmethod
# 3.) Subclass the normal class with ABC
# 4.) Convert the normal method inside the abstract class to abstract method
# 5.) All the child classes have to be subclassed with abstract class
# 6.) The abstract method should be present in the child classes
# Eg --->2
'''
def decor(func):
    def inner():
        str1 = func()
        return str1.upper()
    return inner()
def greet():
    return 'good morning'
print(decor(greet))
'''
# Eg:-3
# super() --> used to access the parent class method from child
#             class method
'''
from abc import ABC,abstractmethod
class c1(ABC):
    @abstractmethod
    def m1(self):
        print("This is abstract class")
class c2(c1):
    def m2(self):
        super().m1()
        print("I am child 1")
    def m1(self):
        pass
class2 = c2()
class2.m2()
'''
# Eg:-4
'''
from abc import ABC, abstractmethod
class password(ABC):
    @abstractmethod
    def pwd(self):
        pwd = "www@143"
        return pwd
class login(password):
    def validate(self, name, password):
        if super().pwd() == password:
            print("Welcome", name, '||')
            print("Login Successfull")
        else:
            print("Please check the password")
    def pwd(self):
        pass
Login = login()
name = input("Enter the name : ")
pwd = input("Enter the password : ")
Login.validate(name, pwd)
'''

# ! Encapsulation
# ----> Eg:1
'''
class car:
    __name = "BMW" 
    print(__name)
c1 = car()
print(c1.name)
c1.name = "Audi"
print(c1.name)
'''

# Eg:2
# ? Accessing private the data outside the class
'''
class c1:
    __phone = '9652572870'
    def display(self):
        print(self.__phone)
c = c1()
c.display()
'''
# Eg:3
# ? declare private method
'''
class class1:
    def __m1(self):  # Private method
        print("I am private method")
    def __init__(self):
        self.__m1()
c = class1()
c.__m1() #error
'''

# ? nested class
'''
class class1:
    class class2:
        name = "Hima"
        def display(self):
            print(self.name)
    obj1 = class2()
obj = class1()
obj.obj1.display()
'''
# ! ---> TASK
# 1.) Write the code for the below tasks using function
#     d1 = {"shirt":1000, "pant":1500, "Shoes":900, "handkey":30}
#     a.) Find the min and max priced product
#     b.) Find the product starts with 's' and 'S'
'''
d1 = {"shirt":1000, "pant":1500, "Shoes":900, "handkey":30}
for val in d1:
    if d1[val] == min(d1.values()):
        print(val)
for val in d1:
    if d1[val] == max(d1.values()):
        print(val)
for val in d1:
    if val.startswith('s') or val.startswith('S'):
        print(val)
'''
    
        











