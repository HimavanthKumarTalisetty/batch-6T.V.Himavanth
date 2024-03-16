# 1.) Python program to capitalize the first and last character of each 
# word in a string
# 2.) Input : 128
# Output : Yes
# 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.
# 3.)l1=[1,2,3,4], l2=[5,6,7,8]
# Add both l1 and l2, ans=[6, 8, 10, 12]

#M --->1
'''
s1 = ("himavanth Kumar")
fst = (s1[0].upper())
lst = (s1[-1].upper())
print(fst+s1[1:len(s1)-1]+lst)
'''
#M --->:2
'''
n = int(input(" enter number : "))
temp = n
f1 = 0
while n!= 0:
    rem = n%10
    check = temp%rem
    if check!=0:
        f1=1
    n=n// 10   
if f1==0:
    print("YES")
else:
    print("N0")
'''

#m --->:3
'''
l1 = [8, 9, 0, 7]
l2 = [7, 6, 5, 4]
op = []
for i in range(len(l1)):
    op.append(l1[i] + l2[i])
print(op)
''' 

# ! ----> set

# ? characteristics of set
# 1.) set can be created using{}
# 2.) the elements inside set are not indexed
# 3.) does not allow duplicate values
# 4.) it unorderd
# 5.) heterogenous    ----> accept only unmutable datatypes
# 6.) mutable or changable

#eg:1
'''
s1 = {9, 9, 89, 7, 76, 8+7j, (8, 7, 5), "truck", 'a'}
print(s1)
'''

#eg:2
'''
s2 = {5, 8, 98, [9, 0]}
Print(s2)   # TypeError: unhashable type: 'list'
'''
# eg:3
# min(), max(), len()

# *eg
# ? to add element inside set
'''
s1 = {8, 78, 67, 'u'}
s1.add(43)
print(s1)
'''

# eg:4
'''
s1 = {8, 78, 67, 'u'}
s1.update([9, 0])
print(s1)
'''

# ? To delete element inside set
# pop() # To delete one element randonly
'''
s1 = {8, 78, 67, 'u'}
s1.pop()
print(s1)
'''

# remove()
'''
s1={4,54,6,3,0,2,68}
s1.remove(54)
print(s1)
'''

# discard()
'''
s1={4,54,6,3,0,2,68}
s1.discard(64)
print(s1)
'''

# clear()
'''
l1 = {}
print(type(l1)) 
'''

'''
s1 = set() # --> to create empty set
print(type(s1))
'''

'''
s1 = {8,9,0}
s1.clear()
print(s1)
'''

'''
s1 = {8,9,0}
del s1
print(s1)
'''

# join the sets
'''
s1 = {9, 0, 8}
s2 = {9.90, "card", 't', 56}
s3 = s1.union(s2)
print(s3)
'''
# * intersection() ---> to get common elements inside set
'''
s1 = {4, 5, 6}
s2 = {5, 6, 7, 8}
print(s1.intersection(s2))
'''
# difference()
'''
s1 = {4, 5, 6}
s2 = {5, 6, 7, 8}
print(s1.differences(s2))
print(s2.differences(s1))
'''
# symmetric difference
'''
s1 = {4, 5, 6}
s2 = {5, 6, 7, 8}
print(s1.symmetric_difference(s2))
'''

# isdisjoit(), issubset(), issuperset()

#s1 = {8, 9, 0}
#s2 = {6, 7, 5, 8, 9, 0}

#print(s1.issubset(s2))
#print(s2.issuperset(s1))

# ---> example-1
'''
s1 = {1,2,3,4,5}
s2 = {3,2,7,8,9}
for val in s1:
    if val in s2:
        str1 = "Its joint set"
print(str1)
'''

# ! ----> dictionary
# eg:1
'''
d1 = {1:100, 'a': 200, 4.5:"hello"}
print(d1)
print(len(d1))
'''
# eg:2
'''
d1 = {1:100, 'a': 200, 4.5:"hello"}
print(d1)
'''

