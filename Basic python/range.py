#------------------------------------------------------------------------------------------
#============================ range() =====================================================


# varname=range(sv,ev,sv)
# varname=range(start_value, end_value, step_value)

#----------------------------------------------------------------------------------------------------

# num=range(1,11,1)
# print(num)        # range(1, 11)



#----------------------------------------------------------------------------------------------------
# 1 se 10 tak print krega (positive )

# num=range(1,11,1)
# for i in num:
#     print(i)

# for num in range(11):
#     print(num)          # 0 to 10


# for num in range(1,11,1):
#     print(num)





#--------- 11 to 1 reverse --------------------------------------------------------------------------------

# for num in range(11,0,-1):
#     print(num)




#-------- even --------------------------------------------------------------------------------------
# print even numer 20 to 30

# for num in range(20,31,2):
#     print(num)




#----------------------------------------------------------------------------------------------------
# odd 50 to 41

# for num in range(49,40,-2):
#     print(num)




#----------------------------------------------------------------------------------------------------
# square of odd 

# for num in range(23,44,2):
#     print(num*num)




#----------------------------------------------------------------------------------------------------
# WRT to print set of square of number from 1 to 10

# s=set()
# for num in range(1,11,1):
#     s.add(num*num)
# print(s) 


# s=set()
# for num in range(1,11,1):
#     sq=num*num
#     s.add(sq)
# print(s)



#----------------------------------------------------------------------------------------------------

# last wala 1 nhi diya to wo default value hoti hai  (start value, & step value)
# start value default 0 , last +1


# for i in range(5):
#     print(i)
    

# for i in range(1,5):
#     print(i)




#--------list, set, tupple ke andar range---but not in dict--------------------------------------

# a=list(range(0,11))
# print(a)

# a=set(range(0,11))
# print(a)

# a=tuple(range(0,11))
# print(a)

# a=dict(range(0,11))
# print(a)             # dict ke andar nhi kr sakte (because key value pair hoti hai)