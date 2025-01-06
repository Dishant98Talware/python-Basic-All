# flow of control ----> 3] ,  coditional, iterative,transfer statement.

#-----------------------------------------------------------------------------------------------
#=============== CONDITIONAL STATEMENT =========================================================

#=============== if statement / else statement =================================================

# syntax:-  if condition:
                # body / statement
                


#def:-  if statement is a conditional statement, that allow the program to execute a block of code 
#       only if a specified condition is true. 





#----------------------------------------------------------------------------------------------------
# 1] voting program

# age=int(input("Enter your age:"))
# if age>=18:
#     print("You are eligible for vote")
# else:
#     print("You are eligible for vote")



#----------------------------------------------------------------------------------------------------
# WAP to check number is positive

# num=int(input("Enter your age:"))
# if num>0:
#     print("Yes")
# else:
#     print("No")



#----------------------------------------------------------------------------------------------------
# WAP to print number is even or not

# num=int(input("Enter your age:"))
# if num%2==0:
#     print("This number is even")
# else:
#     print("not even")



#----------------------------------------------------------------------------------------------------
# WAP to print number is odd or not

# num=int(input("Enter your age:"))
# if num%2!=0:
#     print(num,"This number is odd number")
# else:
#     print(num,"This is even number")


#----------------------------------------------------------------------------------------------------
# WAP to iterate even number.

# num=[11,22,33,44,55,66,77,88,99,100]
# for i in num:
#     if i%2==0:
#         print(i)


#----------------------------------------------------------------------------------------------------
# WAP iterate odd number

# number=[11,22,33,44]
# for num in number:
#     if num%2!=0:
#         print(num)

#----------------------------------------------------------------------------------------------------
# WAP to print passs student name

# result={'jay':89,'ajay':32,'vijay':67,'sujay':29}
# for i,j in result.items():
#     if j>=40:
#         print(i)



#----------------------------------------------------------------------------------------------------
# WAP to print list of name of failed student

# result={'jay':89,'ajay':32,'vijay':67,'sujay':29}
# fail=[]
# for i,j in result.items():
#     if j<=40:
#         fail.append(i)
# print(fail)





#-------- 29/11/2024 ---------------------------------------------------------------------------------
# WAP to print dict of pass stud - (critria 40)

# result={'jay':89,'ajay':32,'vijay':67,'sujay':29}
# dict={ }
# for key,value in result.items():
#     if value>=40:
#         dict[key]=value
# print(dict)




#----------------------------------------------------------------------------------------------------
# WAP to print number from list which is divisible by 4 and 3

# l=[11,22,4,5,6,7,13,12,8,9]
# for i in l:
#     if i%4==0 and i%3==0:
#         print(i)




#----------------------------------------------------------------------------------------------------
#=========== else STATEMENT==========================================================================
#----------------------------------------------------------------------------------------------------
# per=eval(input("Enter percent"))
# if per>90:
#     print("Government")
# else:
#     print("Private")



#----------------------------------------------------------------------------------------------------
# odd , even number nikalo in list formate

# l=[11,22,33,44,55,66]
# even=[]
# odd=[]
# for num in l:
#     if num%2 == 0:
#         even.append(num) 
#     else:
#         odd.append(num)
# print(even)  
# print(odd)



#----------------------------------------------------------------------------------------------------
# jinke marks 50 se jada hai unke 2 se bdawoo and jiske kam hai 50 se unke 5 se bdawoo

# result={'jay':78,'ajay':45,'sujay':67,'vijay':41}
# for i,j in result.items():
#     if j>50:
#         result[i]=j+2 
#     else:
#         result[i]=j+5 
# print(result)



#----------------------------------------------------------------------------------------------------
# WAP to print pass student pass and fail student   (40) is criteria

# result={'jay':78,'ajay':45,'sujay':67,'vijay':41,'arun':23,'kunal':39}
# p=[]
# f=[]
# for name,per in result.items():
#     if per >= 40:
#         p.append(name) 
#     else:
#         f.append(name)
# print(p)
# print(f)



#----------------------------------------------------------------------------------------------------
# create dict represent square of even number and cube of odd number from 11 to 20

# d={ }
# for num in range(11,21):  
#     if num%2==0:
#         d[num]=num**2  
#     else:
#         d[num]=num**3 
# print(d)





#------30/11/2024 -----------------------------------------------------------------------------------

# vishal=eval(input("Enter age:-"))
# kunal=eval(input("Enter age:-"))
# if vishal>kunal:
#     print("vishal")
# else:
#     print("kunal")


