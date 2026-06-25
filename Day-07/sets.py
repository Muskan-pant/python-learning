#Set :- unordered , each element in the set must be unique and immutable . duplicate value ignore by set .
collection = {1, 2, 3, 4}
print(collection) 
print(type(collection)) # <class 'set'>


print(len(collection)) #total number of items.  #4

#empty set syntax :- 
empty_set = set()


#Set Method :- a.) set.add(el) :- adds an element.
info = set()
info.add(1)
info.add(3)
info.add("rahul sharma")
info.add(2)
info.add(34)
info.add((1, 2, 3))

print(info)
print(len(info)) #6


# b.) set.remove(el) :- removes the 
info.remove(2)
print(info)

# c.) set.pop() :- removes the random value
info.pop()
print(info)  #{1, 3, 34, (1, 2, 3)} 

# d.) set.clear() :- empties the set
info.clear()
print(len(info)) #0 


# e.) set.union(set2) :-  combines both set values & returns new
set1 = {1, 2, 4, 3, 3, 4, 5, 6, 2}
set2 = {2, 2, 3, 8, 9, 11}

print(set1.union(set2)) # {1, 2, 3, 4, 5, 6, 8, 9, 11}


# f.) set.intersection(set2) :- combines common value and returns new 

print(set1.intersection(set2)) #{2, 3}