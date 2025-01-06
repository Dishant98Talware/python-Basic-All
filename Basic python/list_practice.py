#1] count 44 how many time appear

# l=[11,22,33,44,["Dishant","Ayush","Ram"],55,66,[1,2,3,4,5],44,["A","B","C"],44,55,66]
# print(l.count(44))



#2] add 100 at end of list

# l=[11,22,33,44,["Dishant","Ayush","Ram"],55,66,[1,2,3,4,5],44,["A","B","C"],44,55,66]
# l.append(100)
# print(l)


# add new list at the end of list [100,200,300]

# l=[11,22,33,44,["Dishant","Ayush","Ram"],55,66,[1,2,3,4,5],44,["A","B","C"],44,55,66]
# l.append([100,200,300])
# print(l)




# add 55 after second 44

# l=[11,22,33,44,["Dishant","Ayush","Ram"],55,66,[1,2,3,4,5],44,["A","B","C"],44,55,66]
# l.insert(9,55)
# print(l)




# add 55,66 after second 44

# l=[11,22,33,44,["Dishant","Ayush","Ram"],55,66,[1,2,3,4,5],44,["A","B","C"],44,55,66]
# l.insert(9,66)
# l.insert(9,55)
# print(l)



#  ram ke bad sham

# l=[11,22,33,44,["Dishant","Ayush","Ram"],55,66,[1,2,3,4,5],44,["A","B","C"],44,55,66]
# l[4].append("Sham")
# print(l)




# 1,2,3,4,5 reverse

# l=[11,22,33,44,["Dishant","Ayush","Ram"],55,66,[1,2,3,4,5],44,["A","B","C"],44,55,66]
# x=l[7]
# x.reverse()
# print(x)



# A,B,C  Delete

# l=[11,22,33,44,["Dishant","Ayush","Ram"],55,66,[1,2,3,4,5],44,["A","B","C"],44,55,66]
# l.pop(9)
# print(l)

# l.remove(["A","B","C"])
# print(l)
# print(l)



# 55,66 remove and add 100,200

# l=[11,22,33,44,["Dishant","Ayush","Ram"],55,66,[1,2,3,4,5],44,["A","B","C"],44,55,66]
# l.remove(55)
# l.remove(66)
# l.insert(5,200)
# l.insert(5,100)
# print(l)


# a,b,c ko delete kro & last ke 44,55,66 ko list me dalo

# l=[11,22,33,44,["Dishant","Ayush","Ram"],55,66,[1,2,3,4,5],44,["A","B","C"],44,55,66]
# l.remove(["A","B","C"])
# l.pop(-3)
# l.pop(-2)
# l.pop(-1)
# l.append([44,55,66])
# print(l)




# sort and sorted function 

# l1=[4,2,3,1,5]
# l1.sort()
# print(l1)
# l1.append(33)
# print(l1)
# print(l1)


# l1=[4,2,3,1,5]
# print(sorted(l1))
# l1.append(99)
# print(l1)