# ? char of dictionary
# 1.) have to be surrounded by
# 2.) It have to be in the form of key, value pair
# 3.) It is mutuable
# 4.) Duplicate keys are not allowed, duplicate values are allowed
# 5.) It is un indexed
# 6.) It is ordered
# 7.) Key does not allow mutuable datatypes, values allow mutuable datatype
# eg ---> 1
# * to access element in dictionary
'''
d1 = {1:100, 2:200, 3:300, 4:400}
print(d1)
'''
# To access the values
'''
d1 = {1:100, 2:200, 3:300, 4:400}
print(d1[1])
'''

# ? some common functions
# len(), min, max()
# ---> min
'''
d1 = {1:100, 2:200, 3:300, 4:400}
print(min(d1))
'''
# ---> max
'''
d1 = {1:100, 2:200, 3:300, 4:400}
print(max(d1))
'''

# ? To find min, max based on values
'''
d1 = {1:100, 2:200, 3:300, 4:400}
print(min(d1.values()))
print(max(d1.values()))
'''
# ---> Dictionary based functions
# to add element(key and value pair) in dict
'''
d1 = {1:100, 2:200, 3:300, 4:400}
d1[5] = 500
print(d1)
'''

# ? To replace a value in dictionary
'''
d1 = {1:100, 2:200, 3:300, 4:400}
d1[2] = "mango"
print(d1)
'''

# ? delete element from dictionary
# popitem()  # ---> to delete last key value pair in dict
'''
d1 = {1:100, 2:200, 3:300, 4:400}
d1.popitem()
print(d1)
'''

# ---> pop()
# ? is the key in the dictionary
'''
d1 = {1:100, 2:200, 3:300, 4:400}
d1.pop(2)
print(d1)
'''

# clear(),del
# join 2 dictionary
'''
d1={1:100, 2:200, 3:300, 4:400}
d2={"a":"apple","b":"boy","g":"game"}
d1.update(d2)
print(d1)
'''

# ---> get() ---> used to get the value from a key
'''
d1={1:100, 2:200, 3:300, 4:400}
print(d1.get(90))
'''

# To print all the keys
'''
d1={1:100, 2:200, 3:300, 4:400}
print(d1.keys())
print(type(d1.keys()))
'''

# To print all the values
'''
d1={1:100, 2:200, 3:300, 4:400}
print(d1.values())
'''

# Iterating dictionary
# To iterate keys alone
'''
d1={1:100, 2:200, 3:300, 4:400}
for val in d1:
    print(val)
'''
# To iterate values alone
'''
d1={1:100, 2:200, 3:300, 4:400}
for val in d1.values():
    print(val)
'''
# to get both key and values
'''
d1={1:100, 2:200, 3:300, 4:400}
for key, val in d1.items():
  print(key,val)
'''

# ! problem:1

# 1.) Swap elements in string list
# 2.) The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks',]
# List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']
'''
n = int(input("Enter num of times : " ))
integer=[]
float_value =[]
string=[]
for val in range(n):
    value = eval(input("Enter the values: "))
    if type(value)==int:
        integer.append(value)
    elif type(value) == float:
        float_val.append(value)
    elif type(value) == str:
        string.append(value)
    else:
        print("Pls provide data in int, float, string")
print(integer)
print(float_value)
print(string)
'''
# problem :2
# m -->1
# Return a set of elements present in Set A or B, but not both
# set1 = {10, 20, 30, 40, 50}
# set2 = {30, 40, 50, 60, 70}
# o/p
# {20, 70, 10, 60}
'''
set1 = {10, 20, 30, 40, 50, 45}
set2 = {30, 40, 50, 60, 70, 100}
l1=set1 ^ set2
print(l1)
'''

# m --->2
# return a set elements present in set A or B, but not both
'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set3 = set()
for val in set1:
    if val not in set2:
        set3.add(val)
for val in set2:
    if val not in set1:
        set3.add(val)
print(set3)
'''
# ! ---> problem:3
# 1.) Swap elements in String list
# # The original list is : ['Gfg', 'is', 'best', 'for', 'Geeks']
# # List after performing character swaps : ['efg', 'is', 'bGst', 'for', 'eGGks']

l1 = [1, 2, 3, 4]  # key
l2 = ["a", "b", "c", "d"]# value
o/p --> {1:'a', 2:'b', 3:'c', 4:'d']
d1 = {}
d1[l1[0]] = l2[0]







