#------------------------------------------------------------------------------------------
#============================List [ ]======================================================


# num=[11,22,33,"Dishant"]
# print(type(num))       # <class 'list'>


# cars = ['mahindra', 'Honda', 'Audi','Rollsroyas','tata','suzuki',"BMW"]
# cars[1:3]=["Range rover"]
# print(cars)         # ['mahindra', 'Range rover', 'Rollsroyas', 'tata', 'suzuki', 'BMW']


#----------------slicing & indexing-----------------------------------------------------------

# student=["rajesh","ajay","om","kunal"]
# print(student[1],)  # ajay
# print(student[-1])  # kunal
# print(student[0])   # rajesh
# print(student[0:2:1])  # ['rajesh', 'ajay']



#---------------addition for index 0 & -1 -----------------------------------------------------

# num=[11,22,33,44,66]
# sum=num[0] + num[-1]
# print(sum)               # 77



#---------------square ka addition 1st & last---------------------------------------------------

# lst=[1,2,3,4,5,6]
# start=lst[0] * lst[0]
# end=lst[-1] * lst[-1]
# print(start+end)        # 37


#---------------- 77 nikalo ------------------------------------------------------------------------

# l = [11, 22, 33, [66, 77, 88], 99, 100]
# val = l[3][1]  
# print(val)    # 77


#-----------------------Arithmatic opration in list-----------------------------------------------------
#--------------   +    ---------------------------------------------------------------------------------

# lst=[2,4,6,8,5,4,7]
# kl=lst[0] + lst[1] +lst[2] + lst[3]  + lst[4] + lst[5] + lst[6]
# print(kl)                    # 36



#--------------   -    ---------------------------------------------------------------------------------

# lst=[10,4,6,8,5,4,7]
# kl=lst[0] - lst[-1]  
# lk=lst[0] - lst[1]  
# print(kl,lk)      # 3  6
# print(kl+lk)     # 9


#--------------   *    ---------------------------------------------------------------------------------

# lst=[10,4,6,8,5,4,7]
# var=lst[-1] * lst[-2]
# print(var)             # 28


# lst=[10,4,6,8,5,4,7]
# last=lst[-1] * lst[-1]
# second=lst[-2] * lst[-2]
# print(last + second)      # 65

#----------------------   s / Tal / erawlaT  ------------------------------------------------------------
# l = [11, 22, 33, ["dishant", "Talware"], 99, 100]
# var=l[3][0][2]
# print(var)         # s

# l = [11, 22, 33, ["dishant", "Talware"], 99, 100]
# vl=l[3][1][0:3:1]
# print(vl)           # Tal

# l = [11, 22, 33, ["dishant", "Talware"], 99, 100]
# vl=l[3][1][: :-1]
# print(vl)           # erawlaT



#---------------Slicing-------------------------------------------------------------------------

# l=[11,22,33,44,55,66]
# print(l[0:4:1])    # [11, 22, 33, 444]
# print(l[2:-1:1])   # [33, 44, 55]
# print(l[0::2])     # [11, 33, 55]
# print(l[0: :3])    # [11, 44]
# print(l[-1:-4:-1])  # [66, 55, 44]


# l=[11,22,33,44,[55,66,77,88],99,100]
# print(l[4][1:3:1])    # [66, 77]
# print(l[4][2: :1])  # [77, 88]


#----------- even / odd -------------------------------------------------------------------------------

# l=[11,12,13,14,15,16,17,18,19,20]
# print(l[0: :2])   # [11, 13, 15, 17, 19] odd
# print(l[1: :2])   # [12, 14, 16, 18, 20] even
# print(l[-2: :-2])  # [19, 17, 15, 13, 11] reverse odd
# print(l[-1: :-2])   # [20, 18, 16, 14, 12] reverse even




#========================================================================================================
#----------------------------Method / Function List------------------------------------------------------

# append, extend, insert, 
# remove, pop, clear
# index, count
# sort, reversed
# copy


#---------------  append  -------------------------------------------------------------------------------
# it is used to add element at the end of list

