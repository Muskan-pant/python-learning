#WAP to ask the user to enter names of their 3 favorite movies and store them in a list.
movies = []
mov = input("Enter first movie: ")
movies.append(mov)
mov = input("Enter second movie: ")
movies.append(mov)
mov = input("Enter Third movie: ")
movies.append(mov)

print(movies)


#WAP to check if a list contains a palindrome of elements.
list1 = [1, 2 , 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
  print("Palindrome")
else:
  print("Not Palindrome") #Palindrome


#Another Example :- 
name = ["m" , "a" ,"a" ,"m", "p"]  

name_copy = name.copy()
name_copy.reverse()

if(name_copy == name):
  print("Palindrome")
else:
  print("Not Palindrome") #Not Palindrome


#WAP to count the number of students with the "A" grade in the following Tuple.
grade = ("C", "D", "A", "A", "B", "B", "A")
print(grade.count("A")) #3


#Store the above values in a list & sort them from "A" to "D".
grades = ["C", "D", "A", "A", "B", "B", "A"]
grades.sort()
print(grades) #['A', 'A', 'A', 'B', 'B', 'C', 'D']


#Create a list of 10 numbers. Write a program to find the largest, smallest, and sum of all elements.
num = [23, 22, 90, 100, 109, 200, 45, 76, 89, 55]
largest = max(num)
smallest = min(num)
total = sum(num)

print("Largest number: ", largest) #200
print("Smallest number: ", smallest) #22
print("Sum of All elements: ", total) #809


#Given a list: fruits = ["apple", "banana", "apple", "orange", "banana", "apple"] . Find how many times each fruit appears in the list.
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]
 
print(fruits.count("apple")) #3
print(fruits.count("banana")) #2
print(fruits.count("orange")) #1


#Create a list: colors = ["red", "blue", "green"] Add "yellow" to the list and print it.
colors = ["red", "blue", "green"]
colors.append("Yellow")
print(colors)

#Create a list: nums = [10, 20, 30, 40] Change 20 to 25.
nums = [10, 20, 30, 40]
nums[1] = 25
print(nums)


#Create a list of 5 names and remove one name.
names = ["Muskan", "Kanika", "Lalit", "Karan", "Anu"]
names.remove("Anu")
print(names)


#create tuple containing 5 cities & print it .
cities = ("delhi", "jalandhar", "mumbai","pune", "ludhiana")
print(cities)


#Create a tuple: marks = (80, 75, 90, 85) . Print the first and last marks.
marks = (80, 75, 90, 85)
print(marks[0]) #80
print(marks[-1]) #85 
#-1  use negative index because it works even if the tuple size changes.



#Create a tuple and print the element at index 2.
tup1 = (12, 45, 21, 56, 67)
print(tup1[2]) #21 