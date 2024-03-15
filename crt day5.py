# ! ----> common functions for list:
#eg:1
'''
l1 = [6, 7, 8, 9, 0]
print(len(l1))
'''
#eg:2
'''
l1 = [6, 7, 8, 9, 0]
print(max(l1))
'''
# eg:3
'''
l1 = [6, 7, 8, 9, 0]
print(min(l1))
'''
#eg:4
'''
l1 = [6, 7, 8, 9, "p", "u"]   # --> error coz its a combination of int and string
print(max(l1))
'''
#eg:5
'''
l1 = [6, 7, 8, 9, "p", "u"]   # --> error coz its a combination of int and string
print(max(l1))
'''
# eg:6
# index () --> to get index value of specific element
'''
l1 = [6,7,8, 9,0,8.89,-5, 0.78]
print(l1.index(9))
'''
#eg:7
'''
l1 = [6,6,6,7,8,9,0, 8.89, -5, 0.78]
count() --> how many num of times an element is repeated
print(l1.count(6)0
'''
# ! some functions which is specially used for list
# to add element inside list
# ? insert(index_value,element) --> to add element at specific index position
'''
l1 = [6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]
l1.insert(2, "cars")
print(l1)
'''
# ? To delete element from list
'''
l1 =  [6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]   
l1.pop()
print(l1)
'''
# * pop() ---> last element will be deleted
'''
l1 =  [6,6,6, 7, 8, 9, 0, 8.89, -5, 0.78]   
l1.pop()
print(l1)
'''
# pop(inde_valve) --> used to delete element at specific index
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.pop(5)
print(l1)
'''

# remove(element) --> used to delete element directly
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.remove(6.76)
print(l1)
'''
# clear() --> to complete delete all element in list
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
l1.clear()
print(l1)
'''
# del -> to delete the list
'''
l1 = [2,3,2,3,4,32,6.76,98.5,-94]
del l1
print(l1)
'''

# ? ---> join 2 lists
'''
l1 = [8, 4, 0]
l2 = ["h", "i", "m", "a"]
print(l1+l2)
'''

# ! or
# * extend() --> to combine 2 lists
'''
l1 = [8, 4, 0]
l2 = ["h", "i", "m", "a"]
l1.extend(l2)
print(l1)
'''
# ---> copy()
'''
l1 = [6, 7, 8, 9, 3]
l2 = l1.copy()
print(l2)
print(l1)
print(id(l1))
print(id(l2))
'''
# ! diff between shallow copy and deep copy
# shallow copy
import copy
'''
l1 = [8, 9, 0, [5, 6], [3, 2, 1]]
l2 = copy.copy(l1)
l1.append(890)
print(l1)
print(l2)
'''
# * deep copy
'''
import copy
l1 = [8, 9, 0, [5, 6], [3, 2, 1]]
print(l1[-1][1])  
l1[-1].append("jeep")
l2 = copy.deepcopy(l1)
print(l1)
print(l2)
'''
# ? sort --> arrange elements in list in ascending or descending order
'''
l1 = [2, 7, 45, 0, -6, 5, 12]
l1.sort()
print(l1)
'''
# M:-2 --> descending order
eg:1
'''
l1 = [9,7,2,3,5,23,63,32]
l1.sort(reverse=True)
print(l1)
'''
eg:2
'''
l1 = ['p', 'r', 'a', 'b', 'h', 'a', 's']
l1.sort()
print(l1)   ---> error
'''
# ? list constructor
# * list() ---> to conver other collection datatypes to list
'''
l3 = ((8, 9, 2))
print(list(l3))
'''
# eg:2
'''
l4 = (59, 62)
print(list(l4))
'''
# ! ----> nested list
# M:-1
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
print(l1[3][1])
'''

# M:-2
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
print(l1[1:5])
'''
# M:-3
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
print(l1[1:-1])
'''

# ? to delete "t" from l1
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
l1[-1].remove('v')
print(l1)
'''

# ? combine these["p", "o", 'y'],[8, 't'] lists in l1 to ["p", "o", 'y', 8, 't']
'''
l1=[8,9,[0,8,7],["p","a","y"],[7,"v"]]
l1[-2].extend(l1[-1])
l1.pop(-1)
print(l1)
'''

# ! ---->Tuple
# *char of tuple

#1.) Tuple hav eto be surrounded by()
#2.) The elements inside tuple are not changable
#3.) The elements inside tuple are indexed
#4.) The element will execute in order
#5.) It is heterogenous
#6.) It allow duplicate elements

#eg:1
'''
t1 = (8, 8, 9, 6, 5.78,[9, 0], (6, 8), "hey", 9+6j)
print(t1)
print(type(t1))
'''
# ? indexing, slicing are all same as list
'''
t1 = (8)    #list
print*(type(t1))
'''
#eg:2
'''
t1 = (8,)    #list
print*(type(t1))
'''
# M:-3
'''
t1=8,9
print(type(t1))
'''
# M:-4
'''
t2=8,
print(type(t2))
'''

# len(), min(), max(), index(), count() --> all same as list

# to add element inside tuple ---> cannot add
# cannot delete any element from tuple
# Join 2 tuples
#m --->1
'''
t1 = (8, 9, 0)
t2 = (6, 7, 8)
print(t1+t2)
'''

# * To add all element inside list and tuple
# --->sum()
#eg:1
'''
l1 = (8, 9, 7, 6)
print(sum(l1))
'''
# * sort tuple
#eg:2
'''
t1 = (8, 9, 0, 89, 12)
print(tuple(sorted(t1)))
print(tuple(sorted(t1, reverse=True)))
'''
# * Iterate list and tuples
#eg:3
'''
l1 = [9, 8, 0, 6, 5]
for i in l1:
    print(i)
