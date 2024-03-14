# eg:3
#? Take values of length and breadth of a
# ? from user and check if it is square or not.
'''
length=int(input("Enter the value : "))
breadth=int(input("Enter the value : " ))
if length==breadth:
             print("its a square")
else:
    print("its not square")
'''
'''
# eg:4
# python program to check whether the
# given integer is a multiple of both 5 and 7
n = int(input("enter the number"))
if n%5==0 and n%7==0:
    print("yes")
else:
    print("no")
'''
#eg:5
# write a program to accept the cost price of a bike and display the
# road tax to be paid
# according to the following criteria:
#           cost price(in Rs)                   Tax
#           > 100000                             15%    +    discount   6%
#           > 50000 and <= 100000       5%
#           <=50000
'''
price = int(input("Enter the price:"))
total = 0
if price>=100000:
    discount = price*(6/100)
    value = price-discount
    tax=value*(15/100)
    total=value+tax
else:
    tax=price*(5/100)
    total=price+tax
print("The onroad cost of bike is: ",total)
'''
#if elif
#eg:1
'''
a=int(input("Enter the value : "))
b=int(input("Enter the value : "))
c=int(input("Enter the value : "))
if a>b and a>c:
    print("A is greater")
elif b>a and b>c:
    print("B is greater")
else:
    print("c is greater")
'''
#eg:2
# A school has following rules for gradind system:
# b.Below 25 - F
# c.25 to 45 - E
# d.50 to 60 - D
# e.60 to 80 - C
# f. Above 80 - A
# Ask user to enter marks and print the corresponding grade.
'''
marks=int(input("Enter the marks: "))
if mark<25:
    print("f")
elif marks>=25 and marks<=45:
    print("E")
elif marks>=50 and marks<=60:
    print("D") 
elif marks>=60 and marks<=80:
    print("C")  
else marks>=80:
    print("A")
'''
# 1 --> short hand if else
# eg:1
'''
a=9
b=60
# if a>b:
#   print("A")
#else:
#   print("B")
'''

#? ---> using short hand if else
# * Rules
#1.)statement inside the if condition have to be present at first
#2.)elif cannot be used in short hand if else
#3.)Always it have to end with else
#print("A") if a>b else print("B")

# ! code to check the given char is vowel and constant
'''
char = input("Enter the char: ")
if char=="a" or char=="e" or char=="i" or char=="o" or char=="u": 
   print("is a vowel")
else:
   print("Its consonant")
'''
# ? or
'''
char = input("Enter the char: ")
stre1 = "aeiouAEIOU"
if char in str1:
    print("vowel")
else:
    print("consonant")
'''
# ! shorthand if else
'''
char = input("Enter the char: ")
str1 = "aeiouAEIOU"
print("vowels") if char in str1 else print("consonent")
'''
# ! ---> elif ladder using short hand if else
#eg:1
# ? find greatest among 3 variables using short hand if else
'''
a=int(input("Enter the value : "))
b=int(input("Enter the value : "))
c=int(input("Enter the value : "))
print("A is greater") if a>b and a>c else print("B is greater")if b>a and b>c   else  print("c is greater")
'''

# ! -------> looping
#looping can be implimented using
#for loop
#while loop

# ---> for loop
# ? for loop is used for iteration, if we know the number of times the loop have to run
# ? It is used to iterate the iterables
# --->eg(string, list, tuple, etc...)
 
# todo ---> syntax for loop

# for syntax in c
# for(i=o;i<10;i++){
#     printf("hello");
#}

# ! for syntax in python
# for userdefined_variable in range(start, end, step):
#    statement
#    statement
#    statement

# ? eg:1
# To print the value from 1 to 10 using for loop
'''
for i in range(0, 100):
    print(i)
'''
# ? eg:2
'''
for val in range(23, 50, 2):
    print(val)
'''
# ? eg:3
# to determent the value
'''
for val in range(10, 2, -1):
    print(val)
'''
#eg:4
# ! print the output of7th multiplication table from 21 to 43
# ---> method:1
'''
for val in range(1, 10+1,):
    print(val*7)
'''
'''
for i in range(1, 11):
    r = 7 * i
    print('7 x', i , '=' ,r)
'''
# ---> method:2
'''
# ans="7 x {} = {}"
#print(ans.format(val, val*7)0
'''
# ---> method:3
'''
for i in range(1, 11):
    print(f"7 x {i}={i*7}")
'''
#eg:5
#  break --> used to terminate the loop
'''
for val in range(1, 10):
    if val ==10:
        break
    print(val)
'''
'''
#eg:6
for val in range(1, 10):
    print(val)
    if val ==7:
        break
'''
#eg:7
'''
for val in range(1, 10):
    if val ==9:
        print(val)
        break 
'''
# ! ---> continue
# eg:1
'''
for val in range(1, 10):
    if val ==8:
        continue
    print(val)
'''
# ! practise problems
# ? print the even the number between 20 to 40
'''
for i in range(20, 41, 2):
    print(i)
'''
'''
for val in range(20, 41):
    if val %2==0:
        print(val)
'''
'''
# ! ----> while loop
# while is used when we do not know the number of times the  loop have to run
# to iterate the non iterable elements while loop is used

# todo syntax

# intialisation
# while condition:
#   statement
#   incre or decre
#eg:1
# to iterate number from 1 to 10
'''
'''
i=0
while i<12:
    print(i)
    i+=1
'''
#eg:2
# to determent  using while loop
'''
i=10
while i>0:
    print(i)
    i-=1
'''
# ! ---> 1-4+9-16+25=15
'''
n=int(input("enter number: "))
sum=0
for val in range(1, n+1):
    sq=val*val
    if val %2!=0:
        sum=sum+sq
    else:
        sum=sum-sq
'''
#for loop practise
# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432
# ---> Assesment
# 1.) cats and mouse:Hacker rank
# 2.) Print the factorla of 8 using for loop
# 3.) Write a program to display sum of odd numbers and even 
# numbers that fall between
# 12 and 37(including both numbers)
# 4.) Write code to print the sum of number using while loop
# n1 = 123 --> 1+2+3 = 6
# 5.) Prine th reverse of given number --> n1= 234 o/p --> 432




















