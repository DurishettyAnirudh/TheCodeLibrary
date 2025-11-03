# 🚀 Arrays Playbook - Complete Guide & Practice

## 📚 Table of Contents
1. [Introduction to Arrays in Python](#introduction)
2. [Array-Like Structures Comparison](#array-structures)
3. [Python Built-in Lists](#python-lists)
4. [Array Module](#array-module)
5. [NumPy Arrays](#numpy-arrays)
6. [Array Operations](#array-operations)
7. [Indexing and Slicing](#indexing-slicing)
8. [Reshaping and Broadcasting](#reshaping-broadcasting)
9. [Copy vs View](#copy-view)
10. [Vectorization](#vectorization)
11. [Memory & Performance](#memory-performance)
12. [Common Array Algorithms](#common-algorithms)
13. [Useful Tricks & Patterns](#tricks-patterns)
14. [Practice Problems](#practice-problems)
15. [Interview Questions](#interview-questions)

---

## 🎯 Introduction {#introduction}

Unlike C, C++, or Java — Python does not have a built-in array data structure for general use.

**Instead, you use:**
- `list` for general-purpose dynamic arrays
- `array.array` for memory-efficient typed arrays (homogeneous)
- `NumPy's ndarray` for high-performance numerical arrays (multi-dimensional)

---

## 📊 Array-Like Structures Comparison {#array-structures}

| Type | Library | Homogeneous? | Speed | Use Case |
|------|---------|--------------|-------|----------|
| `list` | Built-in | ❌ (mixed types) | Medium | General purpose |
| `array.array` | Built-in | ✅ | Fast | Typed numeric data |
| `numpy.ndarray` | NumPy | ✅ | 🚀 Very fast | Scientific & ML work |
| `bytearray` | Built-in | ✅ (bytes only) | Fast | Binary data |
| `memoryview` | Built-in | ✅ | Fast | Zero-copy buffer access |

---

## 📝 Python Built-in Lists {#python-lists}

Think of it as a dynamic array.

```python
arr = [1, 2, 3, 4]
arr.append(5)
arr.extend([6, 7])
arr.insert(2, 99)
print(arr)  # [1, 2, 99, 3, 4, 5, 6, 7]
```

### Core Operations

| Operation | Code | Time Complexity |
|-----------|------|-----------------|
| Append | `arr.append(x)` | O(1) amortized |
| Insert | `arr.insert(i, x)` | O(n) |
| Delete by value | `arr.remove(x)` | O(n) |
| Delete by index | `del arr[i]` | O(n) |
| Search | `x in arr` | O(n) |
| Sort | `arr.sort()` `arr.sort(reverse = True)` | O(n log n) |

### Other Methods
```python
arr.pop()         # removes last
arr.index(99)     # find index of value
arr.count(3)      # count occurrences
arr.reverse()     # in-place reverse
sorted(arr)       # returns new sorted list
```

### List Comprehension
```python
squares = [x**2 for x in range(10)]
evens = [x for x in arr if x % 2 == 0]
```

---

## 🔢 Array Module {#array-module}

Provides typed, compact arrays of basic C types.

```python
from array import array

arr = array('i', [1, 2, 3, 4])  # 'i' = signed int
arr.append(5)
print(arr)  # array('i', [1, 2, 3, 4, 5])
```

### Common Type Codes
| Code | Type | Size |
|------|------|------|
| 'b' | signed char | 1 byte |
| 'B' | unsigned char | 1 byte |
| 'i' | signed int | 4 bytes |
| 'f' | float | 4 bytes |
| 'd' | double | 8 bytes |

### Access
```python
arr[0] = 100
print(arr[1:3])  # array('i', [2, 3])
```

**➡️ Advantage:** More memory-efficient than lists for large homogeneous numeric data.

---

## 🧮 NumPy Arrays {#numpy-arrays}

NumPy is the de facto standard for numeric arrays in Python.

```python
import numpy as np
a = np.array([1, 2, 3])
b = np.array([[1, 2], [3, 4]])
```

### Key Attributes
```python
a.ndim      # number of dimensions
a.shape     # (rows, cols)
a.size      # total number of elements
a.dtype     # data type of elements
a.itemsize  # bytes per element
```

---

## ⚡ Array Operations {#array-operations}

NumPy arrays allow element-wise operations (vectorization):

```python
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

print(a + b)  # [5 7 9]
print(a * b)  # [4 10 18]
print(a ** 2) # [1 4 9]
```

### Matrix Operations
```python
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])
print(A @ B)  # Matrix multiplication
```

---

## 🎯 Indexing and Slicing {#indexing-slicing}

### Basic Indexing
```python
a = np.array([10, 20, 30, 40, 50])
print(a[0])     # 10
print(a[-1])    # 50
```

### Slicing
```python
print(a[1:4])     # [20 30 40]
print(a[::-1])    # reversed array
```

### Multidimensional Indexing
```python
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b[1, 2])    # 6
print(b[:, 1])    # 2nd column -> [2 5]
print(b[0, :])    # 1st row -> [1 2 3]
```

---

## 🔄 Reshaping and Broadcasting {#reshaping-broadcasting}

### Reshape
```python
a = np.arange(6)
a = a.reshape(2, 3)
```

### Flatten / Ravel
```python
a.flatten()
a.ravel()  # faster, returns view
```

The Difference: 
```
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = a.flatten()  # Always a copy
c = a.ravel()    # Usually a view

b[0] = 99
c[1] = 88

print(a)  # Only c's change may reflect in a if ravel returned a view
```

o/p :-
```
[[ 1 88]
 [ 3  4]]
```


### Broadcasting
Allows operations on different shapes:

```python
a = np.array([[1, 2, 3],
              [4, 5, 6]])
b = np.array([10, 20, 30])
print(a + b)
# [[11 22 33]
#  [14 25 36]]
```

---

## 📋 Copy vs View {#copy-view}

- **View** → shares same data
- **Copy** → creates a new object

```python
x = np.array([1,2,3])
y = x.view()
z = x.copy()
x[0] = 100
print(y)  # [100 2 3]
print(z)  # [1 2 3]
```

---

## ⚡ Vectorization {#vectorization}

### ❌ Slow way
```python
res = []
for x in a:
    res.append(x**2)
```

### ✅ Fast way
```python
res = a ** 2
```

NumPy's internal implementation uses C loops, giving massive speedups.

---

## 💾 Memory & Performance {#memory-performance}

- Lists store object references, not raw data → more memory
- NumPy arrays store contiguous C-style memory blocks → faster access
- Use `arr.nbytes` to check memory consumption

**Example:**
```python
a = np.arange(1e6)
print(a.nbytes)  # 8 MB (since dtype=float64)
```

---

## 🔧 Common Array Algorithms {#common-algorithms}

| Task | NumPy Code |
|------|------------|
| Sum | `np.sum(a)` |
| Mean | `np.mean(a)` |
| Max/Min | `np.max(a)`, `np.min(a)` |
| Argmax | `np.argmax(a)` |
| Sort | `np.sort(a)` |
| Unique | `np.unique(a)` |
| Cumulative Sum | `np.cumsum(a)` |
| Dot Product | `np.dot(a, b)` |
| Stack Arrays | `np.hstack()`, `np.vstack()` |

---

## 🎪 Useful Tricks & Patterns {#tricks-patterns}

```python
np.linspace(0, 1, 5)    # [0. 0.25 0.5 0.75 1.]
np.arange(0, 10, 2)     # [0 2 4 6 8]
np.zeros((2,3))         # all zeros
np.ones((2,3))          # all ones
np.eye(3)               # identity matrix
np.random.rand(2,3)     # random floats 0-1
np.random.randint(10, size=(2,2))  # random ints
```

---

## 🧩 Practice Problems {#practice-problems}

### 🧱 SECTION 1: Python Lists

#### 🪜 1. Basic Creation and Access
1. Create a list of numbers from 1 to 5 and print the 3rd element
2. Create a list of 5 strings and print the first and last items
3. Create an empty list and add elements 10, 20, 30 using `append()`

#### 🧩 2. Insertion and Deletion
1. Start with `[10, 20, 30, 40]`. Insert 25 at index 2
2. Remove the element 30 from the list
3. Delete the element at index 1 using `del`
4. Use `pop()` to remove the last element and print it

#### 🧮 3. Searching and Counting
1. Create a list `[2, 3, 4, 2, 5, 2]`. Count how many times 2 occurs
2. Find the index of the first occurrence of 4
3. Check if 6 exists in the list

#### 🧠 4. Sorting and Reversing
1. Sort `[4, 1, 3, 2]` in ascending and descending order
2. Reverse `[1, 2, 3, 4, 5]` in place
3. Use `sorted()` to get a new sorted list from `[3, 1, 4, 2]`

#### 🧮 5. Combining and Extending
1. Combine `[1, 2, 3]` and `[4, 5]` using `+`
2. Extend `[1, 2]` with `[3, 4]` using `.extend()`
3. Multiply `[1, 2] * 3` — what's the output?

#### 💡 6. List Comprehension
1. Create a list of squares of numbers 1–5
2. Create a list of even numbers from 1–10
3. Create a list of strings from another list, all in uppercase
4. Create a list of cubes but only for odd numbers from 1–10

### 🧱 SECTION 2: Array Module

#### ⚙️ 1. Creating Typed Arrays
1. Create an integer array 'i' with `[1, 2, 3, 4]`
2. Create a float array 'f' with `[1.2, 3.4, 5.6]`
3. Try to append a string to the integer array — what happens?

#### 🧩 2. Access and Slicing
1. Create an array 'i' from `[10, 20, 30, 40, 50]` and print the 2nd element
2. Print a slice containing the middle 3 elements
3. Change the first element to 100

#### 🔧 3. Array Operations
1. Append 60 and remove 30 from the array
2. Reverse the array using slicing
3. Convert the array to a list using `.tolist()`
4. Write a loop to print all elements of an array using a for loop

### 🧱 SECTION 3: NumPy Arrays

#### ⚡ 1. Creation and Attributes
1. Create a 1D array `[1, 2, 3, 4, 5]`
2. Create a 2D array `[[1,2,3],[4,5,6]]`
3. Print `ndim`, `shape`, `size`, `dtype` for each
4. Create an array of zeros with shape `(2,3)`
5. Create an array of ones with shape `(3,2)`
6. Create an array of random integers between 1–10 with shape `(2,2)`

#### 🧮 2. Arithmetic Operations
Create arrays `a = [1,2,3]`, `b = [4,5,6]` and compute:
1. `a + b`
2. `a * b`
3. `a ** 2`
4. `a + 10`

Compute dot product of:
```python
A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
```

#### 🔢 3. Indexing & Slicing
Create `a = np.array([10,20,30,40,50])`:
1. Print 1st and last element
2. Slice first 3 elements
3. Reverse using slicing

Create a 2D array `[[1,2,3],[4,5,6],[7,8,9]]`:
1. Print the 2nd row
2. Print the 3rd column
3. Print the element in 2nd row, 3rd column

#### 🧬 4. Reshaping & Flattening
1. Create `np.arange(6)` and reshape it to `(2,3)`
2. Flatten the 2D array using `.flatten()` and `.ravel()`
3. Try reshaping `(2,3)` array to `(3,2)`

#### 📐 5. Broadcasting
Add `np.array([10,20,30])` to:
1. `np.array([[1,2,3],[4,5,6]])`
2. Multiply `[1,2,3]` with `[10]` (scalar broadcast)

#### 🧩 6. Copy vs View
1. Create `a = np.array([1,2,3])`
2. Make a view `b = a.view()`
3. Make a copy `c = a.copy()`
4. Change `a[0]` and print all three

#### 🧮 7. Math & Reduction Operations
1. Use `np.sum`, `np.mean`, `np.min`, `np.max`, `np.std` on `[1,2,3,4,5]`
2. Use `np.argmax` and `np.argmin` on `[3,1,5,2,4]`
3. Compute `np.cumsum` and `np.cumprod` on `[1,2,3,4]`
4. Find unique elements in `[1,2,2,3,3,3,4]`

#### 🧠 8. Boolean Masking & Fancy Indexing
1. Create `[1,2,3,4,5,6]` and print only even numbers
2. Replace all numbers > 3 with 99
3. Use fancy indexing to print elements at positions `[0, 2, 4]`

#### 🧩 9. Stacking & Splitting
1. Stack `[1,2,3]` and `[4,5,6]` vertically and horizontally
2. Split `[10,20,30,40,50,60]` into 3 equal parts

#### 📊 10. Matrix & Linear Algebra
1. Create identity matrix of size 3 using `np.eye(3)`
2. Compute determinant of `[[1,2],[3,4]]`
3. Compute inverse of `[[4,7],[2,6]]`
4. Compute transpose of a 2×3 matrix
5. Compute dot product of two 3×1 vectors

#### 🎲 11. Random & Range Functions
1. `np.arange(0, 10, 2)`
2. `np.linspace(0, 1, 5)`
3. Generate 3x3 random matrix using `np.random.rand`
4. Generate random integers 1–100 with shape `(2,3)`
5. Set seed with `np.random.seed(0)` and generate a random 1D array of size 5

### 🧩 Challenge Mini-Practices (Review)
1. Create a list → convert to NumPy array → square every element
2. Create a NumPy array → slice out all odd-indexed elements
3. Stack two 2D arrays vertically → flatten → compute mean
4. Replace all negative numbers in an array with 0
5. Reshape 1D array of size 12 into `(3,4)` and get its 2nd column

### 🧠 Optional (Advanced)
1. Use `np.concatenate()` to merge arrays of different shapes along axis 0
2. Use `np.where()` to replace all elements < 5 with 0
3. Use `np.all()` and `np.any()` on a boolean array
4. Use `np.dot()` to compute the product of 2D matrices
5. Measure time of NumPy vs list operation with `timeit`

---

## 🎯 Summary Table

| Concept | List | array.array | NumPy |
|---------|------|-------------|-------|
| Mixed Data | ✅ | ❌ | ❌ |
| Speed | ⚙️ | ⚡ | 🚀 |
| Memory Efficiency | ❌ | ✅ | ✅✅ |
| Multi-Dimensional | ❌ | ❌ | ✅ |
| Math Operations | ❌ | ❌ | ✅ |
| Broadcasting | ❌ | ❌ | ✅ |

---

## 💼 Interview-Level Questions {#interview-questions}

1. **What's the difference between `list` and `array.array`?**
2. **What's the difference between view and copy in NumPy?**
3. **How does broadcasting work in NumPy?**
4. **Why are NumPy arrays faster than Python lists?**
5. **How do you reshape a 1D array into a 2D one?**
6. **What is vectorization and why is it important?**
7. **How do you handle arrays larger than memory?** (numpy.memmap or dask)

---

## 🧩 Bonus: Multidimensional & Advanced Topics

### Boolean Masking:
```python
a = np.array([1,2,3,4,5])
print(a[a > 2])  # [3 4 5]
```

### Fancy Indexing:
```python
a = np.arange(10)
print(a[[1,3,5,7]])  # [1 3 5 7]
```

### Stacking:
```python
np.hstack([a, b])
np.vstack([a, b])
```

### Splitting:
```python
np.split(a, 3)
```

### Transpose:
```python
a.T
```

### Dot and Cross Product:
```python
np.dot(a, b)
np.cross(a, b)
```

---

## ✅ TL;DR Summary

| Level | Structure | What You Should Use |
|-------|-----------|-------------------|
| Beginner | `list` | For general data storage |
| Intermediate | `array.array` | For memory-efficient homogeneous data |
| Advanced | `numpy.ndarray` | For numerical, scientific, or ML work |

---

> 🎯 **Goal:** Each problem should be small enough that you can complete it in under a minute. The output is simple (print arrays, numbers, or booleans). You'll "feel" what each function does — building that crucial muscle memory!

**Happy coding! 🚀**