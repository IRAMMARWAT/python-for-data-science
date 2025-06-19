# conditional statments (these are comparision operators)
# > 
# < 
# == 
# !=

here we apply conditions 
x = 0 
if x > 0: 
    print("x is positive") 
    elif x < 0: 
        print("x is negative") 
        else:
            print("x is zero") 


# for loops ( means aik chiz ko bar bar karna) 


Control flow statements in Python are used to control the execution of code based on conditions or loops. Here are the main types:

### 1. **Conditional Statements** 

   - Used to execute code based on conditions.
   - Keywords: `if`, `elif`, `else`.

```python
x = 10
if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

---

### 2. **Loops**
   - Used to repeat a block of code multiple times.

#### **For Loop** 

   - Iterates over a sequence (like a list, tuple, or string).

```python
menu = ["Pizza", "Burger", "Pasta"]
for food in menu:
    print(food)
```

#### **While Loop** 

   - Repeats as long as a condition is `True`.

**With Integers:**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**With Strings:**
```python
word = "Python"
index = 0
while index < len(word):
    print(word[index])
    index += 1
```

---

### 3. **Control Flow Modifiers** 

   - `break`: Exits the loop prematurely.
   - `continue`: Skips the current iteration and moves to the next.
   - `pass`: Does nothing; used as a placeholder.

```python
for i in range(5):
    if i == 3:
        break  # Exits the loop when i is 3
    elif i == 2:
        continue  # Skips the iteration when i is 2
    print(i)
```