# num=[11,22,33,44]
# num.append(55)
# print(num)          #  [11, 22, 33, 44, 55]

# num=[11,22,33,44]
# num.append(55,66)
# print(num)           # Error ( , )

# num=[11,22,33,44]
# num.append[55]
# print(num)           # Error [ ]

# num=[11,22,33,44]
# num.append([55])
# print(num)      # [11, 22, 33, 44, [55]]

# num=[11,22,33,44]
# num.append([55,66,77])
# print(num)       # [11, 22, 33, 44, [55, 66, 77]]



# f=["dishant","komal","mansi","om"]
# p=["jay","ajay","vijay","sujay","pranav"]
# f.append(p.pop())
# print(f)                      # ['dishant', 'komal', 'mansi', 'om', 'pranav']



#-------------------  extend  ------------------------------------------------------------------------------

# bds=[55,66,77,88]
# bds.extend(99)
# print(bds)        # Error  ( )

# bds=[55,66,77,88]
# bds.extend[99]
# print(bds)         # Error [  ]

# bds=[55,66,77,88]
# bds.extend([99,100])
# print(bds)           # [55, 66, 77, 88, 99, 100]

# bds=[55,66,77,88]
# bds.extend([99])
# print(bds)        # [55, 66, 77, 88, 99]

# cars = ['mahindra', 'Honda', 'Audi','Rollsroyas','tata','suzuki',"BMW"]
# cars.extend(["honda","yamaha","suzuki","BMW"])
# print(cars)




#-------------  insert  -----------------------------------------------------------------------------------
# add items at particular index number

# num=[99,88,77,66,11]
# num.insert(1,22)
# print(num)        # [99, 22, 88, 77, 66, 11]

# num.insert([1,22])
# print(num)          # Error  ([])

# cars = ['mahindra', 'Honda', 'Audi','Rollsroyas','tata','suzuki',"BMW"]
# cars.insert(2,"BYD")
# print(cars)



#-----------  remove  --------------------------------------------------------------------------------------
# delete specific value and can't return

# num=[11,22,33,44,22,11,22]
# num.remove(22)
# print(num.remove(22))  # None
# print(num)      # [11, 33, 44, 22, 11, 22]  


# num=[11,22,33,44,22,11,22]
# num.remove[33]
# print(num)         # Error [ ]


# num=[11,22,33,44,22,11,22]
# num.remove(33,22)
# print(num)         # TypeError: list.remove() takes exactly one argument (2 given)


# fruit=["Apple","Banana","Orange","Cherry"]
# fruit.remove("Banana")
# print(fruit)        # ['Apple', 'Orange', 'Cherry']


# l=[11,22,33,44]
# print(l.remove(22))  # None


# l=[11,22,33,44]
# l.remove(22)
# print(l)      # [11, 33, 44]


#EXTRA
# l=[1,2,3,4,5,6,7]
# del l[0:3]
# print(l)   # [4, 5, 6, 7]



#--------  pop  ------------------------------------------------------------------------------------------
# delete elemment by using indexing and return 

# alpha=["A","B","C","D"]
# alpha.pop()
# print(alpha.pop())   # c
# print(alpha)     # ['A', 'B', 'C']


# alpha=["A","B","C","D"]
# alpha.pop(0)
# print(alpha)    # ['B', 'C', 'D']



# l=[11,22,33,44]
# l.pop()
# print(l)          # [11, 22, 33]


# l=[11,22,33,44]
# print(l.pop())    # 44

# l=[11,22,33,44]
# print(l.pop(1))   # 22 



#--------  clear  ------------------------------------------------------------------------------------------

# alpha=["A","B","C","D"]
# alpha.clear()
# print(alpha)       # []


# index nhi chalta 



#-----------  index  ----------------------------------- return -------------------------
# std=["std.1","std.2","std.3","std.4"]
# print(std.index("std.2"))   # 1

# l=[11,22,333,44,55]
# l[2]=33
# print(l)   # [11, 22, 33, 44, 55]


