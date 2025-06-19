person_A_name = input("what is your name:") 
person_A_age = input("what is your age") 


person_B_name = input("what is your name:") 
person_B_age = input("what is your age") 

if person_A_age > person_B_age:
    print(person_A_name, "is older than", person_B_name) 
else:
    print(person_B_name, "is older than", person_A_name)  

     

    name = input("What is your name: ")
weight = float(input("What is your weight (in kg): "))
height = float(input("What is your height (in meters): "))

# Calculate BMI
bmi = weight / (height ** 2)

# Display the result
print(f"{name}, your BMI is {bmi:.2f}")