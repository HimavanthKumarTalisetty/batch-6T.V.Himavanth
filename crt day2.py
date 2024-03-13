'''
a=7,8
print(a)
print(type(a))
'''
'''
#a, b, c = 9, 8, 7, 8
#print(a, b, c)
'''
'''
a, b=c=7, 8
print(a)
print(b)
print(c)
'''
'''
a=b, c = 4,2
print(a, b, c)
'''
'''
#---> swapping of variables
a = 7
b = 5
temp=a #temp=7
a=b     #a=5
b=temp  #b=7
#a=5, b=7
print(a, b)
'''
'''
#eg:2
a=a+b 
b=a-b 
a=a-b
print(a,b)
'''
'''
#eg:3
a, b=b, a #only in python
print(a,b)
'''
'''
#eg:4
a=5
b=6
a=a*b  #a=30
b=a/b  #b=30/6 = 5.0
a=a/b  #a=30/5 = 6.0
print(int(a), int(b))
'''
'''
#eg:5
# id()---> used to find the memory adress of the variable
a=4
b=8
print(id(a))
print(id(b))
'''
'''
#eg:6
#--->keywords
#keywords are reserved words which provides special meaning to
#compiler to interpretor
'''
'''
import keyword
print(keyword.kwlist)
print(type(keyword.kwlist))
print(len(keyword.kwlist))
# to check if the string is keyword or not
#print(keyword.iskeyword("sid"))
'''
'''
if=5
print(if) #error coz if is a keyword
'''
# !--->literals
# Literal is the constant value assinged to a variable
#A variable is considers to be constant when it is defines
#in caps
#a= 78 #a is variable
#A=78 #A is constant
'''
l1 = [6, 7, 8, 0]
L1=96
print(l1)
'''
'''
#hash()---> it creates a hash value for constant datatypes and
#provides error for non constant datatypes
n1 = 89+7j
print(hash(n1))
'''
'''
f1 = [7,8,9]
print(hash(f1)) #error -->list is non-constant or mutuable datatype
'''
'''
'''
'''
a=4
b=2
print(a/b)  #it gives quotient value
print(a*b)   #it gives remainder value
'''
'''
'''
# // --> floor devision
#eg-1
'''
a=765433
b=19
print(a/b)
'''
'''
#! ** --> used for power of a number
#print(2**4) #-->16

#! Assignment --> +-=, -=, /=, //=, **=, &=, |=
#eg:1
'''
'''
a=8
a+=2
print(a)
'''
'''
a=30
a-=5
print(a)
'''

# !comparsion --> ==, >, <, !=, <=, >=
#eg:1
'''
a=8
b=7
print(a>b) # True
'''
#eg:2
'''
a=6
b=6
print(a==b)
'''
# ! Bitwise operator --> &, |, ^, ~, <<, >>
#eg:1
'''
a=7
b=4
print(a&b)
'''
'''
#2^4 2^3  2^2  2^1  2^0
# 16   8   4    2    1
#----------------------
# 0    1    0    0   0
# 0    0    1    1   1
# 0    0    1    1   0
# 0    0    1    0   1
# 0    0    1    0   0
# 0    0    0    1   1
# 0    0    0    1   0
# 0    0    0    0   1
'''
#EG:2
'''
a=5
b=7
print(a|b)
'''
# ~ --->
'''
a=678
print(~a)
'''
'''
# <<, >>
# print(5>>1)
# 16>4
'''

# Logical operator ---> used to compare the expressions
# and, or, not
#eg:1
'''
a = 6
#print(a>3 and a<10)
'''
eg:2
'''
a=6
#print(a>7 or a<30)
'''
eg:3
'''
a = 7
print(not(a>8 and a<8))
'''
# ! identity operator
# it is used to compare the memory location where value is stored
# is , is not
#eg:1
'''
a=9
b=98
print(a is b)
'''
#eg:2
'''
a = [1,2,3]
b = [1,2,3]
print(a is b)
'''
#eg:3
'''
a = (1,2,3)
b = (1,2,3)
print( a is b)
'''
#eg:4
'''
a = [1,2,3]
b = [1,2,3]
print( a is not b)
'''
# !--->Membership operator
#in, not in
'''
l1 = [22,48,30,29,28,40,32]
num=eval(input("Enter the number : "))
print(num in l1)
'''
'''
# num = 678
#print(8 in num)  #errror
'''
# ! conditional statement
# if, elif, else
#eg-1
# --->
'''
a = 6
if a:
    print("hello")
'''
#eg:2
'''
a=12
if a>3:
    print("hima")
else:
    print("no")
'''
#eg:3
'''
if 7>8:
    print("yes")
else:
  print("no")
'''
#eg:4
'''
a=0
a=None
a=False
a=""
if a:
    print("yes")
else:
    print("no")
'''
# a number is even or odd
'''
a=int(input("Enter the number: "))
if a%2==0:
    print("even")
else:
    print("odd")
'''
# name, age ,nationality
# 18 above, Indian
age=int(input("Enter the age: "))
name=input("Enter the name:")
nationality=input("Enter the nation:")
if age >18 and nationality=="Indian":s
      print("Eligible")
else:
      print("Not Eligible")

















































