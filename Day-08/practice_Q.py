#Store following word meanings in a python dictionary:- table: "a piece of furniture" , "Lists of Facts & Figures"
# cat : "a small animal"

dictionary = {
  "cat" : "a small animal",
  "table" : ["a piece of furniture", "Lists of Facts & Figures"]
}

print(dictionary)


# You are given a list of subjects for students . Assume one classroom is required for 1 subject. how many classrooms are needed by all subjects.  "python" , "java" , "c++", "python" , "javascript" , "java", "python", "java", "c++", "c"

subjects = {
  "python" , "java" , "c++", "python" , "javascript" , "java", "python", "java", "c++", "c"
}

print(subjects) #{'c', 'python', 'javascript', 'c++', 'java'}
print(len(subjects)) #5


#WAP to enter marks of 3 students from the users and store them in a dictionary.Start with an empty dictionary & add one by one .Use subject name as key & marks as value.

marks = {}

x =int(input("Enter phy: "))
marks.update({"phy" : x})

y = int(input("Enter maths: "))
marks.update({"maths" : y})

z = int(input("Enter eng: "))
marks.update({"eng" : z})

print(marks) #{'phy': 90, 'maths': 89, 'eng': 99}


#Figure out the way to store 9 & 9.0 as separate values in the set. 
#sol 1 :- 
values = { 9, '9.0'}
print(values) #{9, '9.0'} 
#use string methods 

#sol 2 :- 
val = {
  ("int" , 9),
  ("float" , 9.0)
}

print(val) #{('int', 9), ('float', 9.0)} 
#use built-in data-types way.

