# print("hello")
# print("hello")


# a=10
# print(a)

# name="san"
# print(name)
# print("type of name", type(name))  #check data type
# print("len", len(name)) #check length


# # indexing
# print(name[0])
# print(name[1])

# # slicing
# print(name[0:2])


# # operation
# name="san"
# upper_case=name.upper()

# last="kumar"
# lower_case=last.lower()       

# name="ritik"
# title_name=name.title()          it capitalizes the first letter of every word

# cap_name=name.capitalize()       it capitalizes the first letter of a string
# print(name.count("r"))

# name = "ritik "
# last="kumar"
# print(name+last)



# >>>>>>>>>>>>>>> list >>>>>>>>>>

# heterogeneous=stores multiple data types, mutable, indexing, slicing, allows duplicates,[]

# array-homogeneous, faster, memory allocation


# my_list=[1,2,4,5,6.7,1]
# print("my lis is", my_list)
# print(type(my_list))
# print(len(my_list))
# print(my_list.count(1))


# print("indexing= ",my_list[3])
# print("slicing= ",my_list[0:5])
# print(my_list[::-1])
# print(my_list.reverse())

# s="hello"
# rev=s[::-1]
# print(rev)

# my_list.append(100)
# print(my_list)

# my_list.clear()
# print(my_list)


# my_list.sort()
# print(my_list)
# my_list.pop()
# print(my_list)

# my_list.pop(2)
# print(my_list)


# my_list[0]=1000
# print(my_list)

# my_list=[1,2,4,5,6.7,1]
# copy_list =my_list.copy()
# print(copy_list)

# my_list.insert(0, 1000)
# print(my_list)

# my_list= [1,2,4,5,6.7,1]
# reverse_list= my_list.reverse()
# print(reverse_list)

# The code gives None as output because the reverse() function modifies 
# the original list in place and does not return a new list. Instead of producing 
# a reversed version as a separate value, it simply updates the existing list and
# returns None by default. When the result of my_list.reverse() is assigned to
# reverse_list, the value stored is actually None, not the reversed list. Therefore,
# printing reverse_list displays None instead of the expected list.


# a = [1, 2]
# b = [3, 4]
# print(a + b)  # Output: [1, 2, 3, 4]
# a = [1, 2]
# print(a * 2)  # Output: [1, 2, 1, 2]






# >>>>>>>>>>>>tuple>>>>>>>>>>>>

# # immutable, contains multiple data types, allows duplicates
# tpl=(1,2,3,4,5)
# print(tpl)
# # print(type(tpl))
# # print(len(tpl))
# # print(tpl.count(3))
# # print(tpl.index(3))
# # print(tpl[1])
# print(tpl)
# tpl[0]=100

# name=1,2,3,4,5,6,67
# print(name)
# print(type(name))


#####tuple unpacking

# name=("ritik","divya","rohit")
# print(name)
# print(type(name))

# # num=(1,2,3,4)
# a,b,c=num
# print(a)              #value error
# print(b)
# print(c)

# num=(1,2)
# a,b,c=num
# print(a)
# print(b)        #value error
# print(c)


# tpl1=(1,2,3,4,5)
# tpl2=(1,2,3,4,5)
# print(tpl1+tpl2)
# print(tpl1*tpl2)
# print(tpl1/tpl2)
# print(tpl1*2)

# tpl1=(1,2,3,4,5)
# tpl1=list(tpl1)
# tpl1.append(100)
# print(tuple(tpl1))




# task=["ritik","diya","rohit",(1,2,[3,6],4)]     
# print(task[3][2][1])
# functions of set
# copy, deepcopy, update




# >>>>>>>>>>>>>>dict>>>>>>>>>>>>>>
# mutable
# key must be unique
# key is immutable
#no indexing and slicing

# my_dict={"name":"ritik","age":22,"address":"kolkata"}
# # print(my_dict)
# # print(type(my_dict))
# # print(len(my_dict))
# # (my_dict[4])    #not possible to access index in dict
# print(my_dict["name"])
# print(my_dict["age"])
# print(my_dict["address"])

# my_dict = {"a": 1, "b": 2}
# my_dict = dict(x=1, y=2)
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())



# my_dict.update({"mobile_number":1234567890})
# print(my_dict)

# copy_dict=my_dict.copy()
# print(copy_dict)





# >>>>>>>>>>>>>>>>>>>>set>>>>>>>>>>>>>>>>>
# doesn't allow duplicates, no index, no indexing, no slicing, mutable, unordered


# sat={1,2,3,4,5,6,6}
# # print(sat)
# # print(type(sat))
# # print(len(sat))
# # sat.add(7)
# # print(sat)
# print(sat.remove(3))  
# print(sat)

# diff, intersection, union



##########operations on set

# s={1,2,3}
# print(s)

# s.add(4)
# print(s)  #add the element

# # s.append(5)      #attribute error: set has no attribute append()
# # print(s)

# s.remove(3)
# print(s)

# s.update([3,5,6])
# print(s)

# s.discard(4)   #error if 4 not found
# print(s)
# s.discard(10)
# print(s)            #if the element is not there, then there's no error

# # s.pop(1)            #type error: takes no argument
# # print(s)

# s_new=s.pop()
# print(s_new)

# s.clear()
# print(s)




# >>>>>>> mathematical operation on set >>>>>>>>

# a={1,2,3,4}
# b={3,4,5,6}

# # >>> union >>>
# print(a.union(b))
# print(a|b)

# # >>> intersection >>>
# print(a.intersection(b))
# print(a&b)

# >>> difference >>>
# print(a.difference(b))
# print(a-b)
# print(b.difference(a))
# print(b-a)


# print(a.symmetric_difference(b))
# print(a^b)                only in or only in b


# >>>>>>>>>>>>>>> set comparison >>>>>>>>>>>
# print(a.issubset(b))              subset

# print(b.issuperset(a))              superset

# print(a.issuperset(b))               false because all elements of b is not present in a






# >>>>>>>>> copy >>>>>>>>>>

# import copy
# dict1={"a":1,"b":2,"c":[2,3]}
# dict2=dict1.copy()

# dict1["a"]=10
# dict2["b"]=0
# dict1["c"][0]=20

# print(dict1)
# print(dict2)



# >>>>>>>> deep copy >>>>>>

# import copy

# dict1={"a":1,"b":2,"c":[2,3]}
# deep=copy.deepcopy(dict1)

# deep["c"][0]=99

# print(dict1)
# print(deep)