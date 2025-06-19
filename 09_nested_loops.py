# For loop

colors = ["red", "green", "blue"] 
items = ["book", "pen", "copy"] 

for color in colors: 
    for item in items:
        print(color,item) 


# Nested while loop 

i = 0
while i < 3: 
   j = 0 
   while j < 3: 
    print(i,j) 
    j +=1 
    i +=1  

# For loop inside while loop 

i = 1 
while i < 4: 
    for j in range(3): 
        print(i, j) 
        i +=1 


# While loop inside a for loop

items = ["apple", "banana", "cherry"]

for item in items:
    count = 0
    while count < 2:
        print(item, count)
        count += 1