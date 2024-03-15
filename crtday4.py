# ----> while loop
# ----> break using while loop

# eg:1
# 1.) iterate from 20 to 30 and break the loop in 27
'''
i=20
while i<31:
    if i == 27:
        break
    print(i)
    i+=1
'''
#eg:2
'''
i=20
while i<31:
    print(i)
    i+=2
    if i == 27:
        break
'''
# method -----> 3.)
'''
i=20
while i<31:
    print(i)
    if i == 27:
        break
    i+=1
'''
# -----> only 27
'''
i=20
while i<31:
    if i == 27:
        print(i)
        break
    i+=1
'''
# ----> continue
#eg:1
'''
i=20
while i<31:
    if i == 27:
        continue
    print(i)
    i=i+1
'''
# ----> skip the 27 number
'''
i=20
while i<31:
    i=i+1
    if i == 27:
        continue
    print(i)
'''
# -----> skip the number 27
'''
i=20
while i<31:
    if i == 27:
        i=i+1
        continue
    print(i)
    i=i+1
'''
# eg:1
# while to iterate from 12 to 22
# find the sum of all numbers
'''
i=12
while i<=22:
    print(i)
    i=i+1
'''
'''
i=12
sum=0
while i<=23:
    sum=sum+i
    i+=1
print(sum)
'''
# eg:2
# Find the average of value from 20 to 25
'''
i = 20
sum = 0
count = 0
while i<30.5:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)
'''
# ----> Nested for loop
#eg:1
'''
for row in range(1, 3+1):
    for col in range(1, 4+1):
        print(row, col)
'''        
#eg:2
# * * * *
# * * * *
# * * * *
# * * * *
'''
rows = int(input("Enter the rows: "))
cols = int(input("Enter the cols: "))
'''
'''
for row in range(rows):
    for col in range(cols):
        print("*" , end=" ")
    print()
'''
# -----> method 2
'''
sum = 0
for row in range(5):
    for col in range(5):
        sum = sum+1
        print(row , end=" ")
    print()
'''
# ---> method-3
# ! to print starts in right angle triangle
'''
for row in range(0, 6):
    for col in range(0, row+1):
        print("*", end=" ")
    print()
'''
#eg:1
# * * * * * *
# * * * * *
# * * * * 
# * * * 
# * * 
# *
'''
for row in range(6, 0, -1):
    for col in range(0, row):
        print("*", end=" ")
    print()
'''
#eg:2
# * * * * *
# *       * 
# *       *
# *       *
# * * * * *
'''
for row in range(6):
    for col in range(6):
        if col==0 or col==5 or row ==0 or row ==5:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
#             *
#          *  *  *
#       *  *  *  *  *
#     * *  *  *  *  *  *
'''
for row in range(6):
    for col in range(6):
        if((row==0 and col==3) or (row==1 and(col>=2 and col<=4)) or (row==2 and (col>=1 and col<=5))):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
'''
# *
# * *
# *   *
# *     *
# *       *
# * * * * * *
'''
for row in range(6):
    for col in range(6):
            if(col==0 or (row==0 and col==0) or (row==1 and col==1))or (row==2 and col==2) or (row==3 and col==3) or (row==4 and col==4) or (row==5):
                print("*",end=" ")
            else:
                print(" ",end=" ")
    print()
'''
# ----> List
# ----> primary
# ----> Number ----> int, float complex
# ----> String
# ----> Boolean
# ----> None
# ----> Collection
# ----> List
# ----> Tuple
# ----> Set
# ----> Dictionary

# ? ---> List
# 1.) if the collection of elements are surrounded by square bracjets, it is considered
# to be list
# ! eg:
# l1=[4, 7, 9, 9.89, "hello", 7+9j, [8, 9, 0]]

# * Characteristics of list
# 1.) List have to be surrounded by []
# 2.) It is mustable(the elements in the list are changable)
# 3.) Every element inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous

# To access the elements in list
'''
l1 = [1, 4, 1, 7, 89, 7, 7.5, "p", "j"]
# print(lst1)
'''

# ---> Indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted
# with predefined unique value called index value

# we have 2 types of indexing
# positive indexing --> starts with 0 from left hand side
# Negative indexing --> starts with -1 from right hand side

# Positive indexing
'''
lst1 = [1, 4, 7, 89.7, 7.5, "p", "i"]
print(lst1[3])
print(lst1[4])
print(lst1[20]) 
'''
# ? ---> Negative indexing
'''
lst1 = [1, 4, 7, 89.7, 7.5, "Hima", "akash"]
print(lst1[-1])
print(lst1[-5])
print(lst1[8])
'''

# ? ----> slicing
# lst1[start_index:end_index:step]
'''
lst1 = [1,2,3,4,56,34,"p","g",]
print(lst1[3:8])
print(lst1[1:4])
print(lst1[3:6])
print(lst1[:5])
print(lst1[3:])
print(lst1[:])
'''
#eg:2
'''
lst1 = [1,2,3,4,56,34,"p","g",]
print(lst1[0:7:1]) # lst1[0:7]
print(lst1[0:7:2])
'''
#eg:3
'''
lst1 = [1,2,3,4,56,34,"p","g",]
print(lst1[-4:-1])
print(lst1[-1:-4])
print(lst1[-7:-1])
'''
#eg:4
'''
lst1 = [1,2,3,4,56,34,"p","g",]
print(lst1[-7:-1:2])
'''
# ! To insert at add element inside list
#appened() ---> used to add element at last position of list
'''
l1 = [9, 8, 0, 6]
l1.append("car")
print(l1)
s'''




























