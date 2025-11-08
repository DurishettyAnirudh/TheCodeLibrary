# 🧠 Bitwise Operations Playbook - Complete Guide & Practice

## 📚 Table of Contents
1. [Introduction](#introduction)
2. [Bitwise Operators](#bitwise-operators)
3. [Common Bitwise Tricks](#common-tricks)
4. [Bit Masks](#bit-masks)
5. [Advanced Applications](#advanced-applications)
6. [Theory & Examples](#theory-examples)
7. [Drill Problems](#drill-problems)
8. [Application Problems](#application-problems)
9. [Tips for Muscle Memory](#tips)

---

## 🎯 Introduction {#introduction}

Bitwise operations are operations that directly manipulate **individual bits** of integers. They are fast, memory-efficient, and often used in **competitive programming, low-level programming, and optimization problems**.

Bitwise operations work on the binary representation of numbers.

**Example:**
```
a = 5  # 0101 in binary
b = 3  # 0011 in binary
```

---

## ⚡ Bitwise Operators {#bitwise-operators}

### 2.1 AND (`&`)
**Operation**: Returns `1` if both corresponding bits are `1`, else `0`.

```python
a = 5  # 0101
b = 3  # 0011
a & b  # 0001 -> 1
```

**Use case:** Check if a bit is set.
```python
if a & 1:   # Check if least significant bit is 1
    print("LSB is 1")
```

### 2.2 OR (`|`)
**Operation**: Returns `1` if **any one** of the corresponding bits is `1`.

```python
a = 5  # 0101
b = 3  # 0011
a | b  # 0111 -> 7
```

**Use case:** Set specific bits to `1`.
```python
a = 5
a = a | 2  # Set 2nd LSB
```

### 2.3 XOR (`^`)
**Operation**: Returns `1` if bits are **different**.

```python
a = 5  # 0101
b = 3  # 0011
a ^ b  # 0110 -> 6
```

**Use cases:**
- Swap two numbers without a temporary variable
- Find the **unique element** in an array where all others appear twice

### 2.4 NOT (`~`)
**Operation**: Flips all bits (`1` → `0`, `0` → `1`).

```python
a = 5  # 0101
~a     # 1010 (in 2's complement, -6 in decimal)
```

**Note:** Python stores negative numbers in **infinite 2's complement**, so `~a = -a - 1`.

### 2.5 Left Shift (`<<`)
**Operation**: Shift bits to the left by `n` positions; fills 0 from the right.

```python
a = 5      # 0101
a << 1     # 1010 -> 10
a << 2     # 10100 -> 20
```

**Use case:** Multiply by powers of 2.
```python
x << n  # x * (2**n)
```

### 2.6 Right Shift (`>>`)
**Operation**: Shift bits to the right by `n` positions.

```python
a = 20     # 10100
a >> 1     # 01010 -> 10
a >> 2     # 00101 -> 5
```

**Use case:** Divide by powers of 2 (integer division).

---

## 🧩 Common Bitwise Tricks {#common-tricks}

1. **Check if a number is even or odd**:
```python
if n & 1:
    print("Odd")
else:
    print("Even")
```

2. **Get the rightmost set bit**:
```python
n & -n
```

3. **Turn off the rightmost set bit**:
```python
n = n & (n-1)
```

4. **Count number of set bits**:
```python
count = 0
while n:
    n &= n-1
    count += 1
```

5. **Check if a number is power of two**:
```python
n > 0 and (n & (n-1)) == 0
```

6. **Swap two numbers without temp**:
```python
x ^= y
y ^= x
x ^= y
```

---

## 🎭 Bit Masks {#bit-masks}

A **bitmask** is a number used to **manipulate bits selectively**.

```python
# Set 3rd bit
n |= (1 << 2)

# Clear 3rd bit
n &= ~(1 << 2)

# Toggle 3rd bit
n ^= (1 << 2)
```

---

## 🚀 Advanced Applications {#advanced-applications}

### 1. Subset Generation Using Bits
```python
nums = [1,2,3]
n = len(nums)
for mask in range(1<<n):
    subset = [nums[i] for i in range(n) if mask & (1<<i)]
    print(subset)
```

### 2. Gray Code Generation
Gray code: consecutive numbers differ by **1 bit**
```python
def gray_code(i):
    return i ^ (i >> 1)
```

### 3. Finding Single Number in Array
Given array where all elements appear twice except one:
```python
def single_number(arr):
    res = 0
    for num in arr:
        res ^= num
    return res
```

---

## 📖 Theory & Examples {#theory-examples}

### Binary Representation Practice
| Decimal | 8-bit Binary | Set Bits | Unset Bits |
|---------|--------------|----------|------------|
| 5       | 00000101     | 0,2      | 1,3,4,5,6,7|
| 12      | 00001100     | 2,3      | 0,1,4,5,6,7|
| 23      | 00010111     | 0,1,2,4  | 3,5,6,7    |
| 60      | 00111100     | 2,3,4,5  | 0,1,6,7    |

### Operator Truth Tables
| A | B | A & B | A \| B | A ^ B |
|---|---|-------|--------|-------|
| 0 | 0 |   0   |   0    |   0   |
| 0 | 1 |   0   |   1    |   1   |
| 1 | 0 |   0   |   1    |   1   |
| 1 | 1 |   1   |   1    |   0   |

---

## 🎯 Drill Problems {#drill-problems}

### Level 1: Binary Basics (1-10)
1. Write the 8-bit binary of: 5, 12, 23, 60
2. Convert these 8-bit binaries to decimal: 1010, 1111, 0101, 1001
3. Write the 8-bit binary of 0, 1, 2, 3, 4, 7, 15, 31
4. Identify the LSB (least significant bit) of: 5, 10, 23, 44
5. Identify the MSB (most significant bit) of: 5, 12, 20, 60
6. Which numbers have all bits 1 in 3-bit representation?
7. Which numbers have only one bit set between 0-15?
8. Convert 13 to binary and identify positions of set bits
9. Convert 22 to binary and identify positions of unset bits
10. For n = 19 (10011), count 1s and 0s

### Level 2: AND, OR, XOR (11-20)
11. Compute 5 & 3. Show binary and decimal
12. Compute 5 | 3
13. Compute 5 ^ 3
14. Compute 12 & 10
15. Compute 12 | 10
16. Compute 12 ^ 10
17. Compute 7 & 15
18. Compute 7 | 15
19. Compute 7 ^ 15
20. Compute (6 ^ 3) & 5

### Level 3: NOT & Bit Flipping (21-25)
21. Compute ~5 for 8-bit numbers. Show binary and decimal
22. Compute ~12
23. Compute ~0
24. Flip all bits of 10101010
25. Flip all bits of 11110000

### Level 4: Shifts (26-33)
26. Compute 5 << 1. Show binary and decimal
27. Compute 3 << 2
28. Compute 12 << 3
29. Compute 20 >> 1
30. Compute 20 >> 2
31. Compute 40 >> 3
32. For n = 7 (0111), compute n << 2
33. For n = 15 (1111), compute n >> 3

### Level 5: Bit Tricks (34-42)
34. Find rightmost set bit of n = 12 (n & -n)
35. Find rightmost set bit of n = 10
36. Turn off rightmost set bit of n = 14
37. Turn off rightmost set bit of n = 21
38. Check if n = 16 is power of 2 using n & (n-1)
39. Check if n = 18 is power of 2
40. Count set bits in n = 7
41. Count set bits in n = 15
42. Count set bits in n = 19

### Level 6: Set, Clear, Toggle Bits (43-46)
43. For n = 9 (1001), set 2nd bit
44. For n = 9, clear 3rd bit
45. For n = 9, toggle 0th bit
46. For n = 9, toggle 1st and 3rd bits

### Level 7: XOR Patterns & Mental Tricks (47-50)
47. Compute mentally: 5 ^ 5, 0 ^ 12, 7 ^ 3 ^ 3, 6 ^ 1 ^ 6
48. Compute (a ^ b) ^ b for a=10, b=7. Explain the result
49. Compute a ^ 0 for a = 15, 23, 42. Observe the pattern
50. Convert numbers 0,1,2,3 to 2-bit Gray code using n ^ (n >> 1)

---

## 🚀 Application Problems {#application-problems}

### Basic Applications (1-10)
1. **Even/Odd Checker**: Check if number is even or odd using bitwise
2. **Number Swapper**: Swap two numbers without temp variable
3. **Bit Counter**: Count number of set bits in a number
4. **Power of Two**: Check if number is power of 2
5. **Rightmost Set Bit**: Find position of rightmost set bit
6. **Turn Off Bit**: Turn off the rightmost set bit
7. **Binary to Decimal**: Convert binary string to decimal without built-ins
8. **Decimal to Binary**: Convert decimal to binary string without built-ins
9. **Bit Position**: Check if kth bit is set
10. **Bit Manipulation**: Set, clear, toggle kth bit

### Intermediate Applications (11-20)
11. **Single Number I**: Find unique element in array where others appear twice
12. **Single Number II**: Find unique element where others appear thrice
13. **Missing Number**: Find missing number in array 0 to n
14. **Duplicate Number**: Find duplicate in array of n+1 integers
15. **Subset Generation**: Generate all subsets using bitmask
16. **Hamming Distance**: Calculate Hamming distance between two numbers
17. **Reverse Bits**: Reverse bits of a 32-bit number
18. **Number of 1 Bits**: Count set bits (Hamming weight)
19. **Binary Addition**: Add two binary strings
20. **Gray Code**: Generate n-bit Gray code sequence

### Advanced Applications (21-30)
21. **Two Single Numbers**: Find two numbers appearing once when others appear twice
22. **Maximum XOR**: Find maximum XOR of any two numbers in array
23. **XOR Queries**: Answer XOR queries on array efficiently
24. **Bit Trie**: Implement trie for binary representations
25. **Subarray XOR**: Count subarrays with given XOR
26. **Minimum XOR Pair**: Find pair with minimum XOR
27. **Divide Without Division**: Divide two integers without using division
28. **Multiply Without Multiplication**: Multiply using only addition and shifts
29. **Count Set Bits Range**: Count set bits in range [L, R]
30. **Bitwise DP**: Solve traveling salesman using bitmask DP

### Real-World Applications (31-40)
31. **Permission System**: Implement user permissions using bitmasks
32. **Feature Flags**: Implement feature toggle system
33. **Compression**: Basic run-length encoding using bits
34. **Hash Function**: Create simple hash function using XOR
35. **Checksum**: Calculate simple checksum for error detection
36. **State Machine**: Implement finite state machine using bits
37. **Bloom Filter**: Implement basic bloom filter
38. **Cache Simulation**: Simulate cache using bit operations
39. **Network Mask**: Calculate network and broadcast addresses
40. **Game States**: Represent game board states using bits

### Contest/Interview Problems (41-50)
41. **Bitwise AND Range**: Bitwise AND of numbers in range [m,n]
42. **Sum of Two Integers**: Add without using + operator
43. **Counting Bits**: Count bits for numbers 0 to n
44. **Repeated DNA**: Find repeated DNA sequences
45. **UTF-8 Validation**: Validate UTF-8 encoding
46. **Integer Replacement**: Replace integer with operations to reach 1
47. **Maximum Product**: Maximum product of word lengths (no common letters)
48. **Generalized Abbreviation**: Generate all possible abbreviations
49. **Minimum Flips**: Minimum flips to make OR equal target
50. **Stone Game**: Stone game with XOR operations

---

## ✅ Tips for Muscle Memory {#tips}

1. **Do not rely on built-in functions** 
2. **Write binary representations** on paper for all problems
3. **Practice every operator** individually before combining
4. **Solve small problems multiple times** to internalize tricks
5. **Always think in bits, not decimal**


### Quick Reference Card:
```python
# Essential Bit Tricks
n & 1           # Check if odd
n & (n-1)       # Turn off rightmost set bit
n & -n          # Get rightmost set bit
n | (1<<k)      # Set kth bit
n & ~(1<<k)     # Clear kth bit
n ^ (1<<k)      # Toggle kth bit
n >> k          # Divide by 2^k
n << k          # Multiply by 2^k
```

---

> **Master bitwise operations and unlock the power of low-level programming!** 🚀