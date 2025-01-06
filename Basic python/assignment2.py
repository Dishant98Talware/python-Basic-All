
#===================       Assignment :-2 (string and list)    ===========================
#-----------------------------------------------------------------------------------------------


# 1] Write a python function that takes a string and returns its first character?

# name="Dishant" 
# print(name[0])   # D


#-------------------------------------------------------------------------------------------------
# 2] Write a python function that takes a string and returns its last character?


# name="Dishant Talware"
# print(name[14])   # e
# print(name[-1])   # e



#-------------------------------------------------------------------------------------------------
# 3] Write a python function that takes a string and returns first 3 characters?

# name="Instagram"
# print(name[0:3])  # Ins


#-------------------------------------------------------------------------------------------------
# 4] Write a python function that takes a string and returns last 3  characters?

# name="Engineering"
# print(name[8:11])    # ing
# print(name[8:])      # ing
# print(name[8:11:1])  # ing
# print(name[8: :1])   # ing
# print(name[-3:])     # ing



#-------------------------------------------------------------------------------------------------
'''5] Write a python function that takes a string and returns a substring from the start to middle  
of the string? '''

# college="Sipna_Clg Engg"
# print(college[0:6:1])      # Sipna_


#-------------------------------------------------------------------------------------------------
'''6] Write a python function that takes a string and returns a substring from middle to end  
       of the string?  '''


# intro="Hi everyone Dishant here"
# print(intro[12: :1])            # Dishant here



#-------------------------------------------------------------------------------------------------
# 7] Write a python function that take a string and returns the characters at even indices.

# name="Welcome to the kiran academy"
# print(name[0: :2])    # Wloet h ia cdm


#-------------------------------------------------------------------------------------------------
# 8] Write a python function that take a string and returns the characters at odd indices.

# name="Welcome to the kiran academy"
# print(name[1: :2])     # ecm otekrnaaey


#-------------------------------------------------------------------------------------------------
# 9] Write a python function that take a list and return the sublist from the start up to index 4  

# fruits = ['apple', 'banana', 'cherry', 'mango', 'papaya', 'orange']
# print(fruits[0:5:1])     # ['apple', 'banana', 'cherry', 'mango', 'papaya']


#-------------------------------------------------------------------------------------------------
# 10] Write a python function that take a list and return the sublist start from index 2 to the end.

# name=['Dishant', 'Prashant', 'Nishant', 'Rishant', 'Karan', 'Aman']
# print(name[2: :1])     # ['Nishant', 'Rishant', 'Karan', 'Aman']


#-------------------------------------------------------------------------------------------------
#11] Write a python function that take a list and return a new list with the elements reverse using slicing.

# alpha=['A', 'B', 'C', 'D', 'E']
# print(alpha[-1: :-1])    # ['E', 'D', 'C', 'B', 'A']

# alpha.reverse()
# print(alpha)

#-------------------------------------------------------------------------------------------------
# 12] Write a python function that take a list and return a new list containing every other element  (i.e., element at even indices).

# alpha=['A', 'B', 'C', 'D', 'E']
# print(alpha[0: :2])     # ['A', 'C', 'E']


#-------------------------------------------------------------------------------------------------

'''13] Write a python function that check if a string is empty by slicing the string and returning True if it is 
       empty and False otherwise '''
       
       
# clg=""
# if clg[0:]:
#        print("True")
# else:
#        print("False")    # False    


# clg="Dishant"
# if clg[0:]:
#        print("True")
# else:
#        print("False")    # True  


#----------------------------------------------------------------------------------------------------
# 14] Write a python function that take a string and returns a substring from index 3 to 6

# que="WAP_to_check_number is even or odd"
# print(que[3:7:1])     # _to_



#----------------------------------------------------------------------------------------------------
'''15] Write a python function that removes the first character from a string using slicing and  returns 
       the result. '''

# char="abcdefgh"
# print(char[1: :1])  # bcdefgh


#----------------------------------------------------------------------------------------------------
'''16] Write a python function that removes the last character from a string using slicing and  returns 
       the result.  '''
       
# name="DishantT"
# print(name[0:7:1])   # Dishant


#----------------------------------------------------------------------------------------------------
'''17] Write a python function that takes a list and returns a sublist from the last element to the 
       second-to-last element  '''

# fruit = ['apple', 'banana', 'cherry']
# print(fruit[-1:-3:-1])    # ['cherry', 'banana']



#----------------------------------------------------------------------------------------------------
# 18] Write a python function that takes a list and returns a sublist starting from index 1 to index 4


# num=['1','2','3','4','5','6','7']
# print(num[0:4:1])    # ['1', '2', '3', '4']


#----------------------------------------------------------------------------------------------------
# 19] Write a python function that take two strings and concatenates them using slicing.

# a="Dishant"
# b="Talware"
# print(a[0:] + b[0:])  # DishantTalware


#----------------------------------------------------------------------------------------------------
''' 20] Write a python function that replace the characters from index 2 to index 5 of a string with 
       another string  '''


# name="dishant"
# alpha="ABCD" 
# print(name.replace(name[2:6],alpha))  # diABCDt

