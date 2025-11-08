# 🐍 Python Fundamentals Playbook - Complete Guide & Practice

## 📚 Table of Contents
1. [Introduction & Goals](#introduction)
2. [Python Basics](#python-basics)
3. [Data Types and Variables](#data-types)
4. [Operators and Expressions](#operators)
5. [Conditional Statements](#conditionals)
6. [Loops and Iteration](#loops)
7. [Data Structures (Core)](#data-structures)
8. [Functions](#functions)
9. [Basic Problem Solving](#problem-solving)
10. [Built-in Functions & Shortcuts](#built-ins)
11. [File Handling (Basic)](#file-handling)
12. [Basic Libraries for DSA](#libraries)
13. [Logic-Building Practice](#logic-building)
14. [Practice Problems](#practice-problems)
15. [Summary & Next Steps](#summary)

---

## 🎯 Introduction & Goals {#introduction}

**Goal:** Get strong with Python fundamentals & logic to start solving DSA problems.

By the end of this guide, you should be able to:
- ✅ Write clean functions
- ✅ Solve pattern and logic problems confidently
- ✅ Manipulate lists, dicts, and strings with ease
- ✅ Be ready to start Data Structures & Algorithms (DSA)

---

## 🧠 1. Python Basics {#python-basics}

### 🔹 Concepts

**What is Python & why it's used**
- High-level, interpreted language
- Simple syntax, great for beginners
- Extensive libraries for everything

**How Python runs**
```python
# Python interpreter reads line by line
# Indentation matters (4 spaces recommended)
if True:
    print("Proper indentation")  # 4 spaces
```

**Your first program**
```python
print("Hello World")
```

**Comments**
```python
# This is a single-line comment
"""
This is a
multi-line comment
"""
```

**Input and Output**
```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello {name}, you are {age} years old!")
```

### 🔹 Practice Problems

#### Basic Input/Output
1. Print "Hello World" 
2. Print your name and age on separate lines
3. Take user's name as input and print "Hello [name]"
4. Take user's age as input and print "You are [age] years old"

#### Simple Programs  
1. Print the result of 5 + 3
2. Print the result of 10 - 4  
3. Take two numbers as input and print their sum
4. Use f-string to display: "My name is [name] and I am [age] years old"

#### Comments Practice
1. Write a program with single-line comments explaining each step
2. Add a multi-line comment at the top explaining what your program does
3. Comment out one line of code using #

---

## 📦 2. Data Types and Variables {#data-types}

### 🔹 Concepts

**Primitive Types**
```python
# Integer
age = 25
print(type(age))  # <class 'int'>

# Float
price = 99.99
print(type(price))  # <class 'float'>

# Boolean
is_student = True
print(type(is_student))  # <class 'bool'>

# String
name = "Alice"
print(type(name))  # <class 'str'>
```

**Type Conversion**
```python
# String to Integer
num_str = "123"
num_int = int(num_str)

# Integer to String
age = 25
age_str = str(age)

# Float to Integer (truncates decimal)
price = 99.99
price_int = int(price)  # 99
```

**Dynamic Typing**
```python
x = 10        # x is int
x = "hello"   # x is now str
x = 3.14      # x is now float
```

### 🔹 Practice Problems

#### Type Creation and Checking
1. Create an integer variable and print its value and type
2. Create a float variable and print its value and type  
3. Create a string variable and print its value and type
4. Create a boolean variable and print its value and type

#### Type Conversion Basics
1. Convert the string "25" to an integer and print it
2. Convert the integer 100 to a string and print it
3. Convert the string "3.14" to a float and print it
4. Convert the float 99.99 to an integer and print it (note: it truncates)

#### Input and Type Conversion
1. Take a number as string input, convert to int, and print
2. Take user's age as input, convert to int, add 10, and print result
3. Take two string numbers as input, convert both to int, and print their sum
4. Take a decimal number as input, convert to float, and print

---

## 🔁 3. Operators and Expressions {#operators}

### 🔹 Concepts

**Arithmetic Operators**
```python
a, b = 10, 3

print(a + b)   # Addition: 13
print(a - b)   # Subtraction: 7
print(a * b)   # Multiplication: 30
print(a / b)   # Division: 3.333...
print(a // b)  # Floor Division: 3
print(a % b)   # Modulus: 1
print(a ** b)  # Exponentiation: 1000
```

**Comparison Operators**
```python
x, y = 5, 10

print(x < y)   # True
print(x > y)   # False
print(x <= y)  # True
print(x >= y)  # False
print(x == y)  # False
print(x != y)  # True
```

**Logical Operators**
```python
a, b = True, False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

**Assignment Operators**
```python
x = 10
x += 5   # x = x + 5, now x is 15
x -= 3   # x = x - 3, now x is 12
x *= 2   # x = x * 2, now x is 24
x /= 4   # x = x / 4, now x is 6.0
```

**Operator Precedence** (High to Low)
1. `**` (Exponentiation)
2. `*, /, //, %` (Multiplication, Division)
3. `+, -` (Addition, Subtraction)
4. `<, >, <=, >=, ==, !=` (Comparison)
5. `not` (Logical NOT)
6. `and` (Logical AND)
7. `or` (Logical OR)

### 🔹 Practice Problems

#### Basic Arithmetic
1. Calculate and print: 15 + 25
2. Calculate and print: 50 - 20  
3. Calculate and print: 7 * 8
4. Calculate and print: 100 / 4
5. Calculate and print: 17 // 3 (floor division)
6. Calculate and print: 17 % 3 (remainder)
7. Calculate and print: 2 ** 5 (exponentiation)

#### Comparison Practice
1. Compare 10 and 20 using all comparison operators (<, >, <=, >=, ==, !=)
2. Take two numbers as input and check if first is greater than second
3. Check if a number (input from user) is equal to 100

#### Logical Operations
1. Print the result of: True and False
2. Print the result of: True or False  
3. Print the result of: not True
4. Check if a number is greater than 10 AND less than 50

#### Assignment Operators
1. Start with x = 10, use += to add 5, print result
2. Start with y = 20, use -= to subtract 8, print result
3. Start with z = 4, use *= to multiply by 3, print result

---

## 🔄 4. Conditional Statements {#conditionals}

### 🔹 Concepts

**Basic if-else**
```python
age = 18

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

**if-elif-else**
```python
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Your grade is: {grade}")
```

**Nested Conditions**
```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("Get a license first")
else:
    print("Too young to drive")
```

**Ternary Operator**
```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)
```

### 🔹 Practice Problems

#### Basic if-else
1. Take a number as input and check if it's positive or negative
2. Take a number and check if it's even or odd
3. Take user's age and check if they can vote (age >= 18)
4. Take a number and check if it's greater than 100

#### if-elif-else Practice  
1. Take a number (1-7) and print the corresponding day of week
2. Take a score (0-100) and print grade: A(90+), B(80+), C(70+), D(60+), F(below 60)
3. Take temperature and print: Hot(>30), Warm(20-30), Cold(<20)

#### Multiple Conditions
1. Check if a number is both positive AND even
2. Check if a number is either less than 10 OR greater than 100  
3. Take age and check: Child(<13), Teen(13-19), Adult(20-59), Senior(60+)

#### Nested if Practice
1. Check if a number is positive, then check if it's even or odd
2. Check if user can drive: age >= 18 AND has_license = True
3. Take marks, if >= 60 (pass), then assign grade based on marks

---

## 🔁 5. Loops and Iteration {#loops}

### 🔹 Concepts

**for loop with range()**
```python
# Basic range
for i in range(5):
    print(i)  # 0, 1, 2, 3, 4

# Range with start and stop
for i in range(2, 8):
    print(i)  # 2, 3, 4, 5, 6, 7

# Range with step
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8
```

**while loop**
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

**Loop Control**
```python
for i in range(10):
    if i == 3:
        continue  # Skip this iteration
    if i == 7:
        break     # Exit the loop
    print(i)

# pass - does nothing, placeholder
for i in range(5):
    pass  # TODO: implement later
```

**Nested Loops**
```python
for i in range(3):
    for j in range(3):
        print(f"({i}, {j})")
```

### 🔹 Practice Problems

#### Basic for loops with range()
1. Print numbers 0 to 4 using for loop
2. Print numbers 1 to 5 using for loop  
3. Print numbers 1 to 10 using for loop
4. Print even numbers from 0 to 10 using range(0, 11, 2)

#### Basic while loops
1. Print numbers 1 to 5 using while loop
2. Count down from 5 to 1 using while loop
3. Print "Hello" 3 times using while loop

#### Simple Loop Applications
1. Calculate sum of numbers 1 to 10 using a loop
2. Print multiplication table of 5 (5x1, 5x2, ... 5x10)
3. Count how many numbers from 1 to 20 are even

#### Loop Control (break, continue)
1. Print numbers 1 to 10, but skip 5 using continue
2. Print numbers 1 to 10, but stop at 7 using break
3. Print numbers 1 to 20, skip all even numbers using continue

#### Simple Patterns (using only what's learned)
1. Print 5 stars (*) in a row
2. Print 5 rows of 5 stars each (5x5 square)
3. Print numbers 1 to 5, each on a new line
4. Print your name 5 times, each on a new line

---

## 🧩 6. Data Structures (Core) {#data-structures}

### 🔹 Strings

**Basic Operations**
```python
text = "Hello World"

# Indexing (0-based)
print(text[0])    # 'H'
print(text[-1])   # 'd'

# Slicing
print(text[0:5])  # "Hello"
print(text[6:])   # "World"
print(text[::-1]) # "dlroW olleH" (reversed)
```

**String Methods**
```python
text = "  Hello World  "

print(text.upper())        # "  HELLO WORLD  "
print(text.lower())        # "  hello world  "
print(text.strip())        # "Hello World"
print(text.replace("World", "Python"))  # "  Hello Python  "

words = text.strip().split()  # ["Hello", "World"]
joined = "-".join(words)      # "Hello-World"
```

**String Traversal**
```python
text = "Python"
for char in text:
    print(char)

# With index
for i, char in enumerate(text):
    print(f"{i}: {char}")
```

### 🔹 Lists

**Basic Operations**
```python
numbers = [1, 2, 3, 4, 5]

# Indexing and Slicing
print(numbers[0])     # 1
print(numbers[-1])    # 5
print(numbers[1:4])   # [2, 3, 4]

# Updating
numbers[0] = 10
print(numbers)        # [10, 2, 3, 4, 5]
```

**List Methods**
```python
fruits = ["apple", "banana"]

# Adding elements
fruits.append("orange")           # ["apple", "banana", "orange"]
fruits.insert(1, "grape")        # ["apple", "grape", "banana", "orange"]
fruits.extend(["kiwi", "mango"])  # Add multiple elements

# Removing elements
fruits.remove("banana")  # Remove by value
popped = fruits.pop()    # Remove and return last element
del fruits[0]            # Remove by index

# Other operations
fruits.sort()            # Sort in place
fruits.reverse()         # Reverse in place
```

**List Comprehension**
```python
# Basic comprehension
squares = [x**2 for x in range(1, 6)]  # [1, 4, 9, 16, 25]

# With condition
evens = [x for x in range(1, 11) if x % 2 == 0]  # [2, 4, 6, 8, 10]

# With function
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
```

### 🔹 Tuples

**Immutable Sequences**
```python
coordinates = (3, 5)
rgb = (255, 128, 0)

# Indexing (like lists)
print(coordinates[0])  # 3

# Unpacking
x, y = coordinates
r, g, b = rgb

# Tuple methods
numbers = (1, 2, 2, 3, 2)
print(numbers.count(2))   # 3
print(numbers.index(3))   # 3
```

### 🔹 Sets

**Unique Elements**
```python
numbers = {1, 2, 3, 3, 4, 4, 5}
print(numbers)  # {1, 2, 3, 4, 5}

# Adding elements
numbers.add(6)
numbers.update([7, 8, 9])

# Set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))        # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2)) # {3, 4}
print(set1.difference(set2))   # {1, 2}
```

### 🔹 Dictionaries

**Key-Value Structure**
```python
student = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}

# Accessing values
print(student["name"])        # "Alice"
print(student.get("age"))     # 20
print(student.get("phone", "Not found"))  # "Not found"

# Adding/Updating
student["phone"] = "123-456-7890"
student.update({"city": "New York", "age": 21})

# Removing
del student["grade"]
phone = student.pop("phone")
```

**Dictionary Methods**
```python
student = {"name": "Alice", "age": 20, "city": "NYC"}

print(student.keys())    # dict_keys(['name', 'age', 'city'])
print(student.values())  # dict_values(['Alice', 20, 'NYC'])
print(student.items())   # dict_items([('name', 'Alice'), ('age', 20), ('city', 'NYC')])

# Iteration
for key in student:
    print(f"{key}: {student[key]}")

for key, value in student.items():
    print(f"{key}: {value}")
```

### 🔹 Practice Problems

#### String Basics
1. Create a string and print its first character (index 0)
2. Create a string and print its last character (index -1)
3. Print first 3 characters of a string using slicing
4. Print last 3 characters of a string using slicing
5. Reverse a string using slicing [::-1]

#### String Methods Practice
1. Convert "hello world" to uppercase
2. Convert "HELLO WORLD" to lowercase  
3. Remove spaces from "  hello world  " using strip()
4. Replace "world" with "Python" in "hello world"
5. Split "apple,banana,orange" by comma
6. Join ["hello", "world"] with a space

#### String Traversal
1. Print each character of "Python" on a new line
2. Count how many times 'a' appears in "banana"
3. Print each character with its index using enumerate()

#### List Basics  
1. Create a list [1, 2, 3, 4, 5] and print the first element
2. Create a list [1, 2, 3, 4, 5] and print the last element
3. Print elements at index 1 to 3 using slicing
4. Change the first element of a list to 10

#### List Methods Practice
1. Create a list [1, 2, 3] and append 4 to it
2. Insert 0 at the beginning of [1, 2, 3]
3. Remove element 2 from [1, 2, 3, 2, 4]
4. Sort the list [3, 1, 4, 2] 
5. Reverse the list [1, 2, 3, 4]

#### Basic List Comprehension
1. Create a list of squares: [1, 4, 9, 16, 25] using comprehension
2. Create a list of even numbers from 0 to 10 using comprehension
3. Convert ["hello", "world"] to uppercase using comprehension

#### Tuple Basics
1. Create a tuple (1, 2, 3) and print the second element
2. Unpack tuple (10, 20) into two variables
3. Count how many times 2 appears in (1, 2, 2, 3, 2)

#### Set Basics
1. Create a set {1, 2, 3, 3, 4} and print it (notice duplicates removed)
2. Add element 5 to set {1, 2, 3, 4}
3. Find common elements in {1, 2, 3} and {2, 3, 4} using intersection()

#### Dictionary Basics
1. Create a dictionary {"name": "John", "age": 25} and print the name
2. Add a new key "city" with value "NYC" to the dictionary
3. Print all keys of a dictionary
4. Print all values of a dictionary
5. Iterate through a dictionary and print key: value pairs

---

## ⚙️ 7. Functions {#functions}

### 🔹 Concepts

**Defining Functions**
```python
def greet(name):
    return f"Hello, {name}!"

# Calling the function
message = greet("Alice")
print(message)  # "Hello, Alice!"
```

**Parameters and Return Values**
```python
def add_numbers(a, b):
    return a + b

def get_info():
    return "Alice", 25, "Engineer"  # Multiple return values

result = add_numbers(5, 3)
name, age, job = get_info()
```

**Default Arguments**
```python
def power(base, exponent=2):
    return base ** exponent

print(power(5))     # 25 (5^2)
print(power(5, 3))  # 125 (5^3)
```

**Keyword Arguments**
```python
def create_profile(name, age, city="Unknown"):
    return f"{name}, {age}, from {city}"

# Different ways to call
profile1 = create_profile("Alice", 25)
profile2 = create_profile(age=30, name="Bob", city="NYC")
```

**Variable Arguments**
```python
def sum_all(*args):
    return sum(args)

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print(sum_all(1, 2, 3, 4, 5))  # 15
print_info(name="Alice", age=25, city="NYC")
```

**Variable Scope**
```python
global_var = "I'm global"

def my_function():
    local_var = "I'm local"
    global global_var
    global_var = "Modified global"
    return local_var

print(global_var)    # "I'm global"
result = my_function()
print(global_var)    # "Modified global"
```

### 🔹 Practice Problems

#### Basic Function Creation
1. Write a function that takes a name and returns "Hello [name]"
2. Write a function that takes two numbers and returns their sum
3. Write a function that takes a number and returns its square
4. Write a function that takes no parameters and returns "Python is fun!"

#### Functions with Parameters
1. Write a function that takes radius and returns area of circle
2. Write a function that takes length and width and returns area of rectangle  
3. Write a function that takes a number and checks if it's even (return True/False)
4. Write a function that takes a string and returns its length

#### Default Parameters
1. Write a function that greets a person with default name "Guest"
2. Write a function to calculate power with default exponent 2
3. Write a function to calculate area of rectangle with default width 1

#### Multiple Return Values
1. Write a function that takes two numbers and returns both sum and product
2. Write a function that takes a list and returns minimum and maximum
3. Write a function that takes a string and returns first and last character

#### Variable Scope Practice
1. Create a global variable and modify it inside a function
2. Create a function with a local variable and try to access it outside
3. Write a function that uses both global and local variables

---

## 🧮 8. Basic Problem Solving with Functions {#problem-solving}

### 🔹 Concepts

**Breaking Down Problems**
```python
def is_armstrong_number(num):
    """Check if a number is an Armstrong number"""
    digits = str(num)
    power = len(digits)
    total = sum(int(digit) ** power for digit in digits)
    return total == num

def find_armstrong_numbers(start, end):
    """Find all Armstrong numbers in a range"""
    armstrong_numbers = []
    for num in range(start, end + 1):
        if is_armstrong_number(num):
            armstrong_numbers.append(num)
    return armstrong_numbers
```

**Modular Code Design**
```python
def get_factors(num):
    """Get all factors of a number"""
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors

def is_perfect_number(num):
    """Check if a number is perfect"""
    factors = get_factors(num)
    return sum(factors[:-1]) == num  # Exclude the number itself
```

### 🔹 Practice Problems

#### Breaking Problems into Functions
1. Write separate functions to: check if even, check if positive, then combine them
2. Write a function to get factors, then another to check if number is perfect
3. Write a function to reverse a number, another to check if palindrome

#### Modular Programming
1. Create functions for basic calculator: add(), subtract(), multiply(), divide()
2. Write functions for grade system: input_score(), calculate_grade(), display_result()
3. Create functions for number analysis: is_prime(), get_factors(), is_perfect()

#### Function Reusability
1. Write a function to check if prime, then use it to find all primes up to N
2. Write a function to reverse string, use it to check if string is palindrome
3. Write a function to count digits, use it to check if number is Armstrong number

---

## 🧠 9. Built-in Functions & Shortcuts {#built-ins}

### 🔹 Concepts

**Common Built-in Functions**
```python
numbers = [3, 1, 4, 1, 5, 9, 2, 6]

print(len(numbers))      # 8
print(sum(numbers))      # 31
print(max(numbers))      # 9
print(min(numbers))      # 1
print(sorted(numbers))   # [1, 1, 2, 3, 4, 5, 6, 9]
print(list(reversed(numbers)))  # [6, 2, 9, 5, 1, 4, 1, 3]
```

**enumerate() and zip()**
```python
fruits = ["apple", "banana", "orange"]

# enumerate - get index and value
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

# zip - combine multiple iterables
colors = ["red", "yellow", "orange"]
for fruit, color in zip(fruits, colors):
    print(f"{fruit} is {color}")
```

**any() and all()**
```python
numbers = [2, 4, 6, 8]
mixed = [1, 2, 3, 4]

print(all(n % 2 == 0 for n in numbers))  # True (all even)
print(any(n % 2 == 0 for n in mixed))    # True (at least one even)
```

**map(), filter(), and lambda**
```python
numbers = [1, 2, 3, 4, 5]

# map - apply function to all elements
squares = list(map(lambda x: x**2, numbers))  # [1, 4, 9, 16, 25]

# filter - keep elements that match condition
evens = list(filter(lambda x: x % 2 == 0, numbers))  # [2, 4]

# lambda - anonymous functions
add = lambda a, b: a + b
print(add(3, 5))  # 8
```

### 🔹 Practice Problems

#### Basic Built-in Functions
1. Use len() to find length of list [1, 2, 3, 4, 5]
2. Use sum() to add all numbers in [1, 2, 3, 4, 5] 
3. Use max() to find largest number in [3, 7, 2, 9, 1]
4. Use min() to find smallest number in [3, 7, 2, 9, 1]
5. Use sorted() to sort [3, 1, 4, 2] without changing original

#### enumerate() Practice
1. Print each element of ["apple", "banana", "orange"] with its index
2. Use enumerate to find the index of "banana" in the list
3. Create a numbered list from ["red", "green", "blue"]

#### zip() Practice  
1. Combine ["John", "Jane", "Bob"] and [25, 30, 35] using zip()
2. Create pairs from [1, 2, 3] and ["a", "b", "c"]
3. Use zip() to create a dictionary from two lists

#### any() and all() Practice
1. Check if any number in [1, 3, 5, 7] is even using any()
2. Check if all numbers in [2, 4, 6, 8] are even using all()
3. Check if any string in ["apple", "banana"] starts with "a"

#### Basic map() and filter()
1. Use map() to square all numbers in [1, 2, 3, 4]
2. Use filter() to get only even numbers from [1, 2, 3, 4, 5, 6]
3. Use map() to convert ["1", "2", "3"] to integers

#### Simple lambda
1. Create a lambda function to add two numbers
2. Use lambda with map() to double all numbers in a list
3. Use lambda with filter() to get numbers greater than 5

---

## 📄 10. File Handling (Basic) {#file-handling}

### 🔹 Concepts

**Reading Files**
```python
# Reading entire file
with open("data.txt", "r") as file:
    content = file.read()
    print(content)

# Reading line by line
with open("data.txt", "r") as file:
    for line in file:
        print(line.strip())  # strip() removes newline

# Reading all lines into a list
with open("data.txt", "r") as file:
    lines = file.readlines()
```

**Writing Files**
```python
# Writing to a file (overwrites existing)
with open("output.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("This is line 2\n")

# Appending to a file
with open("output.txt", "a") as file:
    file.write("This is appended\n")

# Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as file:
    file.writelines(lines)
```

### 🔹 Practice Problems

#### Basic File Reading
1. Create a text file with your name and read it using open()
2. Read a file line by line using a for loop
3. Read all lines of a file into a list using readlines()

#### Basic File Writing
1. Write "Hello World" to a new file
2. Write multiple lines to a file using writelines()
3. Append your name to an existing file

#### Simple File Processing
1. Create a file with numbers (one per line) and calculate their sum
2. Count the number of lines in a text file
3. Copy content from one file to another file

---

## 🧰 11. Basic Libraries for DSA {#libraries}

### 🔹 math Module

```python
import math

# Common functions
print(math.factorial(5))    # 120
print(math.sqrt(16))        # 4.0
print(math.gcd(48, 18))     # 6
print(math.ceil(4.3))       # 5
print(math.floor(4.7))      # 4

# Constants
print(math.pi)              # 3.141592653589793
print(math.e)               # 2.718281828459045
```

### 🔹 random Module

```python
import random

# Random integers
print(random.randint(1, 10))        # Random int between 1 and 10
print(random.choice([1, 2, 3, 4]))  # Random choice from list

# Random floats
print(random.random())              # Random float between 0 and 1
print(random.uniform(1, 10))        # Random float between 1 and 10

# Shuffling
numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(numbers)                      # Shuffled list
```

### 🔹 collections Module

```python
from collections import Counter, defaultdict, deque

# Counter - count elements
text = "hello world"
counter = Counter(text)
print(counter)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})

# defaultdict - dict with default values
dd = defaultdict(list)
dd['fruits'].append('apple')
print(dd)  # defaultdict(<class 'list'>, {'fruits': ['apple']})

# deque - double-ended queue
dq = deque([1, 2, 3])
dq.appendleft(0)    # Add to left
dq.append(4)        # Add to right
print(dq)           # deque([0, 1, 2, 3, 4])
```

### 🔹 itertools Module

```python
import itertools

# Combinations and permutations
items = ['A', 'B', 'C']
print(list(itertools.combinations(items, 2)))     # [('A', 'B'), ('A', 'C'), ('B', 'C')]
print(list(itertools.permutations(items, 2)))     # [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# Product (Cartesian product)
colors = ['red', 'blue']
sizes = ['S', 'M', 'L']
print(list(itertools.product(colors, sizes)))     # [('red', 'S'), ('red', 'M'), ('red', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]
```

### 🔹 Practice Problems

#### math Module Practice
1. Use math.sqrt() to find square root of 16
2. Use math.factorial() to find factorial of 5
3. Use math.ceil() and math.floor() on 4.7
4. Calculate area of circle using math.pi

#### random Module Practice
1. Generate a random integer between 1 and 10
2. Choose a random element from ["red", "green", "blue"]
3. Shuffle a list [1, 2, 3, 4, 5] randomly
4. Generate 5 random numbers and find their average

#### Counter Practice
1. Count letters in "hello world" using Counter
2. Find the most common letter in a string
3. Count words in "the quick brown fox jumps over the lazy dog"

#### defaultdict Practice
1. Create a defaultdict(list) and add items to different keys
2. Group students by their grades using defaultdict
3. Create a word-to-index mapping using defaultdict(list)

---

## 🚀 12. Logic-Building Practice Stage {#logic-building}

### 🔹 Focus Areas

#### Pattern Problems (Nested Loops)
```python
def print_pyramid(n):
    for i in range(1, n + 1):
        # Print spaces
        for j in range(n - i):
            print(" ", end="")
        # Print stars
        for k in range(2 * i - 1):
            print("*", end="")
        print()  # New line

print_pyramid(5)
```

#### Number Problems
```python
def find_factors(n):
    factors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return sorted(factors)

def is_divisible_by_all(num, divisors):
    return all(num % d == 0 for d in divisors)
```

#### Array Problems
```python
def find_min_max(arr):
    if not arr:
        return None, None
    
    min_val = max_val = arr[0]
    for num in arr[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    
    return min_val, max_val

def calculate_sum_without_builtin(arr):
    total = 0
    for num in arr:
        total += num
    return total
```

#### String Problems
```python
def is_palindrome(s):
    s = s.lower().replace(" ", "")
    return s == s[::-1]

def reverse_words(sentence):
    words = sentence.split()
    return " ".join(word[::-1] for word in words)

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
```

#### Dictionary Problems
```python
def word_frequency(text):
    words = text.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

def merge_dictionaries(dict1, dict2):
    merged = dict1.copy()
    for key, value in dict2.items():
        if key in merged:
            merged[key] += value  # Or handle conflict differently
        else:
            merged[key] = value
    return merged
```

### 🔹 Practice Problems

#### Simple Patterns (Only nested loops)
1. Print a 3x3 square of stars
2. Print a right triangle: 
   ```
   *
   **  
   ***
   ```
3. Print numbers in rows:
   ```
   1
   12
   123
   ```

#### Basic Number Problems (Using only basic concepts)
1. Check if a number is even or odd
2. Count the digits in a number  
3. Find sum of digits in a number
4. Reverse a number using loops

#### Simple Array/List Problems
1. Find the largest number in a list without using max()
2. Count how many even numbers are in a list
3. Find the sum of all numbers in a list without using sum()
4. Check if a number exists in a list

#### Basic String Problems  
1. Count vowels (a, e, i, o, u) in a string
2. Reverse a string using loops
3. Check if a string reads the same forwards and backwards
4. Count how many words are in a sentence (split by spaces)

#### Simple Dictionary Problems
1. Create a dictionary to store student names and their grades
2. Count how many times each letter appears in a word
3. Find the student with the highest grade from a dictionary
4. Add new students to an existing grade dictionary

---

## 🧩 Practice Problems {#practice-problems}

### 🟢 Week 1: Basics & Variables

#### Day 1-2: Python Basics
1. **Hello Program**: Print "Hello, Python!"
2. **Personal Info**: Print your name, age, and favorite color on separate lines
3. **Simple Math**: Calculate and print 25 + 17, 50 - 23, 6 * 7
4. **User Input**: Ask for user's name and greet them

#### Day 3-4: Data Types & Variables
5. **Type Explorer**: Create variables of each type (int, float, str, bool) and print their types
6. **Number Converter**: Convert string "42" to integer, then back to string
7. **Calculator v1**: Take two numbers as input, convert to int, and print their sum
8. **Age Calculator**: Ask birth year, calculate and print current age

### 🟡 Week 2: Operators & Conditionals

#### Day 1-2: Operators  
9. **Math Practice**: Use all arithmetic operators on 20 and 3
10. **Comparison Test**: Compare two numbers using all comparison operators
11. **Logic Gates**: Practice True/False with and, or, not
12. **Assignment Ops**: Start with x=10, use +=, -=, *=, /= and print each step

#### Day 3-4: Conditionals
13. **Number Checker**: Check if a number is positive, negative, or zero
14. **Grade System**: Score to grade conversion (A: 90+, B: 80+, C: 70+, etc.)
15. **Age Category**: Classify as Child(<13), Teen(13-19), Adult(20-59), Senior(60+)
16. **Login System**: Check username and password (simple hardcoded values)

### 🟡 Week 3: Loops & Patterns

#### Day 1-2: Basic Loops
17. **Count to 10**: Print numbers 1 to 10 using for loop
18. **Even Numbers**: Print even numbers from 2 to 20
19. **Countdown**: Count down from 10 to 1 using while loop
20. **Sum Calculator**: Find sum of numbers 1 to 100

#### Day 3-4: Simple Patterns
21. **Star Square**: Print 5x5 square of stars
22. **Number Triangle**: Print 1, 12, 123, 1234, 12345
23. **Multiplication Table**: Print table for any number (user input)
24. **Skip and Stop**: Print 1-20, skip multiples of 3, stop at first multiple of 7 after 10

### 🟡 Week 4: Data Structures

#### Day 1-2: Strings & Lists
25. **String Manipulator**: Take a sentence, print uppercase, lowercase, word count
26. **List Basics**: Create list [1,2,3], add 4, insert 0 at start, remove 2
27. **Name List**: Take 5 names, sort them, print in alphabetical order
28. **Word Reverser**: Reverse each word in a sentence (but not sentence order)

#### Day 3-4: Dictionaries & Sets
29. **Phone Book**: Create dictionary with names and phone numbers, add/search entries
30. **Letter Counter**: Count frequency of each letter in a word
31. **Unique Finder**: Remove duplicates from a list using sets
32. **Student Grades**: Store student names and grades, find highest scorer

### 🔴 Week 5: Functions & Problem Solving

#### Day 1-2: Basic Functions
33. **Function Basics**: Write functions for add, subtract, multiply, divide
34. **Area Calculator**: Functions for area of circle, rectangle, triangle
35. **Text Processor**: Functions to count vowels, count words, reverse text
36. **Number Analyzer**: Functions to check even/odd, positive/negative, prime

#### Day 3-4: Applied Problem Solving
37. **Password Checker**: Function to validate password (length, has digit, has uppercase)
38. **List Processor**: Functions to find max, min, average without using built-ins
39. **Pattern Generator**: Function that takes height and prints triangle pattern
40. **Simple Game**: Number guessing game with functions for game logic

### 🔴 Week 6: Integration & Real Applications

#### Day 1-2: File Handling & Libraries
41. **File Manager**: Read names from file, sort them, write to new file
42. **Random Generator**: Generate 10 random numbers, find their statistics
43. **Math Helper**: Use math module to solve geometry problems
44. **Data Collector**: Use Counter to analyze text file word frequency

#### Day 3-4: Mini Projects
45. **Grade Book System**: Store, calculate, and display student grades
46. **Simple Calculator**: Menu-driven calculator with all operations
47. **Text Analyzer**: Count sentences, words, characters in a text file
48. **Inventory Tracker**: Add/remove items, track quantities and values

### 🏆 Bonus Challenges (After Week 6)

#### Logic Masters
49. **Prime Generator**: Find all prime numbers up to N using functions
50. **Palindrome Everything**: Check if numbers and strings are palindromes
51. **Pattern Master**: Create complex patterns using nested loops
52. **Algorithm Simulator**: Implement simple sorting (bubble sort) step by step

### ✅ Success Checklist

Before moving to DSA, ensure you can solve these without help:
- [ ] Write a function to check if a number is prime
- [ ] Count word frequency in a text using dictionary
- [ ] Create any pattern using nested loops  
- [ ] Read/write files and process the data
- [ ] Use built-in functions (map, filter, enumerate, zip)
- [ ] Handle user input and validate it properly

---

## 🎯 Summary & Next Steps {#summary}

### ✅ By Completing This Guide, You Can:

**Core Python Skills**
- Write clean, readable Python code
- Use all basic data types effectively
- Create and use functions with confidence
- Handle files and basic I/O operations

**Problem-Solving Abilities**
- Break down complex problems into smaller parts
- Use appropriate data structures for different scenarios
- Implement algorithms using loops and conditionals
- Debug and test your code effectively

**DSA Readiness**
- Understand time and space complexity basics
- Manipulate arrays, strings, and dictionaries efficiently
- Use built-in functions and libraries appropriately
- Think algorithmically about problem solutions

### 🚀 Next Steps: Ready for DSA!

**You're Now Ready For:**
1. **Arrays & Strings** - Advanced manipulation and algorithms
2. **Linked Lists** - Understanding pointer-based data structures
3. **Stacks & Queues** - LIFO and FIFO data structures
4. **Recursion** - Thinking recursively about problems
5. **Sorting & Searching** - Fundamental algorithms
6. **Trees & Graphs** - Complex data structures
7. **Dynamic Programming** - Optimization techniques

### 📚 Recommended Learning Path

**Week 1-2**: Master basics (Variables, conditionals, loops)
**Week 3-4**: Focus on functions and data structures
**Week 5-6**: Practice problem-solving and libraries
**Week 7+**: Start DSA with Arrays and basic algorithms

### 🎯 Success Metrics

Before moving to DSA, ensure you can:
- [ ] Write a function to solve any basic programming problem
- [ ] Manipulate lists, dictionaries, and strings confidently
- [ ] Understand when to use different data structures
- [ ] Debug your code and handle edge cases
- [ ] Read and write files for input/output
- [ ] Use Python's built-in functions effectively

---

> 🎯 **Remember:** The goal is not just to learn syntax, but to think like a programmer. Practice regularly, solve problems daily, and don't be afraid to experiment with code!

**Happy coding! 🐍🚀**