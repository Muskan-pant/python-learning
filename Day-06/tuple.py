#Tuple :- immutable sequence of value. use () to create tuple.
tup = (1, 23, 54, 78)
print(type(tup))
print(tup[0]) #1 
print(tup[3]) #78

#use single value separate with comma. 
tup1 =(1,)
print(tup1)


#Slicing 
print(tup[1:3]) #(23,54)


#Tuple Methods :- a.) index(el) :- returns index of first occurrence.
tup3 = (34, 66, 98, 100, 23, 34)
print(tup3.index(98)) #2 
print(tup3.index(66)) #1 


# b.) count(el) :- counts total occurrence.
print(tup3.count(100)) #1
print(tup3.count(34))   #2 


