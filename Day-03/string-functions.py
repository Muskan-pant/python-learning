#endswith():- Returns true if string ends with substr.EncodingWarning
str = "welcome Muskan"
print(str.endswith("an")) #True 


#capitalizee() :- capitalize 1st character. Not changes the original string . It creates another string do to their task. 
print(str.capitalize()) #Welcome muskan


#replace(old, new):- replace all occurrence of old
print(str.replace("o", "a")) #welcame Muskan 
print(str.replace("Muskan", "Priya")) #welcome Priya


#find(word) :- return 1st index of 1st occurance 
print(str.find("M")) #M index is 8
print(str.find("welcome")) #welcome 1st index is 0


#count() :- counts the occurrence(how many time) of substr
print(str.count("a")) #1 :- one time a occure in the string.
print(str.count("e")) #2 :- two time e occure in the string.
