#------------------------------------------------------------------------------------------
#============================ dict{}, practice  ===========================================

# 3 student ki details show krni hai
# bar bar likha to duplicate key aayegi
# 1,2 are key baki value


# batch1211={
#     1:{'name':'Dishant','age':21,'city':'pune'},
#     2:{'name':'Talware','age':21,'city':'pune'}
# }
# print(batch1211)




#------------------------------------------------------------------------------------------------

# vivo={
#     'y81':{'model':'y81','color':'skyblue','ram':'8gb','storage':128}, 
#     'y75 5G':{'model':'y75','color':'black','ram':'16gb','storage':256},
# }
# print(vivo)




#------------------------------------------------------------------------------------------------
# 3 cars ke model ki details

# car_info = {
#         "model_1": {"name": "BMW 3 Series 320i","engine": "2.0L 4-cylinder","horsepower": 180,"price": "$42,000"},
#         "model_2": {"name": "BMW 3 Series 330i","engine": "2.0L 4-cylinder Turbo","horsepower": 255,"price": "$47,000"},
#         "model_3": {"name": "BMW 3 Series M340i","engine": "3.0L 6-cylinder Turbo","horsepower": 382,"price":"$56,000"}
# }
# print(car_info)




#------------------------------------------------------------------------------------------------
# write a program to create Dict to represent result of 10 student


# student={}
# for number in range(1,11):
#     student['student',number]=int(input("Enter Marks:-"))
# print(student)
    
    
# student={}
# for i in range(2):
#     roll=int(input("Enterr roll no"))
#     per=int(input("Enterr per"))
#     student[roll]=per 
# print(student)



# isme per +1 se bdega

# result={1:45,2:67,3:87,4:78}
# for roll,per in result.items():
#     result[roll]=per+1
# print(result)








#===============================================================================================
#                     Dict Question (practice)
#------------------------------------------------------------------------------------------------
# you can change the value of specific item by refering to its key name

# dict={'brand':'suzuki','model':'Dzire','year':2020}
# dict['year']=1015
# print(dict)



#------------------------------------------------------------------------------------------------
# dict ko list me conver krna matlab typecasting krna

# student={
#     'name':'Dishant',
#     'age':21,
#     'marks':98.21
# }
# print(student)         # {'name': 'Dishant', 'age': 21, 'marks': 98.21}
# print(list(student))   #['name', 'age', 'marks']
# print(len(student))    # 3

# print(student.keys())   # dict_keys(['name', 'age', 'marks'])
# print(student.values()) # dict_values(['Dishant', 21, 98.21])
# print(student.items())    # dict_items([('name', 'Dishant'), ('age', 21), ('marks', 98.21)])

# print(list(student.keys()))       # ['name', 'age', 'marks']
# print(len(list(student.keys())))  # 3

# print(student.update({'clg':'SCOEAT'}))

#------------------------------------------------------------------------------------------------
# meko sirf 1 key and value chaiye to 

# student={
#     'name':'Dishant',
#     'age':21,
#     'marks':98.21
# }
# pairs=list(student.items())   # list likhna compulsary
# print(pairs[0])               # ('name', 'Dishant')


#------------------------------------------------------------------------------------------------
# sum of all list

# l=[1,2,3,4,5,6]
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)

#------------------------------------------------------------------------------------------------

# 1. create a dict to store the names and ages of three people.add()

# people={1:{'name':'Dishant','age':22},
#         2:{'name':'Prashant','age':25},
#         3:{'name':'Nishant','age':56}}
# print(people)


#------------------------------------------------------------------------------------------------

# 2. Access the value
# Given a dict, access the value associated with a specific key

# info={'name':'Nishant','age':56,'per':89,'clg':'SCOEAT'}
# print(info['clg'])


#------------------------------------------------------------------------------------------------
# 3. add new key-value pair
# Add new key value pair in dict

# info = {'name': 'Nishant', 'age': 56, 'per': 89, 'clg': 'SCOEAT'}
# info['marks'] = 56
# print(info)

#------------------------------------------------------------------------------------------------
# 4. Update a value
# Update the age of a specific person in the dict


# info={'name':'Nishant','age':56,'per':89,'clg':'SCOEAT'}
# info['age']=22
# print(info)



#------------------------------------------------------------------------------------------------
# 5. remove the key value pair
# remove a person from dict

# info={'name':'Nishant','age':56,'per':89,'clg':'SCOEAT'}
# info.pop('name')
# print(info)

#------------------------------------------------------------------------------------------------
# 6 check if key exists
# check if a specific person is in dict

# info={'name':'Dishant','age':21,'per':89,'clg':'SCOEAT'}
# if info['name']=='Dishant':
#     print("Yes")
# else:
#     print("no")
    
#------------------------------------------------------------------------------------------------
# 7.  iterate through key
# print all the names in dict

# person = {
#     1: {'name': 'Dishant', 'age': 21, 'per': 89, 'clg': 'SCOEAT'},
#     2: {'name': 'Prashant', 'age': 26, 'per': 81, 'clg': 'PRMT'},
#     3: {'name': 'Nishant', 'age': 23, 'per': 79, 'clg': 'GODE'}
# }
# for i in person:
#     print(person[i]['name'])

#------------------------------------------------------------------------------------------------

# 8 iterate through value
# print all age in dict

