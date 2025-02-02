# Tuples?

Tuple is an ordered, immutable collection of elements. This means that once you create a tuple, you cannot modify its contents - you can't add, remove, or change elements in a tuple after it has been created. Tuples are defined by enclosing a comma-separated sequence of values in parentheses `()`

## Basic Syntax

```py
my_tuple = (1, 2, 3, 'hello', 3.14)
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 'hello'
print(len(my_tuple)) # Output: 5
```

## Error

```py
my_tuple = (1, 2, 3, 'hello', 3.14)
# This will raise an error since tuples are immutable
# my_tuple[0] = 5

# Creating a new tuple with modified content
new_tuple = my_tuple + (5, 'world')
print(new_tuple)  # Output: (1, 2, 3, 'hello', 3.14, 5, 'world')
```

## Weird Things About Tuples

```py
nums = 1, 2, 3, 4, 5
print(type(nums))  # tuple

notTuple = 50
isTuple = (50,)
print(type(notTuple))  # number
print(type(isTuple))  # tuple
```

## Iterating Over Tuple

```py
friends = ("alex", "michel", "jordan")
for friend in friends:
    print(friend)
```

---

## Exercise

This document explores working with tuples in Python. We'll cover creating tuples, accessing elements, immutability, and unpacking.

### Challenge 1: Creating Tuples

- **Using parentheses ():** Create a tuple containing your favorite foods.
- **Using the tuple() function:** Create a tuple from a list (e.g., `tuple(["apple", "banana", "cherry"])`).

```py
favorite_food = ("Bakso", "Mie", "Nasi")
print(favorite_food)

fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)
```

### Challenge 2: Accessing Tuple Elements

- Create a tuple containing different data types (string, number, boolean).
- Access elements using their index (just like with lists).

```py
my_data = ("Kisah", 10, True)
print(my_data[0])
print(my_data[1])
print(my_data[2])
```

### Challenge 3: Immutability of Tuples

- Try to modify an element in a tuple using indexing and assignment (e.g., `my_tuple[0] = "new value"`).
- Observe the error message that you'll get since tuples are immutable (unchangeable).

```py
my_tuple = ("apple", "banana", "cherry")
try:
    my_tuple[0] = "new value"
except TypeError as e:
    print(f"Error: {e}")
```

### Challenge 4: Unpacking Tuples

- Create a tuple with student information (name, age, grade).
- Use tuple unpacking to assign these values to separate variables.

```py
student_info = ("John Doe", 20, "A")
name, age, grade = student_info
print(f"Name: {name}, Age: {age}, Grade: {grade}")
```
