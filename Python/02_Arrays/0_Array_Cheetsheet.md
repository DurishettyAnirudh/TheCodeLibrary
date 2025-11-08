# 🧩 Arrays Functions & Methods Cheatsheet (Ordered by Usefulness)

This cheatsheet lists the most common Python array-related functions and methods, ordered from most frequently used (top) to more advanced or rarely used (bottom). Use this as a quick reference for array manipulation in Python!

---

## 📝 Python Built-in List Methods (Most Common First)
| Method                | Purpose / Example Usage                                 |
|-----------------------|---------------------------------------------------------|
| `append()`            | Add element to end: `lst.append(5)`                     |
| `extend()`            | Add multiple elements: `lst.extend([6,7])`              |
| `insert()`            | Insert at index: `lst.insert(2, 99)`                    |
| `remove()`            | Remove first occurrence: `lst.remove(3)`                |
| `pop()`               | Remove and return last (or index): `lst.pop()`          |
| `del`                 | Delete by index: `del lst[1]`                           |
| `index()`             | Find index of value: `lst.index(99)`                    |
| `count()`             | Count occurrences: `lst.count(2)`                       |
| `sort()`              | Sort in place: `lst.sort()`                             |
| `sorted()`            | Return sorted copy: `sorted(lst)`                       |
| `reverse()`           | Reverse in place: `lst.reverse()`                       |
| `reversed()`          | Return reversed iterator: `reversed(lst)`               |
| `copy()`              | Shallow copy: `lst.copy()`                              |
| `clear()`             | Remove all elements: `lst.clear()`                      |
| List comprehension    | `[x**2 for x in lst]`                                   |
| Slicing               | `lst[1:4]`, `lst[::-1]`                                 |
| Membership            | `x in lst`, `x not in lst`                              |

---

## 🔢 array.array Methods (Most Common First)
| Method                | Purpose / Example Usage                                 |
|-----------------------|---------------------------------------------------------|
| `append()`            | Add element: `arr.append(5)`                            |
| `extend()`            | Add multiple elements: `arr.extend([6,7])`              |
| `insert()`            | Insert at index: `arr.insert(2, 99)`                    |
| `remove()`            | Remove first occurrence: `arr.remove(3)`                |
| `pop()`               | Remove and return last (or index): `arr.pop()`          |
| `del`                 | Delete by index: `del arr[1]`                           |
| `index()`             | Find index of value: `arr.index(99)`                    |
| `count()`             | Count occurrences: `arr.count(2)`                       |
| `reverse()`           | Reverse in place: `arr.reverse()`                       |
| Slicing               | `arr[1:4]`, `arr[::-1]`                                 |
| Membership            | `x in arr`, `x not in arr`                              |
| `tolist()`            | Convert to list: `arr.tolist()`                         |
| Type codes            | `'i'`, `'f'`, `'d'`, etc. for type specification        |

---

## 🧮 NumPy Array Functions & Methods (Most Common First)
| Function/Method         | Purpose / Example Usage                                 |
|------------------------|---------------------------------------------------------|
| `np.array()`           | Create a NumPy array                                    |
| `np.arange()`          | Create array with range of values                       |
| `np.zeros()`           | Create array of zeros                                   |
| `np.ones()`            | Create array of ones                                    |
| `np.eye()`             | Create identity matrix                                  |
| `np.shape`             | Get array shape                                         |
| `np.ndim`              | Get number of dimensions                                |
| `np.size`              | Get total number of elements                            |
| `np.dtype`             | Get data type of array                                  |
| `np.itemsize`          | Get size of each element (bytes)                        |
| `np.reshape()`         | Change shape of array                                   |
| `np.flatten()`         | Flatten array to 1D (returns copy)                      |
| `np.ravel()`           | Flatten array to 1D (returns view if possible)          |
| `np.transpose()` / `.T`| Transpose array                                         |
| `np.sum()`             | Sum of all elements                                     |
| `np.mean()`            | Mean of elements                                        |
| `np.min()` / `np.max()`| Minimum / Maximum value                                 |
| `np.argmin()`/`np.argmax()`| Index of min/max value                            |
| `np.sort()`            | Sort array                                              |
| `np.unique()`          | Get unique elements                                     |
| `np.cumsum()`          | Cumulative sum                                          |
| `np.cumprod()`         | Cumulative product                                      |
| `np.dot()`             | Dot product (matrix multiplication)                     |
| `np.hstack()`          | Stack arrays horizontally                               |
| `np.vstack()`          | Stack arrays vertically                                 |
| `np.concatenate()`     | Concatenate arrays along axis                           |
| `np.split()`           | Split array into sub-arrays                             |
| `np.where()`           | Conditional selection                                   |
| `np.copy()`            | Create a copy of array                                  |
| `np.view()`            | Create a view of array                                  |
| `np.broadcast_to()`    | Broadcast array to new shape                            |
| `np.take()`            | Take elements by index                                  |
| `np.put()`             | Set values by index                                     |
| `np.delete()`          | Delete elements by index                                |
| `np.insert()`          | Insert elements                                         |
| `np.diag()`            | Extract or create diagonal                              |
| `np.tile()`            | Repeat array                                            |
| `np.repeat()`          | Repeat elements                                         |
| `np.clip()`            | Limit values to interval                                |
| `np.round()`           | Round elements                                          |
| `np.floor()` / `np.ceil()`| Floor/Ceil elements                                 |
| `np.random.rand()`     | Random floats array                                     |
| `np.random.randint()`  | Random integers array                                   |
| `np.isin()`            | Test if elements are in another array                   |
| `np.argsort()`         | Indices that would sort array                           |
| `np.count_nonzero()`   | Count non-zero elements                                 |
| `np.all()` / `np.any()`| Test if all/any elements are True                       |
| `np.array_equal()`     | Test if arrays are equal                                |
| `np.memmap()`          | Memory-mapped array (large arrays)                      |

---

> Use this table to quickly find the right function for your array task. For most DSA and coding interview prep, the top 10-15 functions for each type will cover 95% of your needs!