#----------------------------------------------------------------------------------------------------

# dishant_age=int(input("Enter age"))
# gaurav_age=int(input("Enter age"))
# vishal_age=int(input("Enter age"))
# if dishant_age>gaurav_age and dishant_age>vishal_age:
#     print("Dishant")
# elif gaurav_age>dishant_age and gaurav_age>vishal_age:
#     print("Gaurav")
# else:
#     print("Vishal")


#----------------------------------------------------------------------------------------------------

# first=eval(input("Enter number:"))
# opr=input("enter operator:")
# second=eval(input("Enter number:"))
# if opr== '+':
#     print(first+second)
# elif opr == '-':
#     print(first-second)
# elif opr == '*':
#     print(first-second)
# elif opr == '/':
#     print(first-second)
# else:
#     print("check number or opr properly.")


#----------------------------------------------------------------------------------------------------

# employ={'manoj':40000,'mandar':2000,'ashok':50000,'vishal':35000}
# for i in employ:
#     print(i)


#----------------------------------------------------------------------------------------------------

# employ={'manoj':40000,'mandar':2000,'ashok':50000,'vishal':35000}
# for sal in employ.values():
#     print(sal)

#----------------------------------------------------------------------------------------------------

# employ={'manoj':40000,'mandar':2000,'ashok':50000,'vishal':35000}
# for name,sal in employ.items():
#     print(name,sal)


#----------------------------------------------------------------------------------------------------

# WAP to print nameof employ havingsalaryis more tham 36000

# employ={'manoj':40000,'mandar':2000,'ashok':50000,'vishal':35000}
# for name, salary in employ.items():
#     if salary > 36000:
#         print(name)



#----------------------------------------------------------------------------------------------------
#jinki salary jada hai 36000 se unko yek list me ans jinki kam hai unko yek iist me ais 2 list me store kro

# employ={'manoj':40000,'mandar':2000,'ashok':50000,'vishal':35000}
# gret=[]
# less=[]
# for name,salary in employ.items():
#     if salary>36000:
#         gret.append(name)
#     else:
#         less.append(name)
# print(gret)
# print(less)



#----------------------------------------------------------------------------------------------------
# jinki sal 36000 se kam hai unki salary bdawoo 4000 se.

# employ={'manoj':40000,'mandar':2000,'ashok':50000,'vishal':35000}
# for name,salary in employ.items():
#     if salary<36000:
#         employ[name]=salary+4000
# print(employ)



#----------------------------------------------------------------------------------------------------

# employ={'manoj':40000,'mandar':2000,'ashok':50000,'vishal':35000}
# for name,salary in employ.items():
#     if salary>36000:
#         employ[name]=salary+(salary *5 /100) 
#     else:
#         employ[name]=salary+(salary *15 /100)
# print(employ)


#----------------------------------------------------------------------------------------------------

# l=[4,15,9,18,67,34,12,5,108,12]
# div_by_4=[]
# div_by_5=[]
# div_by_9=[]
# for num in l:
#     if num%4==0:
#         div_by_4.append(num)
#     elif num%5==0:
#         div_by_5.append(num)
#     elif num%9==0:
#         div_by_9.append(num)
# print(div_by_4)
# print(div_by_5)
# print(div_by_9)


#----------------------------------------------------------------------------------------------------

# num=int(input("enter number:-"))
# for i in range(2,num):
#     if (num%i==0):
#         print("prime number")
#         break
#     else:
#         print("Not a prime number")

# for i in range(2, num):
#     if num % i == 0:
#             print("prime")
#             break
#     else:
#         print(f"{num} is a prime number.")


#----------------------------------------------------------------------------------------------------
'''2] WAP to calculate total marks in 5 subject (Full marks =100) as well as percentage of marks and 
    division as per the following condition   '''

# a=int(input("Enter 1st sub marks:"))
# b=int(input("Enter 2nd sub marks:"))
# c=int(input("Enter 3rd sub marks:"))
# d=int(input("Enter 4th sub marks:"))
# e=int(input("Enter 5th sub marks:"))
# total=a+b+c+d+e
# percent=(total / 500)*100
# print("Total Marks:",total,"Percentage:",percent)
# if percent>=80:
#     print("you have got Grade A")
# elif percent>=60:
#     print("you have got Grade B")
# elif percent>=40:
#     print("you have got Grade C")
# else:
#     print("you have got Grade D")


