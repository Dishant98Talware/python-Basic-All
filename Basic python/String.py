'''               String
String is collection of character  '''


'''    string with in 
    ' '
    " "
    """ """               '''
#---------------------------Indexing-----------------------------------------------------------

# name="Dishant Talware"
# print(name)            # Dishant Talware
# print(type(name))      # <class 'str'>

# name="rameshwaram"
# print(name[-1])     # m
# print(name[0])      # r
# print(name[6])      # w
# print(name[-11])    # r
# print(name[-6])     # h



#------------------Slicing--------------------------------------------------------------------------
# a= [SI:EI:SV]


# name="instagram"
# print(name[::-1])      # margatsni
# print(name[0:5:1])    # insta
# print(name[3:-3:1])   # tag
# print(name[0:-4:2])   # isa
# print(name[5:9])      # gram
# print(name[5: :1])    # gram
# print(name[-6:15:1])  # tagram
# print(name[-1: :-2])   # mrasi       Reverse me 1 increment
# print(name[-1: :-1])   # margatsni   
# print(name[0: :2])     # isarm


#--------------------------------------------------------------------------------------------------

# name="pavankumar"
# print(name[5: :])   # kumar
# print(name[:-5])    # pavan
# print(name[-1:-6:-1]) # ramuk
# print(name[4: :-1])  # navap






# -------------------------------Function / Method---------------------------------------------------
# ----------------------------------upper------------------------------------------------------------
# name="dishant"
# name1= name.upper()
# print(name1)       # DISHANT

# print(name.upper())  # DISHANT



# ------------------------------------lower--------------------------------------------------------------
# name="DISHANT"
# name1= name.lower()
# print(name1)      # dishant

# print(name.lower())  # dishant


# -----------------------------------title--------------------------------------------------------------
# name="dishant talware"
# name1= name.title()
# print(name1)         # Dishant Talware

# print(name.title()) # Dishant Talware

# ------------------------------------capitalize---------------------------------------------------------
# name="dishant talware"
# ame1= name.capitalize()
# print(name1)              # Dishant talware

# print(name.capitalize())  # Dishant talware



# ---------------------------------isalpha---------------------------------------------------------------------
# name="dishant talware"
# print(name.isalpha())    # False

# name="dishanttalware"
# print(name.isalpha())    # True



# ---------------------------------isnumeric---------------------------------------------------------------------
# num="3462478"
# print(num.isnumeric())  # True

# num="tyhfg"
# print(num.isnumeric())  # False

# num="R3462478"
# print(num.isnumeric())  # False

# n="Di63sh7ant123"
# for i in n:
#     if i.isalpha():
#         print(i)         # sequence me :- D i s h a n t


# n="Di63sh7ant123"
# for i in n:
#     if i.isnumeric():
#         print(i)          # sequence me number :-  6 3 7 1 2 3


# n="Di63sh7ant123"
# for i in n:
#     if i.isnumeric():
#         print(int(i)**2)    # sequence me square 36 9 49 1 4 9




# ----------------------------------isupper-------------------------------------------------------------
# num="JAVA BY KIRAN"
# print(num.isupper())  # True

# num="Java by kiran"
# print(num.isupper())  # False

# num="JAVA by746Kiran"
# print(num.isupper())  # False

# l=["DISHANT", "rajesh", "RISHANT", "shantanu"]
# for i in l:
#     if i.isupper():
#         print(i)     # upper wale sabhi name output DISHANT RISHANT in sequence




# ---------------------------------isspace--------------------------------------------------------------
# name="Dishant Talware"
# print(name.isspace())  # False

# name="  "
# print(name.isspace())  # True



# ---------------------------------isalpha--------------------------------------------------------------
# clg="Sipna clg engg"
# print(clg.isalpha())  # False

# clg="Sipnacgengg"
# print(clg.isalpha())  # True

# clg="Sipna565cgengg"
# print(clg.isalpha())  # False



# --------------------------endswith--------------------------------------------------------------------
# name="Dishant Talware"
# print(name.endswith("re"))   # True



# ------------------------------capitalize--------------------------------------------------------------
# clg="sipna engg"
# print(clg.capitalize())  # Sipna engg



# -----------------------------replace--------------------------------------------------------------------
# name="tryhant"
# print(name.replace("try","Dis"))  # Dishant



# ------------------------------find-------------------------------------------------------------------
# char="java by kiran"
# print(char.find("a"))  # 1
# print(char.find("k"))  # 8


# --------------------------isalnum-----------------------------------------------------------------------
# lmn="hdfhjfd756"
# print(lmn.isalnum())  # True

# lmn="hdfh@jfd756"
# print(lmn.isalnum())  # False

# lmn="DishantTalware"
# print(lmn.isalnum())  # True

# lmn="Dishant_Talware"
# print(lmn.isalnum())  # False


# -----------------------------count--------------------------------------------------------------------
# plo="jk$ $ jkfjk $ jklfj"
# print(plo.count("$"))    # 3



# ---------------------------split----------------------------------------------------------------------
# name="Dishant Talware"
# print(name.split())      # ['Dishant', 'Talware']

# name="i am Dishant and my id is 1211"
# print(name.split())       # ['i', 'am', 'Dishant', 'and', 'my', 'id', 'is', '1211']


# name="Dish#ant Ta#lware"
# print(name.split(sep="#"))  # ['Dish', 'ant Ta', 'lware']

# name="Dishant Talware"
# print(name.split(sep="a"))   # ['Dish', 'nt T', 'lw', 're']


#---------------------------------------------------------------------------------------------------
