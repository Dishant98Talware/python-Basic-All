#-------------------------ITERATION ----------------------------------------------------
#============================ forloop  ==================================================

# it is iterate over statement  - (like list,tuple,string,range)
# iteration krna



#-------------------------------------------------------------------------------------------------------
# iterating through a list

# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)



#-------------------------------------------------------------------------------------------------------
# Using range() iterate over number:

# range() symtax ---->       varname=range(start_value, end_value, step_value)


# for i in range(5):
#     print(i)



# for i in range(1,6,1):
#     print(i)



# for i in range(5,0,-1):
#     print(i)



#-------------------------------------------------------------------------------------------------------
# iterate through a string:

# for letter in "Dishant":
#     print(letter)



#-------------------------------------------------------------------------------------------------------
# loop through a list:

# l=[11,22,33,44]
# for num in l:
#     print(num)



# l=[11,22,33,44]
# for num in l:
#     print(num)
#     print("Dishnat")
# print("Dishant Talware")


# l=[11,22,33,44]
# for num in l:
#     print("hello")



# l=[11,22,33,44]
# print("Welcome")
# for num in l:
#     print(num)
#     print("Dishnat")
# print("Dishant Talware")




#-------------------------------------------------------------------------------------------------------
# WRT to print square of number of list

# l=[1,2,3,4,5,7,9,8]
# for num in l:
#     print(num*num)



#-------------------------------------------------------------------------------------------------------
# WAP to print list of square of number     ---->   (list ke andar square print kro)

# l=[1,2,3,4,5,7,9,8]           |
# sq=[]                         |
# for num in l:                 |
#     s=num*num                 |
#     sq.append(s)              |
# print(sq)                     |



# l=[1,2,3,4,5,7,9,8]           |
# sq=[]                         |
# for num in l:                 |
#     s=num*num                 |
#     sq.append(s)              |
#     print(sq)                 |




#-------------------------------------------------------------------------------------------------------
# student ko upper kro

# student=["mayur","kunal","ragav","vijay"]
# s=[]
# for name in student:
#     s.append(name.upper())
# print(s)





#-------------------------------------------------------------------------------------------------------
# all list item cube add in set 

# l=[1,2,3,4]
# s=set()
# for num in l:
#     cu=num*num*num
#     s.add(cu)
# print(s)



#-------------------------------------------------------------------------------------------------------
# meko inpute lena hai and bar bar excute krna hai and list me store krna hai.

# student=[]
# name=input("enter name:-")
# student.append(name)
# print(student)



# student=[]
# for i in range(5):
#     name=input("enter name:-")
#     student.append(name)
# print(student)




#---------- list iteration ---------------------------------------------------------------------------

# l=[1,2,3,4,5,6]
# for i in l:
#     print(i)




# l=[[1,2,3],[11,22,33],[3,4,5],[55,66,77]]
# for i in l:
#     for j in i:
#         print(j)



#---------- tuple iteration ---------------------------------------------------------------------------

# t=(1,23,4,5,6,7)
# for i in t:
#     print(i)


#---------- tuple iteration ---------------------------------------------------------------------------

# s="DISHANT"
# for i in s:
#     print(i)

# s="DISHANT","TALWARE"
# for i in s:
#     print(i)


#-------- TABLE PRINT KRO-----------------------------------------------------------------------

# a=18
# for i in range(1,11):
#     print(a,"x",i,"=",a*i)


#-------- 1 DALA TO 10 TAK PRINT KREGA  --------------------------------------------------------

# a=int(input("Enter number:-"))
# for i in range(a,a+10):
#     print(i)









#-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
#--------- nasted for -------------------------------------------------------------------------

# for i in range(3):
#     for j in range(5):
#         print("hello")



# for i in range(2):
#     for j in range(5):
#         print(j)



# for i in range(4):
#     for j in range(2):
#         print(j)



# for i in range(1,6):
#     for j in range(1,6):
#         print("*",end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         print(i, end=' ')
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         print(j, end=' ')
#     print()


# for i in range(5,0,-1):
#     for j in range(5,0,-1):
#         print(i, end=" ")
#     print()


# for i in range(5,0,-1):
#     for j in range(5,0,-1):
#         print(j, end=" ")
#     print()


# i=1
# for i in range(i,26,5):
#     for j in range(i,i+5):
#         print(j,end="  ")
#     print()


#  print 1 table 5 netx line 2 tbale 5   5....5


# r=5
# for i in range(1,r+1):
#     for j in range(1,i+1):
#         print('*', end=' ')
#     print()