#While loop :-
i = 1
while i <= 5 :
  print(i)
  i += 1


#Print numbers from 1 to 5
y = 1
while y <= 5 :
  print(y)
  y += 1

print("Done")


#print numbers from 5 to 1
i = 5
while i >= 1 :
  print(i)
  i -= 1
print("Loop ended")



#Print Hello! 5 times using while loop .
z = 1
while z <= 5 :
  print("Hello!")
  z += 1


# Break :- used to terminate the loop when encountered.
i = 1
while i <= 5:
  print(i)
  if(i == 3):
    break
  i += 1

print("end of loop") 


# Continue :- terminates execution in the current iteration & continues execution of the loop with the next iteration.

#Print odd numbers from 1 to 10.
z = 1
while z <= 10 :
  if(z%2 == 0): 
    z += 1
    continue #it skips even numbers 
  print(z)
  z += 1

#print even numbers from 1 to 10
z = 1
while z <= 10:
  if(z%2 != 0):
    z += 1
    continue #skips odd numbers 
  print(z)
  z += 1


# For Loops :- are usd=ed for sequential traversal. For traversing list, string , tuple , etc.
 #use list:
veggies = ["potato", "brijal", "ladyfinger", "cucumber"]

for val in veggies:
  print(val)

#use tuple :-
tup = (1, 2, 3, 4, 5, 6,)
for num in tup:
  print(num)


#use string :-
str = "Welcome!"

for ch in str :
  print(ch)


# For loop with else :-
str1 = "python"

for char in str1 :
  if(char == 'o'):
    print("o found")
    break
  print(char)
else: 
  print("End")



# range() :- returns a sequence of numbers, starting from 0 by default and increments by 1 (by default) and stops before a specified number. 
# range(start?,stop,step?)
seq = range(5)
for i in seq :
  print(i)

for i in range(2, 10): # range(start,stop) 
  print(i)

for i in range(2, 11, 3): #range(start,stop,step) 
  print(i)


for i in range(1, 100, 2): 
  print(i)