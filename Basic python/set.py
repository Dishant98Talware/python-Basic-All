#------------------------------------------------------------------------------------------
#============================set { } ======================================================


# quamma seperated values within curly bracket it is unorder, mutable, heterogeneous collection of immutable elements where duplicate are not allowed


#----------  unorder  -----------------------------------------------------------------------------------
# after print sequence change

# s1={11,22,33,44,55}
# print(s1)



#-------  mutable  ---------------------------------------------------------------------------------------
# add, remove kr sakte hai (CRUD operation perform kr sakte hai)

# s1={32,4,5,6,7,6,}
# print(s1)
# s1.add(66)
# print(s1)
# print(s1)


# #str
# name="dishant"
# print(name.upper())
# print(name)

#--------------  heterogeneous collection of immutable elements  -------------------------------------
# immutable ---> int,float,complex,bool,str,tupple

# s={10,10.5,2+3j,"dishant",True}     #immutable element means list,set,dict not allow 
# print(s)


# s={10,10.5,2+3j,"dishant",True,("tupple",8)}     
# print(s)


# s={10,10.5,2+3j,"dishant",True,[1,2,3]}     
# print(s)             # typeerrror becose list add mutable

#--------- duplicate not allowed --------------------------------------------------------------------

# s={1,2,3,2,1,3,3,4}
# print(s)


#empty list
# l=[]
# print(l)    
# print(type(l))

#empty set
# sar=set()
# print(sar)        # set()
# print(type(sar))  # <class 'set'>


#------  add ------------------------------------------------------------------------------------
# add are the method add a single element to the set.

# s={1,2,3,4}
# s.add(78)
# print(s)

#------  remove  -------------------------------------------------------------------------------------
# remove specific element

# s={1,2,3,4}
# s.remove(3)
# print(s)

#-----  pop  ----------------------------------------------------------------------------------------------
# remove & return item from set, 

# s={11,22,33,6,55,8}
# s.pop()
# print(s)
# print(s.pop())

#----------  discard  -------------------------------------------------------------------------------------
# remove specifc element from set , without raising an error if the element does not exist

# s={1,2,3,4}
# s.discard(6)
# print(s)


# s={1,2,3,4}
# s.remove(9)
# print(s)
# print(s)

#------  intersection --------------------------------------------------------------------------------
#intersection common value nikalti hai

# s1={1,2,3}
# s2={1,56,2,5}
# s3={1,4,3,2}

# s1.intersection(s2,s3)
# print(s1)


# print(s1.intersection(s2,s3))   # s1 ko ya s2  # print(s1.intersection(s2,s3,s4)) 

# print(s1.difference(s2))




#---------- intersection_update ---------------------------------------------------------------------------

# s1={11,22,33,44}
# s2={33,44,55,66}
# s1.intersection_update(s2)     # s1 me intersection update kiya s2 me nhi s2 as it is
# print(s1)
# print(s2)      




# s1={11,22,33,44}
# s2={33,44,55,66}
# s2.intersection_update(s1)  # s2 me intersection update kiya s1 me nhi s1 as it is
# print(s2)

#---------  difference_update -----------------------------------------------------------------------

#ye common value delete krega/ 

# s1={11,22,33,44}
# s2={33,44,55,66}
# s1.difference_update(s2)
# print(s1)

#------- update ----------------------------------------------------------------------------------------

# s1={11,22,33,44}
# s2={33,44,55,66}
# s1.update(s2)
# print(s1)         # {33, 66, 11, 44, 22, 55}

# question :- how to concanet two set  ///  ans by using update + support nhi krta set me

#--------  issubset -----------------------------------------------------------------------------------

# s1={11,22,33,44}
# s2={11,22,33,44,55,66,77,88,99}
# print(s1.issubset(s2))        # True

# s1={11,22,33,44,999}
# s2={11,22,33,44,55,66,77,88,99}
# print(s1.issubset(s2))        # False


#-------- issuperset -----------------------------------------------------------------------------------

# s1={11,22,33,44}
# s2={11,22,33,44,55,66,77,88,99}
# print(s1.issuperset(s2))         # False 


# s1={11,22,33,44}
# s2={11,22,33,44,55,66,77,88,99}
# print(s2.issuperset(s1))         # True

# s1={11,22,33,44,999}
# s2={11,22,33,44,55,66,77,88,99}
# print(s1.issuperset(s2))        # False









#---------------------------------------------------------------------------------------------
#=============================================================================================
