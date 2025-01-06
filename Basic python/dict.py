#------------------------------------------------------------------------------------------
#============================ dict { } ====================================================

# dict is a quama seperated key and value pair within curlybracket, it is mutable,order,duplicate key are not allow

# key unique / not duplicate  key only immutable 



#-----------------------------------------------------------------------------------------------

# details={"name":"Dishant","age":21,"marks":89}
# print(details)            # {'name': 'Dishant', 'age': 21, 'marks': 89}
# print(type(details))      # <class 'dict'>


# details={
#     "name":"Dishant",
#     "age":21,
#     "marks":89
# }
# print(details)         # {'name': 'Dishant', 'age': 21, 'marks': 89}
# print(type(details))   # <class 'dict'>




#--------key explanation --------------------------------------------------------------------------
# duplicate key not allow (unique) / aagar dalte ho to value update hoti hai. (key is immutable type like int,float tuple,string)

# key mai mutable nhi use kr sakte

# dict={1:"dishu",2:"kullu",3:"rahul",1:"Dishant"}
# print(dict)




#------- value explanation ----------------------------------------------------------------------------
# value duplicate are allow  /   mutable , immutable alllow  / sare data type allow fundamental, collective


# details={
#     'name':"Dishant",'age':22,'per':22,'marks':[89,22,33],
#     'name1':'Rishant','rtrt':{22},'perr':(3434),'markss':{'datastru':{67}}
# }
# print(details)




#------------------------------------------------------------------------------------------------

# dishant_details={
#     'name':'Dishant',
#     'age':21,
#     'city':'Amravati',
#     'per':89
# }
# print(dishant_details)





#------------------------------------------------------------------------------------------------
# 3 sub ke marks dalne hai

# dishant_details={
#     'name':'Dishant',
#     'age':21,
#     'city':'Amravati',
#     'per':89,
#     'subject':{'CD':98,'DBMS':90,"DAA":85,"TOC":67}
# }
# print(dishant_details)




#-------add 1 to 5 square in dict ----------------------------------------------------------------
#dict ke andar 1 to 5 square represent krne hai

# square={1:1,2:4,3:9,4:16,5:25,6:36,7:39}
# print(square)


# dict={}
# for i in range(1,6,1):
#     dict[i]=i*i
# print(dict)




#------------------------------------------------------------------------------------------------
# fev single movie ke bareme data relise kro

# movie={
#     'movie1':{'name':'Dilwale Dulhaniya le jayenge','hero':'Shah Rukh khan','heroine':'Kajol','relize':1995,'director':'Aditya chopra'},
#     'movie2':{'name':'Kuch kuch hota hai','hero':'Shah Rukh khan','heroine':'Kajol','year':1998,'director':'karan johar'}
#     }
# print(movie)


#=============================================================================
# SIMPLE SYNTAX FOR STORE MANY DATA

# allu={'dj':{ },'sos':{ },'lucky':{ }}

#=============================================================================





#------------------------------------------------------------------------------------------------
# how to access data from dict{}
# returnn

# vivo={'model':'y81','color':'skyblue','ram':'8gb','storage':128}
# print(vivo['ram'])       # 8gb
# print(vivo.get('ram'))   # skyblue



# vivo={
#     'y81':{'model':'y81','color':'skyblue','ram':'8gb','storage':128}, 
#     'y75 5G':{'model':'y75','color':'black','ram':'16gb','storage':256},
# }
# print(vivo['y81'])           # {'model': 'y81', 'color': 'skyblue', 'ram': '8gb', 'storage': 128}
# print(vivo['y81']['color'])  # skyblue




#------------------------------------------------------------------------------------------------
# WAP to craete dict of square of number from 1 to 10

# square={}
# for number in range(1,11):
#     square[number]=number*number
# print(square)
    






#------- add data --  key & value dono bhi -----------------------------------------------------------
# how to add data from dict{}
# vname[key]=value

# square={1:1,2:4,3:8}
# square[4]=16
# print(square)




#-------- update data --------------------------------------------------------------------------------
# a14 and a15 color add krna hai
#vname['key]='updatedvalue'


# oppo={'a14':{'ram':'16gb','storage':'128gb'},
#       'a15':{'ram':'16gb','storage':'128gb'}
# }
# oppo['a14']['ram']='4gb'
# oppo['a15']['storage']='264gb'
# print(oppo)




#---------- delete data -------------------------------------------------------------------------
#-------- pop ----------------------------------------------------------------------------------
#pop
#del

# vname.pop(key)

# details={"name":"Dishant","age":21,"marks":89}
# details.pop('marks')
# print(details)
# print(details.pop('name'))    # ye return dega



# s1={'name':"jay",'age':21,'per':89}
# s1.pop('per')
# print(s1)          # {'name': 'jay', 'age': 21}

# print(s1.pop('age'))   # ye value ko return deta hai


# pop age of ABcd by using pop

# batch1211={1:{'name':"jay",'age':21,'per':89},
#            2:{'name':"ABcd",'age':787,'per':8999}}

# batch1211[2].pop('age')
# print(batch1211)


#-------- del ----------------------------------------------------------------------------------

#del
# del var[key]

# s1={'name':"jay",'age':21,'per':89}
# del s1['per']
# print(s1)


# batch1211={1:{'name':"jay",'age':21,'per':89},
#            2:{'name':"jay",'age':21,'per':89}}
# del batch1211[2]['per']
# print(batch1211)

