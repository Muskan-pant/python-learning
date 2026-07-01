# 1. Print numbers from 1 to 100.
num = 1
while(num <= 100):
  print(num)
  num += 1   

print('end of loop')     
# 2. Print numbers from 100 to 1.
num = 100

while(num >= 1):
  print(num)
  num -= 1


# 3. Print the multiplication table of a number n.
mul_table = 5
i = 1
while(i <= 10):
  print(mul_table , "x" , i , "=", mul_table*i )
  i += 1


# 4. Print the elements of following list using a loop: [1,4,9,16,25,36,29,68,81,100]
nums = [1,4,9,16,25,36,29,68,81,100]
idx = 0
while(idx < len(nums)):
  print(nums[idx])
  idx += 1
      

# 5. Search for a number x in this tuple using loop: (1,4,9,16,25,36,29,68,81,100)
tup = (1,4,9,16,25,36,29,68,81,100)
x = 25
idx = 0

while(idx < len(tup)):
  if(tup[idx] == x):
    print("Found at index", idx) #4
  idx += 1


# Using for loop :- print the elements of following list using a loop [1,4,9,16,25,36,29,68,81,100]

nums = [1,4,9,16,25,36,29,68,81,100]

for el in nums:
  print(el)

#Search for a number x in this tuple using loop : (1,4,9,68, 16,25,36,29,68,81,100, 68)
tup = (1,4,9,68,16,25,36,29,68,81,100, 68)
x = 68
i = 0

for el in tup : 
 if(el == x):
  print("num found at index",i)
 i += 1
 #output : num found at index 3
 #num found at index 8
 #num found at index 11 


# using for and range():
# q1. print numbers from 1 to 100.
for i in range(1, 101):
  print(i)

print("finish")

#q2. print numbers from 100 to 1.
for y in range(100, 0, -1):
  print(y)

print("end of the loop")






 