#list are mutable :- you can change it .

marks = [12, 23, 45,33,56]
print(marks)
print(type(marks)) #list
print(len(marks)) #5
print(marks[3]) #33


#multiple type data can store in single list .
student = ["Karan", 20 , "Computer Application", 8.5]
print(student)
print(student[0])
student[0] = "Arjun" #can update the value of element that are stored in list.
print(student)


#List Slicing :- 
scores = [45, 67, 34, 89, 56]
print(scores[1:4]) #[67,34,89]

#negative-index based slicing :-
print(scores[-3:-1]) #[34,89]


#List Methods:-
#append() :- add one elements at the end.

list = [2, 6, 8, 3 ]
list.append(5)
print(list) #[2,6,8,3,5]


#sort() :- sorts in ascending order.
list.sort()
print(list) #[2, 3, 5, 6, 8]

#sort(reverse=True) :- sorts in decending order
list.sort(reverse=True)
print(list) #[8, 6, 5, 3, 2]


#reverse() :- reverse list
list.reverse()
print(list) 


#inser(idx,el) :- insert element at particular index
num = [1,3,56,8]
num.insert(3,97)  #3 is index and 97 is element value 
print(num) #output :- [1, 3, 56, 97, 8]


#remove() :- removes first occurrence of element
num.remove(56)
print(num) #[1, 3, 97, 8]


#pop(idx) :- removes particular element at idx.

num.pop(3) #3 index element remove
print(num) #[1, 3, 97]