#-------- max -------------------------------------------------------------------------------------

# l={ 1:34 , 2:44 , 3:89 }
# print(max(l.values()))

# print(min(l.values()))

#------- iteration in nested list -----------------------------------------------------------------

# l=[[1,2,3],[4,5,6],[7,8,9]]
# for i in l:
#     print(i)


# nested for loop

# l=[[1,2,3],[4,5,6],[7,8,9]]
# for i in l:
#     for j in i:
#         print(j)





#===========   FUNCTION OD DICT ===========================================================
#------- KEYS-----------------------------------------------------------------------------
# method of dict
# keys       ye retuen me deti hai list of all keys

# details={"name":"Dishant","age":21,"marks":89}
# details.keys()
# print(details)     # aisa lihka to key & value dono bhi return krega

# print(details.keys())   # return deta hai  (aise hi likhna pdta hai)


#----------  VALUE ----------------------------------------------------------------------------

# details={"name":"Dishant","age":21,"marks":89}
# details.values()
# print(details)            # aisa lihka to key & value dono bhi return krega

# print(details.values())   # retuen deta hai 



#----------  ITEMS --------------------------------------------------------------------------
#items --> return of all keys and values

# details={"name":"Dishant","age":21,"marks":89}
# details.items()
# print(details)           # ye bhi return kera hai but dict me (yani direct details ko print kr raha hai)

# print(details.items())     # return deta hai


#------------------------------------------------------------------------------------------------
#  dict() function

# del()   ----> to create empty dict

# d=dict()
# print(d)
# print(type(d))

#------------------------------------------------------------------------------------------------

# len() -----> return deta hai

# d={'name':'dishant','age':24,"marks":89}
# print(len(d))                            #  direct print me likhna pdega 

#------------------------------------------------------------------------------------------------

# clear()

# d={'name':'dishant','age':24,"marks":89}
# d.clear()
# print(d)

#------------------------------------------------------------------------------------------------

# get() ----->  to get the value associated with the key ( return deta hai)

# d={'name':'dishant','age':24,"marks":89}
# print(d.get('name'))

# print(d['name'])    # by using key


#------------------------------------------------------------------------------------------------
# pop      return deta hai

# d={'name':'dishant','age':24,"marks":89}
# d.pop('name')
# print(d)

# print(d.pop('age'))




#------------------------------------------------------------------------------------------------
#  popitems() ----> return krta hai   
# ye last ki key & values delete krta hai & return bhi krta hai

# d={'name':'dishant','age':24,"marks":89}
# d.popitem()
# print(d)         

# print(d.popitem())



#------------------------------------------------------------------------------------------------


# keys()
# values()
#items()

#------------------------------------------------------------------------------------------------

# #copy()  ---------> return krta hai

# d={'name':'dishant','age':24,"marks":89}
# d1=d.copy()
# print(d1)

# print(d.copy())



#------------------------------------------------------------------------------------------------

# setdefault()  ------> if the key alredy available the it will not update value and not print the value

# d={'name':'dishant','age':24,"marks":89}
# d.setdefault('clg','SCOEAT')
# print(d)

# print(d.setdefault('clg','SCOEAT'))  # ye only SCOEAT dega
# d.setdefault('name','djsdskl')
# print(d)


#------------------------------------------------------------------------------------------------

# update()

#------------------------------------------------------------------------------------------------
#-------  ITERATION  -----------------------------------------------------------------------------

# details={"name":"Dishant","age":21,"marks":89}
# for i in details:
#     print(i)             # all KEYS ko return krega
    
    

# details={"name":"Dishant","age":21,"marks":89}
# for i in details:
#     print(details[i])    # value nikalega


# s1={'name':"jay",'age':21,'per':89}
# for i in s1.values():
#     print(i)                 #  all values nikalega


# s1={'name':"jay",'age':21,'per':89}
# for i in s1.items():
#     print(i)                     # key and values dega in tuple
    
    

# s1={'name':"jay",'age':21,'per':89}
# for i,j in s1.items():
#     print(i,j)                  # key and values dega not in tuple only value




#------------------------------------------------------------------------------------------------
# check if the key exist or not

# person={'name':'jphm','age':25,'profession':'developer'}
# if 'profession' in person:
#     print("yes")
# else:
#     print('no')


#------------------------------------------------------------------------------------------------
# check profession key exist or not in dict

# person={'name':'Dishant','age':29,'profession':'developer'}
# if 'profession' in person:
#     print("yes")
# else:
#     print("no")


#------------------------------------------------------------------------------------------------
# murge 2 dict

# person={'name':'Dishant','age':29,'profession':'developer'}
# lm={'name1':'Dishant','age1':29,'profession1':'developer'}


# person |=lm
# print(person)

# result=person |lm
# print(result)


#------------------------------------------------------------------------------------------------
# store all key and value in dict

# person={'name':'Dishant','age':29,'profession':'developer'}
# l=[]
# for key in person:
#     l.append(key)
# print(l)

# for key in person.keys():
#     l.append(key)
# print(l)

# for key in person.values():
#     l.append(key)
# print(l)



#------------------------------------------------------------------------------------------------
# sort dict keys

# person={'name':'Dishant','age':29,'profession':'developer'}
# sorr=dict(sorted(person.items()))
# print(sorr)

