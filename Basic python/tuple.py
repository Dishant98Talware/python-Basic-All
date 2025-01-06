#------------------------------------------------------------------------------------------
#============================ tupple ( ) ==================================================


# tupple is quama seperate valuw within paraenthesis it is 'immutable' ,it is 'ordered' , it is heteroginus collection of element and 'duplicate are allow'

# indexing slicing allow

# how to access element from tupple //// ans indexing , slicing

#----------  indexing / slicing  --------------------------------------------------------------

# tup=(2,1,3,1)
# print(tup[3])

# t=(1,2,3,(4,5,6),7,8)
# print(t[3])      # (4, 5, 6)
# print(t[3][1])   # 5

# t=(1,2,3,(4,5,6,"rajesh"),7,8)
# print(t[3][-1].upper())           # RAJESH

# t=(11,22,33,44,55,66,77)
# print(t[0:3:1])       # (11, 22, 33)
# print(t[: :-1])       # (55, 44, 33, 22, 11)
# print(t[1: :2])       # (22, 44)
# print(t[-1:0:-2])     # (77, 55, 33)


# t=(11,22,33,44,55,66)
# print(t[-1:1:-2])
# print(t[-1:1:2])


#--------  methods -----------------------------------------------------------------------------------
#methods

# tup.index()
# num.count(1)


#------ count ----------------------------------------------------------------------------------------

# WAP to count the number of student with "A" grade in the following tuple

# grade=("C","A","A","B","D","A")
# print(grade.count("A"))        # 3


# grade=("C","A","A","B","D","A")
# grade.count("A")
# print(grade)          # ('C', 'A', 'A', 'B', 'D', 'A')



#-----  type ---------------------------------------------------------------------------------------

# t=(11,22,33)
# print(type(t))  # <class 'tuple'>

# t=11,22,33
# print(type(t))   # <class 'tuple'>


# lst=[1,2,3,4]
# print(type(lst))  # <class 'list'>

# lst=1,2,3,4
# print(type(lst))  # <class 'tuple'>




#-----  getsizeof --------------------------------------------------------------------------------------
# getsizeof  kitni memory li check


# from sys import getsizeof
# t1=(1,2,3,4,5)
# print(getsizeof(t1))   # 80

# t2=[1,2,3,4,5]
# print(getsizeof(t2))   # 104




#--------- id ------------------------------------------------------------------------------------------

# t=(11,22,33,44)
# t1=(11,22,33,44)
# print(id(t))
# print(id(t1))

# t3=[1,2,3,4,5]
# t4=[1,2,3,4,5]
# print(id(t))
# print(id(t1))


#-------- packing and unpacking -----------------------------------------------------------------------

# packing and unpacking   tupple supprt both / list support only unpacking 

#unpacking
# tup=(11,22,33)
# x,y,z=tup
# print(x,)
# print(y)
# print(z)
# print(x,y,z)


# # packing
# a=100
# b=200 
# c=300 
# t=a,b,c
# print(t)












