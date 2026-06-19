#WAP to input user's first name & print its length.
name = input("Enter your First name: ") #Muskan
print(len(name)) #6 :- output


#WAP to find the occurrence of '$' in a string.
str = "welcome! In python journey"
print(str.count("$")) #0 :- output

str2 = "Hey! I have $9 and Reena has $25"
print(str2.count("$")) #2 :- output 


#Create a string "Python Programming" and print only the word "Programming" using slicing.
course = "Python Programming"
print(course[6 : 18])


#Take a string from the user and convert it to uppercase.
str4 = input("enter string: ") #muskan
print(str4.upper()) #MUSKAN :- output


#Take a string from the user and replace one word with another word.
text = input("Enter the sentence: ")  #hello world
old_text = input("enter the word to replace: ") #world
new_text = input("enter the new word: ") #muskan
result = text.replace(old_text , new_text)

print("The Updated result is: ", result) #hello muskan :- output