# l=[1,2,3,4]
# l[0]=99
# print(l)   # [99, 2, 3, 4]

# l=[11,22,333,44,55]
# l[1:-1:1]=[222,333,444]
# print(l)              # [11, 222, 333, 444, 55]

# l=[11,22,333,44,55]
# l[1:-1:1]=[222,333]
# print(l)               # [11, 222, 333, 55]


# l=[11,22,333,44,55]
# l[1]=[222,333]
# print(l)     # [11, [222, 333], 333, 44, 55]

#---------  count  --------------------------------------------------------------------------------------

# lmn=[2,3,4,5,6,2,3,3,3,2,5,6,7]
# print(lmn.count(2))              # 3

# fruit=["Apple","Banana","Orange","Cherry","Apple"]
# print(fruit.count("Apple"))       # 2      A capital ho ya small farak nhi pdta


# fruit=["Apple","Banana","Orange","Cherry","Apple"]
# fruit.count("Appple")
# print(fruit)            # ['Apple', 'Banana', 'Orange', 'Cherry', 'Apple'] 



#----------  sort  --------------------------------------------------------------------------------------

# num=[4,2,3,1]
# num.sort()
# print(num)     # [1, 2, 3, 4]

# num=[4,2,3,1]
# num.sort(reverse=True)
# print(num)             # [4, 3, 2, 1]

# num=[4,2,3,1]
# print(sorted(num))   # [1, 2, 3, 4]
# print(num)           # [4,2,3,1]


# num=[4,2,3,1]
# print(num.sort())   # None
# print(num)



#----------  reverse  -----------------------------------------------------------------------------------

# lm=[1,2,3,4,5]
# lm.reverse()
# print(lm)    # [5, 4, 3, 2, 1]

# lm=[4,3,5,2,1]
# lm.sort()
# lm.reverse()
# print(lm)      # [5, 4, 3, 2, 1]


#----------  copy  ---------------------------------------------------------------------------------------

# var=[11,22,33,44]
# var.copy()
# print(var)      # [11, 22, 33, 44]




#-------------------------------------------------------------------------------------------------------
#=======================================================================================================
#-------------------------------------------------------------------------------------------------------








#----------  Practice question  -------------------------------------------------------------------------

#1] WAP to ask the user to enter names of their 3 favorite movies & store them in a list

# movies=[]
# mov1=input("Enter 1st Movies name:-")
# mov2=input("Enter 2nd Movies name:-")
# mov3=input("Enter 3rd Movies name:-")

# movies.append(mov1)
# movies.append(mov2)
# movies.append(mov3)

# print(movies)

# ----------------------------------------------------

#2] check the list palindrome or not

# list=["m","a","a","m"]
# list1=list.copy()
# list.reverse()

# if (list1==list):
#     print("list are palindrome")
# else:
#     print("list is not palindrome")

# ------------------------------------------------------


#3] short this list ["C","A","A","B","D","A"]

# lst=["C","A","A","B","D","A"]
# lst.sort()
# print(lst)



#-------------------------------------------------------------------------------------------------------

# p=[11,22,33,[11,22,33,44,"Dishant",55]]
# p[3][-2]="Talware"
# print(p)                     # [11, 22, 33, [11, 22, 33, 44, 'Talware', 55]]



#-------------------------------------------------------------------------------------------------------


# p=[11,22,33,[11,22,33,44,"Dishant",55]]
# p[3][0:3:1]=77,88,99
# print(p)                      # [11, 22, 33, [77, 88, 99, 44, 'Dishant', 55]]


# p=[11,22,33,[11,22,33,44,"Dishant",55]]
# p[3][0:3:1]=77,88
# print(p)                  # [11, 22, 33, [77, 88, 44, 'Dishant', 55]]




#-------------------------------------------------------------------------------------------------------

# Common Functions for Lists:
#These are common built-in functions that work with lists:

# len(list)
# min(list)
# max(list)
# sum(list)
# sorted(list)
# reversed(list)







#-------------------------------------------------------------------------------------------------------
#=======================================================================================================
#-------------------------------------------------------------------------------------------------------