'''

# Iterate based on index value
'''
l1=[9,8,0,6,5,7,36,54,55,6,43,5,66]
for i in range(0,len(l1)):
    print(l1[i])
'''

# ! ----> Strings
'''
s1 = '0'
print(type(s1))
'''
eg:2
'''
s1 = "u"
print(type(s1))
'''
#eg:3
'''
s1 = "hello world"
print(s1)
'''
# * To access string
# indexing and slicing --> same as list and tuple

# ---> common functions
# len()< min(), max(), index(), count()
'''
s1 = "hello world"
print(len(s1))
'''
# eg:2
'''
s1 = "helloworld"
print(min(s1))
'''
# eg:3
'''
s1 = "helloworld"
print(max(s1))
'''
# ord() ---> used to find the ASCII value of a character
'''
s1 = 'u'
print(ord(s1))
'''
# ! Functions of string
# ? to convert all characters to upper case
'''
s1 = "hello world"
print(s1.upper())
'''
# m --->2
# ? to convert all characters to lower case
'''
s1 = "hello world"
print(s1.lower())
'''
# strip()
# to eliminate the space in beginning and end of string
# m--->1
# to eliminate left space
'''
s1 = "   where are you.?"
print(s1.lstrip())
'''
# m --->2
# to eliminate right space
'''
s1 = " Where are you.?"
print(s1.lstrip())
'''
# eg:3
# to eliminate right space and  left space
'''
s1 = "    Where are you.?     "
print(s1.lstrip())
'''

# ---> split()-->
# --> to split the words in string based on a character
# m ---> 1
'''
s1= "where are you.?"
print(s1.split(" "))
'''
# m ---> 2
'''
s1= "where are you.?"
print(s1.split(" r "))
'''
# m ---> 3
'''
s1= "where are you.?"
print(s1.split("e"))
'''

# replace() --> to replace a specific char in the string
'''
s1= "where are you.?"
print(s1.replace('r','&&'))
'''

# swapace() --> to convert capital to small and small to capital at a time
'''
s1 = "HEY there"
print(s1.swapcase())
'''

# * title()
'''
s1 = 'never giveup'
print(s1.title())
'''

# * capitalize()   ---> 1st char of string will be converted to capital
'''
s1 = 'never giveup'
print(s1.capitalize())
'''
# * join the string
'''
s1 = "hello"
s2 = "world"
print(s1+s2)
'''
# eg:1
'''
s1 = 'how are you
# iam fine
# hey there'
print(s1.splitnes())
'''
#* find)()
# M:-1
'''
s1 = "hello world"
print(s1.find('h'))
'''
# M:-2
'''
s1 = "hello world"
print(s1.index('h'))
'''

# join() 
# eg:1
'''
l1 = ["hey","there"]
print(" ".join(l1))
'''
# m-->2
'''
l1 = ["hey","there"]
print("$ ".join(l1))
'''
# eg:3
'''
s1 = "welcome to all"
print(s1.startswith('w'))
'''
# eg:4
'''
s1 = "welcome to all"
print(s1.endswith('w'))
'''
# Example:
'''
s1 = "67"
print(type(s1))
print(s1.isdigit())
'''

# * print the string in reverse manner
'''
s1 = "welcome to all"
print(s1[::-1])
'''

# ! ----> Eg:1
#wap to find the number of lower case letters
'''
s1 = "AKASH weds you ARE"
count = 0
for i in s1:
    if i.islower():
        count+=1
    print("The total numk of lower case letters: ",count)
'''



# ! ---> Eg:2 r ----> "$"
# m:-1
'''
s1 = 'restarter'
print(s1[0] + s1[1:].replace('r', '$'))
'''
#m:-2
'''
s1 = 'restarter'
s1 = "IMAGIN"
fst = s1[0]
bal = s1[1:]
txt = bal.replace(fst, "4")
print(fst+txt)
'''
# ! ---> eg:3

s1="Lorem Ipsum is simply dummy text of the printing and typesetting industry.Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,when an unknown printer took a galley of type and scrambled it to make a typespecimen book. It has survived not only five centuries, but also the leapinto electronic typesetting, remaining essentially unchanged.It was popularised in the 1960s with the release of Letraset sheets containingLorem Ipsum passages, and more recently with desktop publishing software likeAldus PageMaker including versions of Lorem Ipsum."
'''
print(len(s1))
'''
# eg:2
s1="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
'''
words = s1.split(" ")
print(len(words))
'''
# eg:3
s1="Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
sentenses = s1.split('.')
no_sen=(sentenses)
for val in sentenses:
    if val =='':
        index = sentenses.index('')
        sentenses.pop(index)
    print("no of sentenses : ", no_sen)
    
    



























