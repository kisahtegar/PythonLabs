# Matrix & Cubes

A list is a versatile data structure that can store multiple elements. Lists can be one-dimensional (1D), two-dimensional (2D), or even higher-dimensional.

## 1D List

A one-dimensional list is a simple list that contains elements in a linear sequence.

```py
my_list = [1, 2, 3, 4, 5]
print(my_list)  # Output: [1, 2, 3, 4, 5]
```

## 2D List

A two-dimensional list is essentially a list of lists. Each element in the outer list is itself a list.

```py
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix)  # Output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
```

## 3D List

A three-dimensional list is a list of lists of lists. It can be thought of as a cube of elements, where each element is a list.

```py
cube = [
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [10, 11, 12],
        [13, 14, 15],
        [16, 17, 18]
    ],
    [
        [19, 20, 21],
        [22, 23, 24],
        [25, 26, 27]
    ]
]

print(cube) # Output: [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]], [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]

```

## Numpy

Using the same matrix, namely "[[1, 2, 3], [4, 5, 6], [7, 8, 9]]" produces a different amount of memory for each method. If we use NumPy, the memory used for all elements is 72. However, if we use lists, the memory used for all elements is 240.

```py
import numpy 
import sys

var_list= [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var_array= numpy.array([[1, 2, 3], [4, 5, 6], [7, 8 ,9]])

print("Ukuran keseluruhan elemen list dalam bytes = ",sys.getsizeof(var_list)*len(var_list))
print("Ukuran keseluruhan elemen NumPy dalam bytes = ", var_array.size*var_array.itemsize)


"""
Output:
Ukuran keseluruhan elemen list dalam bytes =  240
Ukuran keseluruhan elemen NumPy dalam bytes =  72
"""
```