# 1] APPEND
# Create an empty list and add the number from 1 to 5 using append() method. print the final list

# lst=[]
# lst.append(1)
# lst.append(2)
# lst.append(3)
# lst.append(4)
# lst.append(5)
# print(lst)      # [1, 2, 3, 4, 5]


# lst=[]
# lst.append([1,2,3,4,5])
# print(lst)          #  [[1, 2, 3, 4, 5]]


# -------------------------------------------------------------------------------------------------------------------

# 2] INSERT
# Start with a list of fruits ["apple","banana","cherry"]. insert "orange" at the second position and print the list.

# fruits=["apple","banana","cherry"]
# fruits.insert(1,"orange")
# print(fruits)                # ['apple', 'orange', 'banana', 'cherry']

# --------------------------------------------------------------------------------------------------------------------

# 3] CLEAR
# Create a list of the first five odd number. clear the list using cleare() and print it to confirm it's empty.

# lst_odd=[1,3,5,7,9]
# lst_odd.clear()
# print(lst_odd)   # []


# ---------------------------------------------------------------------------------------------------------------------

# 4] SORT
# Sort the list [3,1,4,1,5,9] in ascending order and print the sorted list.

# my_lst=[3,1,4,1,5,9]
# my_lst.sort()
# print(my_lst) # [1, 1, 3, 4, 5, 9]

# ----------------------------------------------------------------------------------------------------------------------

# 5] REMOVE
# Given the list ['apple', 'banana', 'cherry',"banana"], remove the first occurrence of "banana" and print the updated list.

# fruit= ['apple', 'banana', 'cherry',"banana"]
# fruit.remove("banana")
# print(fruit)              # ['apple', 'cherry', 'banana']

# ---------------------------------------------------------------------------------------------------------------------

# 6] INDEX
# Find the index of "Charlie" in the list ["Alice","Bob","Charlie","David"].

# ind=["Alice","Bob","Charlie","David"]
# print(ind.index("Charlie"))        # 2

# ----------------------------------------------------------------------------------------------------------------------
# 7] EXTEND
# Extend the list [1,2,3] with another list [4,5,6] and print the result.

# lst1=[1,2,3]
# lst2=[4,5,6]
# lst1.extend(lst2)
# print(lst1)         # [1, 2, 3, 4, 5, 6]

# ----------------------------------------------------------------------------------------------------------------------
# 8] POP
# Start with a list ["red", "green", "blue", "yellow"] and remove the last element using pop().

# color=["red", "green", "blue", "yellow"]
# color.pop()
# print(color)  # ['red', 'green', 'blue']

# ----------------------------------------------------------------------------------------------------------------------
# 9] COUNT
# Count how many times 2 appears in the list [1,2,3,2,4,2,5]

# count_lst=[1,2,3,2,4,2,5]
# print(count_lst.count(2))  # 3




# -------  9/11/2024  practice --------------------------------------------------------------------------------------------------------
# ----------------------------------------------------------------------------------------------------------------------


# l=[11,22,33,44,55]
# n1=l.pop(1)
# n2=l.pop(3)
# print(n1+n2)

# l=[11,22,33,[1,2,3,4,[10,20,30,40],5,6],44,55]
# l.pop()
# print(l)   

# l=[11,22,33,[1,2,3,4,5,[10,20,30,40],5,6],44,55]
# l[3].pop(6)
# print(l)

# l = [11, 22, 33, [1, 2, 3, 4, 5, [10, 20, 30, 40], 5, 6], 44, 55]
# l[3][5].remove(30)
# print(l)

# l = [11, 22, 33, [1, 2, 3, 4, 5, [10, 20, 30, 40], 5, 6], 44, 55]
# l[3][5].pop(2)
# print(l)

# l = [11, 22, 33, [1, 2, 3, 4, 5, [10, 20, 30, 40], 5, 6], 44, 55]
# l.append(66)
# l.insert(3,333)
# l[3].append(7)
# l[3].insert(3,444)
# l[3][5].insert(2,21)
# print(l)

