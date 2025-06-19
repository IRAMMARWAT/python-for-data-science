# Data structure 
# List 
# define a list 
food = ["apple", "banana", "cherry", "orange", "kiwi", "mango"] 

print(food[1]) 
# 2 -Tuple 

# coordinates = (10.0, 20.0) 
# print (coordinates [0]) 
# print (coordinates [1]) 


# 3- set 

food_set ={"Drinks", "snacks", "fruits", "vegetables"} 
print(food_set) 
food_set.add("meat") 
print(food_set) 

# 4_ dictionary 

car = {"brand": "ford", "model": "Mustang", "year": 1964} 
print(car) 
car["year"] = 2030 
print(car["year"]) 





cyruskhan644: make table of list tuple dictionary set in which show ordered mutable access allow duplicates explain of each data set

GitHub Copilot: Here is a table summarizing the characteristics of Python's `list`, `tuple`, `dictionary`, and `set` data structures:

| Data Structure | Ordered | Mutable | Allows Duplicates | Access Method | Explanation                                                                 |
|----------------|---------|---------|-------------------|---------------|-----------------------------------------------------------------------------|
| **List**       | Yes     | Yes     | Yes               | Index-based   | A collection of items that is ordered and changeable. Duplicates are allowed. |
| **Tuple**      | Yes     | No      | Yes               | Index-based   | Similar to a list but immutable (cannot be changed after creation).          |
| **Dictionary** | Yes     | Yes     | No (keys)         | Key-based     | A collection of key-value pairs. Keys must be unique, but values can duplicate. |
| **Set**        | No      | Yes     | No                | Unordered     | An unordered collection of unique items. Duplicates are not allowed.         |

### Explanation of Each:
1. **List**: 
   - Example: `food = ["apple", "banana", "cherry"]`
   - You can access elements using an index (e.g., `food[1]`).

2. **Tuple**:
   - Example: `coordinates = (10.0, 20.0)`
   - Immutable, meaning you cannot modify its elements after creation.

3. **Dictionary**:
   - Example: `car = {"brand": "ford", "model": "Mustang", "year": 1964}`
   - Access values using keys (e.g., `car["brand"]`).

4. **Set**:
   - Example: `food_set = {"Drinks", "snacks", "fruits"}`
   - Unordered and does not allow duplicate elements.
