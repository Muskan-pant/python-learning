# if-elif-else 

light = "yellow"

if(light == "green"):
  print("go")
elif(light == "red"):
  print("stop")
elif(light == "yellow"):
  print("Yellow")
else: 
  print("Light is not working") # output :- yellow 


age = 24

if(age >= 18):
  print("eligible")
else :
  print("not eligible") #output :- eligible

  
#nested condition
age = 90

if(age >=20):
  if(age <= 80):
    print("eligible")
  else:
    print("not")   #output :- not


#Practice questions :- 

#WAP to check if a number entered by the user is odd or even.
num = int(input("Enter a number: "))
if(num %2 == 0):
  print("Even Number.")
else:
  print('Odd number.')



#WAP to find the greatest of 3 numbers entered by the user.
a = int(input("enter first number: ")) #50
b = int(input("enter second number: ")) #20
c = int(input("enter third number: ")) #300
if(a >= b and a >= c):
  print("first number is  greatest number" , a)
elif(b >= c):
  print("Second number is  greatest number" , b)
else:
    print("Third number is greatest number" , c) #output :- Third number is greatest number 300



#WAP to check if a number is a multiple of 7 or not.
x = int(input("enter a number: "))

if( x % 7 == 0):
  print("Multiple of 7")
else:
  print("not")
  