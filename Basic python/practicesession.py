# ------------ 27-11-2024 ----------------------------------------------------------------------

#1. WAP to calculate the sum,difference, product, and quotient of two numbers entered by the user.

# num1=int(input("Enter 1st number: "))
# num2=int(input("Enter 2nd number: "))
# print()
# sum=num1+num2        # add
# diff=num1-num2       # subtraction
# product=num1*num2    # multi
# quotient=num1/num2   # division
# print("The sum of",num1, "and",num2,"is:",sum)
# print("The difference of",num1, "and",num2,"is:",diff)
# print("The product of",num1, "and",num2,"is:",product)
# print("The quotient of",num1, "and",num2,"is:",quotient)



#------------------------------------------------------------------------------------------------
# 2. WAP to check if two variable reference the same object using is and not is. 

# number1=100
# number2=200
# print(number1 is number2)        # False
# print(number1 is not number2)    # True



#------------------------------------------------------------------------------------------------
# 3. initialize a variable with a number and demonstrate the all asignment operators(+=,-=,*=,/=,%=). 

# num = 10          # initialize
# num += 5  
# print("The result of +=: ", num)

# num1 = 10  
# num1 -= 3  
# print("The result of -=: ", num1)

# num2 = 10  
# num2 *= 2  
# print("The result of *=: ", num2)

# num3 = 10  
# num3 /= 4  
# print("The result of /=: ", num3)

# num4 = 10  
# num4 %= 3  
# print("The result of %=: ", num4)




#------------------------------------------------------------------------------------------------
#4. WAP that takes two number and prints whether the first is grater than, less than, or equal to the second.
# ==,!= are (Relational operator/equality operators)

# num1=int(input("Enter 1st number: "))
# num2=int(input("Enter 2nd number: "))

# greater= num1>num2
# print(num1,'>',num2,':',greater)        

# less= num1<num2
# print(num1,'<',num2,':',less)           

# equal= num1==num2
# print(num1,'==',num2,':',equal)          

# notequal= num1!=num2
# print(num1,'!=',num2,':',notequal)       



#------------------------------------------------------------------------------------------------
#5. calculate the perimeter and area of a rectange givenn its length and width using arithmetic operator. 

# length =float(input("Enter the length of the rectangle: "))
# width =float(input("Enter the width of the rectangle: "))

# perimeter = 2*(length+width)    # Perimeter formula
# area = length*width             # Area formula

# print(f"The perimeter of the rectangle is: ",perimeter)
# print(f"The area of the rectangle is: ",area)



#------------------------------------------------------------------------------------------------
#6. compare two  string using "is" to check whether they are stored at the same memory location. 

# a="Dishant"
# b="Dishant"
# print(a is b)



#------------------------------------------------------------------------------------------------
#7 WAP to find the remainder of a division operation using the %= operator. 

# num1 = int(input("Enter the dividend (numerator): "))
# num2 = int(input("Enter the divisor (denominator): "))
# a=num1%num2
# print('The remainder is:',a)



#------------------------------------------------------------------------------------------------
#8 WAP to compare the length of two string and print wich one is longer. (relational op)

# str1="Dishant"
# str2="Rishant"

# x=(len(str1))
# y=(len(str2))
# print(x)
# print(y)

# if x>=y:
#     print(str1)
# else:
#     print(str2)





#-------------------------------------------------------------------------------------------
#=========  29/11/2024 =====================================================================
#-------------------------------------------------------------------------------------------

# 1]  Write a program to check the data type of a variable.
# num=10
# print(type(num))



#-------------------------------------------------------------------------------------------
#2]  Create a list of integers and find the sum of all elements.

# l=[1,2,3,4,5]
# total=sum(l)
# print(total)



#-------------------------------------------------------------------------------------------
# 3] Write a function that takes a string and returns its length.

# str=input("Enter string:-")
# print(len(str))



#-------------------------------------------------------------------------------------------
#4. Convert a float to an integer and print both.

# fl=12.5
# con=int(fl)
# print(con)

# print(fl)



#-------------------------------------------------------------------------------------------
#5.  reate a tuple and access its elements.

# tup=(1,2,3.5,4,"Dishant")
# for i in tup:
#     print(i)



#-------------------------------------------------------------------------------------------
#6.  Write a program to concatenate two strings.

# a="Dishant"
# b="Rishat"
# print(a+b)



#-------------------------------------------------------------------------------------------
#7 Create a dictionary and retrieve a value using its key.

# dict={'a':10,'b':20,'c':30,'d':40}
# print(dict['a'])



#-------------------------------------------------------------------------------------------
#8  Check if a list is empty.

# l=[1,2]
# if len(l) == 0:
#     print("The list is empty.")
# else:
#     print("The list is not empty.")



#-------------------------------------------------------------------------------------------
#9. Write a function that takes a number and returns its type.

# num=int(input("enter number:"))
# print(type(num))



#-------------------------------------------------------------------------------------------
#10.  Create a set and demonstrate adding and removing elements.

# set={1,2,3,4,5}
# set.add(100)
# print(set)

# set.remove(3)
# print(set)



#-------------------------------------------------------------------------------------------
#11. Convert a list of strings to a list of integers.

# l = ['10','20','30','40','50']
# my_list=list(map(int, l))  
# print(my_list)



#-------------------------------------------------------------------------------------------
# 12. Write a program to find the maximum and minimum values in a list.

# my_list=[3,1,7,9,4,2]
# max=max(my_list)
# min=min(my_list)
# print(max)
# print(min)



#-------------------------------------------------------------------------------------------
#13. Check if a given string is a palindrome.

# str="madam"
# if str==str[::-1]:
#     print("palindrome")
# else:
#     print('not a palindrome.')



#-------------------------------------------------------------------------------------------
# 14. Write a program to create a list of squares of numbers from 1 to 10.

# l=[]
# for i in range(1,11):
#     a=i*i
#     l.append(a)
# print(l)



#-------------------------------------------------------------------------------------------
# 15. Create a nested list and access an element in the inner list.

# l=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
# element=l[1][1]
# print(element)



#-------------------------------------------------------------------------------------------
# 16. Write a function that checks if a given number is even or odd.

# num=int(input("Enter number:-"))
# if num%2==0:
#     print("Even")
# else:
#     print("Odd")




#-------------------------------------------------------------------------------------------
# 17. Create a dictionary and add a new key-value pair.

# details={"name":"Dishant","age":21,"marks":89}
# details['clg']='SCOEAT'
# print(details)

# details.setdefault('clg','SCOEAT')
# print(details)



#-------------------------------------------------------------------------------------------
# 18. Write a program to remove duplicates from a list.

# l=[1,21,2,2,21,3,4,21]
# x=set(l)
# print(x)



#-------------------------------------------------------------------------------------------
# 19. Convert a string to a list of characters.

# str="DISHANT"
# lm=list(str)
# print(lm)



#-------------------------------------------------------------------------------------------
# 20. Write a function that returns the type of each element in a list.

# l=[ 1, 12.0, "Dishant", True, [1,2,3], (1,"string"), {'name':"dishant"} ]
# for i in l:
#     print(type(i))