# A Function is a block of code which only runs when it is called. 
# You can pass data, known as parameters, into a function. A function can return data as a resulr.
# in python, a function is defined usuing the def keyword 


# Lets define a function 
def greet_user():
    print("Hello, user!") 
    greet_user() 

    def aoa (): 
        print("Asalamo alaikum , All the way from london") 

# aoa() 

def aoa(name): 
    print(f"Asala o alaikum, {name}!, kaifa Haluk "?) 
    aoa("cyrus") 

    # Return values 

    def square(num):
    return num * num

result = square(4)
print(result)  # Output: 16 

# Multipl ereturns values  

def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(x, y)  # Output: 10 20 

# No return values 

def greet():
    print("Hello!")

result = greet()
print(result)  # Output: None 


# Recursion 

def factorial(n):
    # Base case: stop recursion when n is 0 or 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: call the function itself
        return n * factorial(n - 1)

# Test the recursive function
result = factorial(5)
print(result)  # Output: 120 

# Lambda function

# A lambda function is a small anonymous function.
# It can have any number of arguments, but only one expression.

# Example of a lambda function to add 10 to a number
add_ten = lambda x: x + 10
print(add_ten(5))  # Output: 15

# Example of a lambda function to multiply two numbers
multiply = lambda x, y: x * y
print(multiply(3, 4))  # Output: 12

# Example of using a lambda function with the `map` function
numbers = [1, 2, 3, 4]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16]
