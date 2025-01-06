#=================================================================================================
#-------------- string formating -----------------------------------------------------------------

# %d for integer
# %f for float
# %s for string
# {} {}   .format(name,city)
# {1} {0} .format(city,name)
# {n} {c} .format(c=city, n=name)
# (f'my name is {name} and i am from {city}')
# print(f'firt number is {num1} and {num2} sum is {num1+num2}')


#-------------- %s -----------------------------------------------------------------------------------

# name='Dishant'
# age=78
# print('my name is',name,'and i am',age,)

# print('my nae is %s and i am %s' %(name,age))   # yaha per yek string and yek number hai but ham %s likhe don ke liye o bhi print hoga and %d number ke liye likhe to bhi print hoga




#-------------- %d -----------------------------------------------------------------------------------

# num1=int(input("Enter number:-"))
# num2=int(input("Enter number:-"))
# print("sum of",num1,'and',num2,'is',num1+num2)

# print('sum of %d and %d is %d' %(num1,num2,num1+num2))



#-------------- %f -----------------------------------------------------------------------------------
# %f for float
# default value 6 fix      
# default me 2 hai and 5 dale to wo 2 hi lega and kam dalo to 000 lga dega

# num1=eval(input("Enter number:-"))
# num2=eval(input("Enter number:-"))
# print('sum of %f and %f is = %f' %(num1,num2,num1+num2))

# print('sum of %0.2f and %0.4f is= %0.2f' %(num1,num2,num1+num2))




#========= formate method  ===========================================================================
# {} placeholder   
# default value 0 {is ki}


# name='dishant'
# name.upper()
# print(name)

# print("dishant".upper())




# name=input("enter name")
# city=input('enter city')
# print('my name is {} and i am from {}'.format(name,city))


# num1=eval(input("Enter number:-"))
# num2=eval(input("Enter number:-"))
# print('sum of {} and {} is {}'.format(num1,num2,num1+num2))



#-------------- index formate  --------------------------------------------------------------------
# index number


# name='Dishant'
# city='ytl'
# print('my name is {} and i am from {}'.format(city,name))
# print('my name is {1} and i am from {0}'.format(city,name))


#-------------- key formate  --------------------------------------------------------------------
# by using key

# name='Dishant'
# city='ytl'
# print('my name is {n} and i am from {c}'.format(c=city,n=name))




#-------------- f stiring ------------------------------------------------------------------------

# name='Dishant'
# city='ytl'
# print(f'my name is {name} i am from {city}')


# num1=55
# num2=86
# print(f'firt number is {num1} and {num2} sum is {num1+num2}')




