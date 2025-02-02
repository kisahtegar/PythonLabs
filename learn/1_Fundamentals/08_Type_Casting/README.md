# Type Casting

Type casting refers to the process of converting one data type into another. Python provides several built-in functions for type casting, allowing you to convert variables from one type to another

## int()

Converts a value to an integer.

```py
float_num = 3.14
int_num = int(float_num)
print(int_num)  # 3
```

## float()

Converts a value to a floating-point number.

```py
int_num = 5
float_num = float(int_num)
print(float_num)  # 5.0
```

## str()

Converts a value to a string.

```py
num = 42
str_num = str(num)
print(str_num)  # '42'
```

## bool()

Converts a value to a boolean.

```py
num = 0
bool_value = bool(num)
print(bool_value)  # False
```

---

## Challenges

## Challenge 1: String to Integer

- Prompt the user to enter their age as a string.
- Convert the string to an integer using `int()`.
- Print the age as a number.

    ```py
    age = input("What is your current age? ")
    age_as_int = int(age)
    print(age_as_int)
    ```

## Challenge 2: Integer to Float**

- Prompt the user to enter the radius of a circle as an integer.
- Convert the integer radius to a float using `float()`.
- Calculate the area of the circle using the formula: `area = 3.14 * radius * radius`.
- Print the calculated area.

    ```py
    radius_circle = input("Enter the radius of the circle: ")
    radius_as_float = float(radius_circle)
    area = 3.14 * radius_as_float * radius_as_float
    print(radius_as_float)
    ```
