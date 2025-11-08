# 🧩 Python Data Types Playbook - Complete Guide & Practice

## 📚 Table of Contents
1. What Are Data Types?
2. Why Data Types Matter
3. Categories of Python Data Types
4. Numeric Types (int, float, bool, complex)
5. Sequence Types (str, list, tuple, range)
6. Set Types (set, frozenset)
7. Mapping Type (dict)
8. Special Type (NoneType)
9. Mutable vs Immutable
10. DSA Connection Summary
11. Common Beginner Mistakes
12. Learning Path & Mini Project
13. Practice Questions (Beginner → DSA)

---

## 🪄 1. What Are Data Types?
A data type tells Python what kind of data it is and what you can do with it. Think of it as a container: a box for numbers, a box for text, a bag for many items.

---

## 🧠 2. Why Data Types Matter
Before algorithms or data structures, you must know:
- How data is stored
- What operations you can perform
- How data behaves when changed or copied

Example:
```python
a = 5        # number
b = "5"      # text
```
`a` and `b` look the same, but one is a number you can add, the other is text you can print.

---

## ⚙️ 3. Categories of Python Data Types
| Category   | Examples                  | Mutable? | Description                  |
|------------|---------------------------|----------|------------------------------|
| Numeric    | int, float, complex, bool | ❌       | Numbers                      |
| Sequence   | str, list, tuple, range   | list ✅   | Ordered data                 |
| Set        | set, frozenset            | set ✅    | Unordered, unique elements   |
| Mapping    | dict                      | ✅        | Key–value pairs              |
| Special    | NoneType                  | N/A      | Represents “nothing”         |

---

## 🔢 4. Numeric Types
### 4.1 Integers (int)
Whole numbers, no decimals.
```python
age = 21
print(age + 5)  # 26
```
### 4.2 Floating Point (float)
Numbers with decimals.
```python
pi = 3.14
print(pi * 2)  # 6.28
```
### 4.3 Boolean (bool)
True or False values.
```python
is_sunny = True
if is_sunny:
    print("Let's go outside!")
```
### 4.4 Complex (complex)
Numbers with real and imaginary part (rare in DSA).
```python
z = 2 + 3j
print(z.real, z.imag)  # 2 3
```

---

## 🧵 5. Sequence Types
### 5.1 String (str)
Sequence of characters (text). Immutable.
```python
name = "Alice"
print(name[0])      # 'A'
print(name[::-1])   # 'ecilA'
```
### 5.2 List (list)
Ordered, mutable collection.
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("grape")
fruits[1] = "mango"
```
### 5.3 Tuple (tuple)
Like a list, but immutable.
```python
coordinates = (10, 20)
```
### 5.4 Range (range)
Represents a sequence of numbers.
```python
for i in range(5):
    print(i)  # 0 1 2 3 4
```

---

## 🧺 6. Set Types
### 6.1 Set (set)
Unordered collection of unique items.
```python
numbers = {1, 2, 3, 3}
print(numbers)  # {1, 2, 3}
numbers.add(4)
```
### 6.2 Frozen Set (frozenset)
Like a set, but immutable.
```python
f = frozenset({1,2,3})
```

---

## 🗺️ 7. Mapping Type (dict)
Stores data as key–value pairs.
```python
student = {"name": "Alice", "age": 21, "marks": 95}
print(student["age"])
student["grade"] = "A"
del student["marks"]
```

---

## ⚫ 8. Special Type (NoneType)
Represents nothing or no value.
```python
x = None
print(x)  # None
```

---

## 🧩 9. Mutable vs Immutable
| Type                | Mutable? | Example                |
|---------------------|----------|------------------------|
| int, float, str, tuple, frozenset | ❌ | Can't change after creation |
| list, set, dict     | ✅        | Can modify contents     |

---

## 🧮 10. DSA Connection Summary
| Data Type | Used For         | DSA Analogy           |
|-----------|------------------|-----------------------|
| int       | Counting, indexes| Basic unit            |
| float     | Measurements     | Rare                  |
| bool      | Conditions       | Flags                 |
| str       | Text, tokens     | String problems       |
| list      | Dynamic storage  | Arrays, stacks, queues|
| tuple     | Fixed data       | Coordinates, constants|
| set       | Unique collection| Hash set              |
| dict      | Key-value mapping| Hash map              |
| None      | Placeholder      | Null pointer          |

---

## ⚠️ 11. Common Beginner Mistakes
- Confusing "5" (string) with 5 (int)
- Forgetting lists inside lists are linked by reference
- Using mutable objects as dictionary keys
- Modifying lists while looping over them
- Expecting precise decimals with float

---

## 🧭 12. Learning Path & Mini Project
**Stage 1:** Print and manipulate simple variables (age, name, etc.)
**Stage 2:** Use lists, tuples, sets (e.g., shopping list app)
**Stage 3:** Use dictionaries (student record manager)
**Stage 4:** Combine them (phonebook: dict of lists)
**Stage 5:** DSA prep (implement stack/queue using lists)

**Mini Project Example:**
```python
students = [
    {"name": "Alice", "marks": [85, 90, 92]},
    {"name": "Bob", "marks": [70, 80, 65]}
]
for s in students:
    avg = sum(s["marks"]) / len(s["marks"])
    print(f"{s['name']} -> Average: {avg}")
