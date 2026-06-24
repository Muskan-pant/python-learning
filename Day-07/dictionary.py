# Dictionary are used to store data values in key:value pairs.They are unordered , mutable & don't follow duplicate keys.
info = {
  "name" : "Mini",
  "age" : 20 ,
  "is_pass" : True,
  "marks" : 98.9
}

print(type(info))
print(info) #{'name': 'Mini', 'age': 20, 'is_pass': True, 'marks': 98.9}

print(info["name"]) #Mini
print(info["marks"]) #98.9

info["name"] = "Riya" #can change value 
info["surname"] = "Sharma" #can add new key

print(info)   # {'name': 'Riya', 'age': 20, 'is_pass': True, 'marks': 98.9, 'surname': 'Sharma'}


#can create empty dictionary 
empty_dict = {}
print(empty_dict) #{}

#can add data in empty dictionary 
empty_dict["CGPA"] = 8.0
empty_dict["name"] = "Ginny"
print(empty_dict) #{'CGPA': 8.0, 'name': 'Ginny'}


#Nested Dictionary :- 
student = {
  "name" : "Rahul",
  "age" : 20,
  "subjects" : {  #Nested dictionary 
    "phy" : 89,
    "maths" : 93,
    "bio" : 85
  }
}

print(student)  #{'name': 'Rahul', 'age': 20, 'subjects': {'phy': 89, 'maths': 93, 'bio': 85}}

print(student["subjects"]) #{'phy': 89, 'maths': 93, 'bio': 85}
print(student["subjects"]["bio"]) #85
print(student["age"]) #20


#Dictionary Methods :-   
data = {
  "name" : "ravi",
  "age" : 23,
  "sub" : {
    "maths" : 89,
    "sci" : 78,
    "eng" : 98
        } , 
  "class" : "BCA"
}

# a.) myDict.keys() :- returns all keys
print(data.keys()) #dict_keys(['name', 'age', 'sub', 'class']) Note* nested keys are not print. eg :- eng , sci , maths 


#dict_keys print output in list and tuple  & we can convert in list only as well as tuple only using typecasting .

print(list(data.keys()))  #['name', 'age', 'sub', 'class']  Dictionary output comes in list formate only.

print(tuple(data.keys())) #('name', 'age', 'sub', 'class') 


#can print total number of keys of the dictionary :- 
print(len(data)) #4



# b.) myDict.values() :- returns all values

print(data.values()) #dict_values(['ravi', 23, {'maths': 89, 'sci': 78, 'eng': 98}, 'BCA'])

#can convert it in list & tuple 
print(list(data.values())) #['ravi', 23, {'maths': 89, 'sci': 78, 'eng': 98}, 'BCA']

#can find length of 
print(len(list(data.values()))) #4




# c.) myDict.items() :- returns all (key,val) pairs as  tuples

print(data.items()) #dict_items([('name', 'ravi'), ('age', 23), ('sub', {'maths': 89, 'sci': 78, 'eng': 98}), ('class', 'BCA')])

#can typecast :-
print(list(data.items())) #[('name', 'ravi'), ('age', 23), ('sub', {'maths': 89, 'sci': 78, 'eng': 98}), ('class', 'BCA')]

#can access individual pairs 
pairs = list(data.items())
print(pairs[0]) #('name', 'ravi')
print(pairs[3]) #('class', 'BCA')


# d.) myDict.get(keys) :- returns the keys according to value 

print(data.get("name")) #ravi


# e.) myDict.update(newDict) :- inserts the specified items to the dictionary (can insert new key-value or update previous key-value)

data.update({ "city" : "delhi"}) 
print(data) # {'name': 'ravi', 'age': 23, 'sub': {'maths': 89, 'sci': 78, 'eng': 98}, 'class': 'BCA', 'city': 'delhi'}