# person = {
#     1: {'name': 'Dishant', 'age': 21, 'per': 89, 'clg': 'SCOEAT'},
#     2: {'name': 'Prashant', 'age': 26, 'per': 81, 'clg': 'PRMT'},
#     3: {'name': 'Nishant', 'age': 23, 'per': 79, 'clg': 'GODE'}
# }
# for i in person:
#     print(person[i]['age'])

#------------------------------------------------------------------------------------------------
# 9 iterate through key-value pairs
# print all names with their age

# person = {
#     1: {'name': 'Dishant', 'age': 21},
#     2: {'name': 'Prashant', 'age': 26},
#     3: {'name': 'Nishant', 'age': 23}
# }
# for i,j in person.items():
#     print(j['name'],j['age'])

#------------------------------------------------------------------------------------------------
#10 merge two dict
# merge two dict into one


# person1 = {'a': 1, 'b': 2}
# person2 = {'b': 3, 'c': 4}
# person1.update(person2)
# print(person1)

#------------------------------------------------------------------------------------------------
# 11.  Count Occurrences
# given a list of fruit and count the occurence of each fruit using dict in python without using if

# fruits = ['apple', 'banana', 'orange', 'apple', 'banana', 'apple']
# fruit_count = {}
# for fruit in fruits:
#     fruit_count[fruit] = fruit_count.get(fruit, 0) + 1
# print(fruit_count)

#------------------------------------------------------------------------------------------------


# 12. find max value
# find the person with the maximum age in the dict

# person = {
#     1: {'name': 'Dishant', 'age': 21},
#     2: {'name': 'Prashant', 'age': 26},
#     3: {'name': 'Nishant', 'age': 23}        # wrong
# }
# for i in person:
#     max=max(i.values())
#     print(max)

# d={'fdf':56,'yt':67,'kjijk':87}
# gh=max(d.values())
# print(gh)

#------------------------------------------------------------------------------------------------

# s2 nikalna hai

# result={1:{'s1':78,'s2':67},2:{'s1':68,'s2':57}}
# print(result[1].get('s2'))  
# print(result[2].get('s2')) 


#------------------------------------------------------------------------------------------------

#total per calculate kro#

# students = {
#     'Dishant': {'sub1': 75, 'sub2': 85, 'sub3': 90, 'sub4': 80, 'sub5': 70},
#     'Prashant': {'sub1': 60, 'sub2': 70, 'sub3': 65, 'sub4': 80, 'sub5': 75},
#     'Nishant': {'sub1': 88, 'sub2': 92, 'sub3': 85, 'sub4': 78, 'sub5': 80},
#     'Rishant': {'sub1': 90, 'sub2': 85, 'sub3': 95, 'sub4': 80, 'sub5': 85}
# }
# per={}
# for roll,marks in students.items():
#     total_marks=sum(marks.values())  
#     percentage=(total_marks/500)*100 
#     per[roll]=percentage
# print(per)



#total per calculate kro

# Dishant={'sub1': 75, 'sub2': 85, 'sub3': 90, 'sub4': 80, 'sub5': 70}
# total_marks=len(Dishant)*100
# ob_marks=0
# for marks in Dishant.values():
#     ob_marks=ob_marks+marks
# per=(ob_marks/total_marks)*100
# print(per)

#--------------------------------------------------------------------------------------------
# create 2 dict in 1

# d1={1:100,2:200,3:300}
# d2={4:400,5:500,6:600}
# d1.update(d2)
# print(d1)


#--------------------------------------------------------------------------------------------
# multiply all values in dict

# dict= {1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
# m=1
# for i in dict:
#     m=m*dict[i]
# print(m)


#--------------------------------------------------------------------------------------------
# calculate sum of all values in dict

# dict= {1: 100, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}
# total=sum(dict.values())
# print(total)


#--------------------------------------------------------------------------------------------
# count the sequence of words appering in a string

# a=input("enter string:-")
# l=a.split()
# d={}
# for i in l:
#     if i not in d.keys():
#         d[i]=0
#     d[i]=d[i]+1
# print(d)

# #--------------------------------------------------------------------------------------------


#--------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------

# details={"name":"Dishant","age":21,"marks":89}
# d={'a':1,'b':2,'c':3,'d':4}
# print(type(details))
# print(len(details))

'''dono bhi value return krte hai but in case key doessnt exist 1st error return krega and   
    .get (none) print'''
# print(details['name'])
# print(details.get("name"))
# print(details.get("clg", "key not exist"))


# print(details.keys())
# print(details.values())
# print(details.items())


# print(details.fromkeys('dish',12,))
# print(details.fromkeys(['dishant','rishant','llm'],198))
# print(details.fromkeys(('A','B','C'),(1,2,3,4)))
# sd=details.fromkeys(('A','B','C'),(1,2,3,4))
# print(sd)


# print(details.setdefault('clg','scoeant'))
# details.setdefault('frnd','Dishant')
# print(details)
# print(details.setdefault('name','rishant'))   # setdefault me agagr key alredy hai to wo muje value return krke dega.



# details.update(d)
# print(details)
# print(details.update(d))   # none


# print(details.pop('age'))
# details.pop('name')
# print(details)

# print(details.popitem())  # koie key value nhi lega but last ke key and value ko remove krega.  aagar 


# details.clear()
# print(details)
# print(details.clear())  #None
# print(type(details))


#-----------------------------------------------------------------------------------------------
# print percent of total sub

# sub={'TOC':76,'DBMS':87,'DAA':90,'SE':56}
# total=sum(sub.values())
# per=(total/(len(sub)*100))*100
# print(per)