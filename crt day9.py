# ! Constructors
# ? Eg:2
'''
class profile:
    def __init__(self):
        print("hello world")
obj = profile()
obj.__init__()
'''
# Eg:3
# Parameterised constructor
'''
class profile:
    def __init__(self, id, name, age):
        print(id, name, age)
obj = profile(1, "\nHima", 21)
'''
# Eg:4
'''
class c1:
    email = "talisetty@gmail.com"
    def m1(self):
        name = "Hima"
        place = "Yerraguntla"
        print(name, place)
        print(self.email)
object =  c1()
object.m1()
'''
# Eg:5
'''
class c1:
    def m1(self):
        name = "Hima"
        age = 21
        return name, age
    def display(self):
         print(self.m1())
object = c1()
object.display()
'''
# Eg:6
# To use the variable inside the constructor in another methods
'''
class class1:
    def __init__(self):
        self.name = "Hima"
        self.email = "talisetty@gmail.com"
        # return name, email # error ---> cannot use return witth constructor
    def display(self):
        print(self.name, self.email)
c1 = class1()
c1.display()
'''

# ! ----> Inheritance
# The process of utilizing the methods and attributes of parent class
# throught the object of child class it is called as inheritance

# ? 5 types of Inheritance
# Single Inheritance
# Multilevel Inheritance
# Multiple Inheritance
# Hybrid Inheritance
# Heirarichal Inheritance

# *Single Inheritance
# ? It is only one parent class and only one child class
# ! Eg:1
'''
class parent:
    def m1(self):
        print("I am parebnt class")
class child(parent):
    def m2(self):
        print("Iam child class")
obj = child()
obj.m1()
'''
# eg:2
'''
class c1:
    def __init__(self):
        print("Iam akash from parent class")
class child(c1):
    pass
obj = c1()
'''
#Eg:3
'''
class parent:
    name = "Hima"
class child(parent):
     name = "name1"
     def display(self):
        print(self.name)
d = child()
d.display()
'''

# ! Multilevel inheritance
# ? Eg:1
'''
class voice:
    def sound(self):
        print("All the animals have their own voices")
class dog(voice):
    def dog_voice(self):
        print("bark")
class cat(dog):
    def cat_voice(self):
        print("Meow")
class parrot(cat):
    def parrot_voice(self):
        print("speak")
all = parrot()
all.dog_voice()
all.cat_voice()
all.sound()
all.parrot_voice()
'''
# ?Eg:2
'''
class honda_city:
    def engine_specs(self, cc, Hp, torque, fuel_type, num_of_pisition):
        printt(cc, Hp, torque, fuel_type, num_of_pisition)
    class honda_city:
        def engine_specs(self, cc, Hp, torque, fuel_type, num_of_pisition):
            printt(color, weight, height, length, vehicle_type)
    class amaze(honda_city):
        def amaze_engine_specs(self, cc, Hp, torque, fuel_type, num_of_pisition):
            printt(cc, Hp, torque, fuel_type, num_of_pisition)
            def amaze_body_specs(self, cc, Hp, torque, fuel_type, num_of_pisition):
                printt(color, weight, height, length, vehicle_type)
    class civic(amaze):
        def civic_engine_specs(self, cc, Hp, torque, fuel_type, num_of_pisition):
            printt(cc, Hp, torque, fuel_type, num_of_pisition)
            def civic_body_specs(self, cc, Hp, torque, fuel_type, num_of_pisition):
                printt(color, weight, height, length, vehicle_type)    
    class Honda(civic):
        pass
honda = Honda()
honda.honda_city_engine_specs(1500, 230, 2979, "petrol", 4)
honda.civic_body_specs("white", 2000, 5.5, 8, "Hatchback")
'''
# ----> Multiple inheritance
# ? It has multiple parent and 1 child
# Eg:1
'''
class white_petrol:
    def function_w(self):
        print("used to Airplans")
class organic_petrol:
    def function_o(self):
        print("Used for Bike, Cars")
class premium_petrol:
    def function_p(self):
        print("sport cars, bikes")
class petrol(white_petrol, organic_petrol, premium_petrol):
    def defanation(self):
        print("Petrol types")                              
p= petrol()
p.defanation()
p.function_o()
'''
# Eg:2
'''
class addition:
    def add(self, a, b):
        print(a+b)
class subtraction:
    def sub(self, a, b):
        print(a-b)
class multiply:
    def mul(self, a, b):
        print(a*b)
class division(addition, subtraction, multiply):
    def div(self, a, b):
        print(a/b)
calc = division()
calc.add(3, 4)
calc.sub(6, 7)
calc.mul(5, 2)
calc.div(1, 10)
'''

# ---> Heirarical inheritance
# ? The one parent classe will ascts as parent for all the child classes
# Eg:1
'''
class catagory:
    def cat_name(self):
        print(weight)
        def wight(self, weight):
            print(weight)
        def display(self, color, taste):
            print(color, taste)
class Tomato(catagory):
    def tomato_specs(self):
        colour="black"
        taste = "neutral taste"
        self,display(color, taste)
class carrot(catagory):
    def carrot_specs(self):
        colour="green"
        taste = "sweet"
c = carrot()
c.carrot_specs()
c.weight("30gms")
t =tomato()
t,tomato_specs()
t.weight("20gms")
'''

# ! Hybrid inheritance
# ? The combination of above 4 inheritance is called Hybrid inheritance
'''
class c1:
    def m1(self):
        print("class 1")
class c2:
    def m2(self):
        print("class 2")
class c3(c2):
    def m3(self):
        print("class 3")
class c4(c2):
    def m4(self):
        print("class 4")
        
class c5(c3):
    def m5(self):
        print("class 5")

class c6(c5, c4, c2, c1):
    def m6(self):
        print("class 6")
obj = c6()
obj.m1()
obj.m2()
obj.m3()
'''

# ! -----> Polymorphism
# ? Poly  -  many, morph ---> form
# A function which has the ability to perform more than 1 functionality
# Then it is considered to be as polymorphism

# Polymorphism in builtin functions
# len() --> which is used to find the length of list, tuple, dict etc..
# index()
# max()
# min()
# count()
# pop()
# and more...

# * Polymorphism in operaters
# +
'''
print(8+8)
print("k"+'1')
print([1,2,3]+[5,6])
'''

# *
'''
print(6*5)
l1 = [1,2,3,4]
print(*l1)
`# def f1(*args)
l1 = [1,2,3,4]
print(l1*10)
'''

# Polymorphism in classes
# We can achieve polymorphism in 2 ways
# 1.) Method overloading --> It is not possible in python
# 2.) Method overloading
































