```


## 🧠 13. Practice Questions (Beginner → DSA Readiness)

### FOUNDATIONS — IDENTIFY & DIFFERENTIATE

- What data type will Python assign to each of these?

  ```python
    a = 5  
    b = 3.14  
    c = "3.14"  
    d = True  
    e = None  
    f = (1, 2, 3)  
    g = {1, 2, 2, 3}  
    h = {"x": 1, "y": 2}
  ```

- What’s the difference between 5, "5", and 5.0?
- What will type(5 == 5.0) return?
- Predict the output:
  ```python
    print(1 + True)
    print("hi" * 3)
    print(3 / 2)
    print(3 // 2)
    print(3 % 2)
  ```
- Which of these are immutable: list, tuple, str, dict, set?

### NUMERIC TYPES — OPERATIONS & PITFALLS
- Compute mentally:
  ```python
    print(10 // 3)
    print(10 / 3)
    print(10 % 3)
    print(2 ** 5)
  ```
- Why might 0.1 + 0.2 != 0.3?
- What’s the difference between // and /?
- Convert float → int → string → back to float:
  ```python
    x = 3.75
    y = int(x)
    z = str(y)
    w = float(z)
    print(w)
  ```
- What will this print?
  ```python
    print(int(True), int(False))
    print(bool(0), bool(1), bool("hello"), bool(""))
  ```

### STRING OPERATIONS — SLICING & IMMUTABILITY
- Predict output:
  ```python
    name = "Python"
    print(name[0])
    print(name[-1])
    print(name[1:4])
    print(name[::-1])
  ```
- Try modifying a string directly:
  ```python
    s = "data"
    s[0] = "D"
  ```
- Combine and repeat:
  ```python
    s1 = "AI"
    s2 = "ML"
    print(s1 + s2)
    print(s1 * 3)
  ```
- Convert "python" → "Python" without using capitalize().
- How would you count letters in "abracadabra"?

### LISTS — MUTABLE, MULTI-TYPE CONTAINERS
- Create a list of 5 fruits.
- Add “grape” at the end.
- Replace the 2nd element with “mango”.
- Remove the last element.
- What happens here?
  ```python
    a = [1, 2, 3]
    b = a
    b.append(4)
    print(a)
  ```
- How do you clone a list without linking memory?
- What is len([]) ?
- Predict output:
  ```python
    nums = [1, 2, 3]
    print(nums[1:])
    print(nums[::-1])
  ```
- Mix data types: [1, "hi", 3.14, True] — valid or invalid?

### TUPLES — IMMUTABLE SEQUENCES
- Create a tuple of coordinates (x, y, z).
- Try changing one element. What happens?
- How to convert (1, 2, 3) → [1, 2, 3] and back?
- Can a tuple contain a list? If yes, can you modify that list?

### RANGE — SEQUENCES ON DEMAND
- What does list(range(5)) produce?
- What about list(range(2, 10, 2))?
- Why is range() memory-efficient compared to lists?
- Write a loop that prints numbers 10 → 1 using range().

### SETS — UNIQUE, UNORDERED COLLECTIONS
- What will this print?
  ```python
    s = {1, 2, 2, 3}
    print(s)
  ```
- Add 4 and remove 1.
- Check if 2 is in the set.
- Find intersection and union:
  ```python
    a = {1, 2, 3}
    b = {2, 3, 4}
  ```
- Why can’t you access elements by index in a set?
- Can a set contain a list? Why not?

### FROZENSET — IMMUTABLE SETS
- Create a frozenset({1,2,3}) and try adding a new element.
- Where might frozenset be useful compared to set?

### DICTIONARIES — KEY–VALUE PAIRS
- Create a dictionary for a student: name, age, marks.
- Access the value of "marks".
- Add a "grade".
- Remove "age".
- Loop through all key–value pairs.
- What happens if you use a list as a key?
- What data types can be dictionary keys?
- What’s the difference between:
  ```python
    student["age"]
    student.get("age")
  ```
- Build a mini record:
  ```python
    students = {"Alice": [85, 90], "Bob": [70, 80]}
    print(students["Alice"][1])
  ```

### NONE — ABSENCE OF VALUE
- What does print(None) output?
- How is None different from 0 or False?
- Predict:
  ```python
    x = None
    if x:
        print("Something")
    else:
        print("Nothing")
  ```

### MUTABILITY & MEMORY
- Explain difference:
  ```python
    a = [1,2,3]
    b = a
    c = a[:]
    b.append(4)
    print(a, c)
  ```
- Why does changing b affect a but not c?
- Which types are hashable (usable as dict keys)?
- What happens if you modify a mutable object used as a dict key?

> **Master these data types and you'll be ready for any DSA challenge!**

### DSA READINESS CHECK (LOGIC + DATATYPE USE)
- How would you count frequency of words in a string? (Hint: dict)
- How to remove duplicates from a list but keep order?
- Represent a graph edge list using which data type?
- Given students and marks, print highest average (combine dict + list).
- Which data type best fits each:
  - Ordered names?
  - Unique usernames?
  - Fixed RGB values?
  - Key–value data lookup?
  - Optional placeholder?

### MINI DRILLS (1-LINERS)
- Reverse a string without using loops.
- Get last element of a list.
- Check if number is even using boolean logic.
- Convert list → set → list (remove duplicates).
- Sort dictionary keys alphabetically.
- Count vowels in "artificial intelligence".
- Merge two dicts in one line.
- Get unique words from a sentence.
- Create list [1,4,9,16,25] using list comprehension.

---

