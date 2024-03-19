#eg:3
'''
def profile(name, age, place):
    txt = "My name is {}. I am {} years old. I am from {}."
    print(txt.format(name, age, place))
profile("Himavanth", 21,"YERRAGUNTLA")
'''
#eg:4
'''
# ? Function with return statement
def f1():
    z=8
f1()
print(z)
'''
# ! return
#1.) A variable declared inside the function can be accessed outside the function
#using return
#2.) return does not prrint anything
#3.) we cannot write any code below return statement
#eg:5
'''
def f1(a, b):
    c = a*b
    return c
# print(f1(6, 8))
obj = f1(6, 8)
obj1 = f1(4, 6)
def gracemark(object):
    print(object)
    gracemark(obj)
    gracemark(obj1)
'''
# eg:6
# 123 ----> write a palindrome
'''
def palindrome (n):
    string = str(n)
    rev = str(n)[::-1]
    if string==rev:
        print(n, "is a palindrome")
    else:
        print(" is not a palindrome")
a = int(input("Enter the value: "))
palindrome(a)
'''     
# ? Based on the declaration of parameter and args
# ? functions are divided into 5 catageries

#Positional args
#keyword args
#default args
#variable length args
# keyword variable length args

# * positional args
# ---> The position of parameter have to be same as position as arguents
#Eg:1
'''
def profile(name, phone, mark):
    txt = "\nMy name is {}. My phone number is {}. \n I got {} marks."
    print(txt.format(name, phone, mark))
profile("Himavanth", 100, 99)
'''
# ! Keword args
# ---> In overcome the disadvantage of positin args, we use keyword args
# ---> It is the process of intialising the parameter with the args while calling the function
# Eg:1
'''
def profile(name, phone, mark):
    txt = "\nMy name is {}. My phone number is {}. \n I got {} marks."
    print(txt.format(name, phone, mark))
profile(name-"Himavanth", mark-99, phone-9652572870)
'''
# todo ----> Exception of keyword args function
'''
def profile(name, phone, mark):
    txt = "\nMy name is {}. My phone number is {}. \n I got {} marks."
    print(txt.format(name, phone, mark))
# profile(name="Hima", phone=9652572870, mark=97) # error
# profile(9652572870, name-"Hima", mark=97)       # error
profile("Hima", mark=97, phone=9652572870)     
'''
# Default args
# The method of assigning the argument to the parameter while declaring the
# function
# Eg:1
'''
def profile(name, phone, place):
    txt = "\nMy name is {}. My phone number is {}. I am from {}."
    print(txt.format(name, phone, place))
profile("Hima", 9652572870, "Tirupathi")
'''
# eg:2
'''
def profile(name, phone, place):
    txt = "\nMy name is {}. My phone number is {}. I am from {}."
    print(txt.format(name, phone, place))
    if place=="Tirupathi":
        print("maps is correct")
    else:
        print("maps is not matched")
profile("Hima", 9652572870, "Tirupathi")
'''

# * variable length args
# To pass more than 1 arg to a parameter means we use variable length args
# To convert normal parameter to variable length parameter, add * to otherprefix of parameter
# ! Eg:1
'''
def profile(*name):
    for val in name:
        print("My name is",val)
profile("Hima", 'akash', 'vijay')
'''
# Eg:2
'''
def profile(age, *name):
    for val in name:
        print("My name is", val, "My age is", age)
profile(20,"Hima", 'akash', 'vijay')
'''

# ---> * Keyword variable length args
# Kwargs --> Which is used to provide the args in the form of key value pair.
# Eg:1
'''
def price(price_list):
print(price_list)
price(shirt=1000, iphone=80000)
'''
#Eg:2
'''
d1 = {"a":100, "b":200, "c":300}
d1 = dict(a=100, b=600, c=900)
print(d1)
'''

# ---> Assesment
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# 2.)Find the uncommon words from 2 strings
# # s1 = "Hello how are you"
# s2 = "Hello how is"
# 3.)Wrire a code print the 8th fibanochi number

# ---> Answers
# 1.) Write a Python script to generate and print a dictionary that 
# contains a number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) :
# Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
# ---> Code
# M ---->1
'''
n = int(input("input a number: "))
d = dict()
for x in range(1, n+1):
     d[x] = x * x
print(d)
'''
# M ---> 2
'''
def dict1(n):
    d1 = {}
    for val in range(1, n+1):
        d1[val] = val**2
        print(d1)
        dict1(5)
'''
# 2.)Find the uncommon words from 2 strings
# # s1 = "Hello how are you"
# s2 = "Hello how is"
# ---> Code
'''
def uncommon_words(s1, s2):
    A = set(s1.split())
    B = set(s2.split())
    uncommon = list(A.symmetric_difference(B))
    return uncommon
s1 = "Hello how are you"
s2 = "Hello how is"
uncommon = uncommon_words(s1, s2)
print(uncommon)
'''
# 3.)Wrire a code print the 8th fibanochi number
# ---> Code
'''
def fibonacci(n):
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i-1] + fib[i-2])
    return fib[n-1]
n = 8
print(f"The {n}th Fibonacci number is
'''

# ! --------> Object oriented programming
# The paradigms of objects oriented programming are
# Class
# Objects
# Inheritance
# Polymorphism
# Abstraction
# Encapsulation

# ! Class is a blue print of an object
# Eg:1
'''
class c1:
    name1 = "Hima"
    print(name1)
'''
# Eg:2
'''
class person:
    name = "Hima"
c = person()
print(c.name)
'''

# Eg:3
# Create a method
# When the function is created with a  class is called as method
'''
class person:
    def display(person):   
        print("Hello welcome to classes")
p = person()
p.display()
'''
# Eg:4
# ! Method with parameter
'''
class person:
    def display(person, name, age):
        print(name, age)
p = person()
p.display("Hima", 25)
'''
# Eg:5
# M --->1
'''
class person:
    name = "Hima"  
    def display(person):
        print(person.name)
p = person()        
p.display()    
'''
# M --->2
'''
class person1:
    fname = "Hima"
    Iname = "Himavanth"
    def first_name(self):
        print(self.fname)
    def full_name(self):
        print(self.fname+" "+self.Iname)
p = person1() 
p.first_name()
p.full_name()
'''
# Eg:6
# Constructor --->_init_()
# This is a special method which has the ability to execute itself without
# Calling it manually through the process of
'''
    def __init__(self):   # constructor method
        print("hey akash")
p = profile()   # throught this process
'''
    












