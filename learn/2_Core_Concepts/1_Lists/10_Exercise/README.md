# Exercise

## Basic List Creation

**Challenge 1:** Create lists in different ways.

1. **Using square brackets:** Create a list of your favorite colors.
2. **Using the list() function:** Create a list from a string (e.g., `list("hello")`).
3. **Using list comprehension (bonus challenge):** Create a list of squares from numbers 1 to 5 (e.g., `[x**2 for x in range(1, 6)]`).

    ```py
    favorite_colors = ["blue", "green", "red", "yellow"]
    print(favorite_colors)

    string_list = list("hello")
    print(string_list)

    squares = [x**2 for x in range(1, 6)]
    print(squares)
    ```

## Accessing List Elements

**Challenge 2:** Access elements in a list of fruits.

1. Access the first and last element using indices (0 and -1).
2. Print a specific element by index (e.g., the element at index 2).

    ```python
    fruits = ["apple", "banana", "cherry", "date", "elderberry"]
    first_fruit = fruits[0]
    last_fruit = fruits[-1]
    specific_fruit = fruits[2]
    print(f"First fruit: {first_fruit}")
    print(f"Last fruit: {last_fruit}")
    print(f"Fruit at index 2: {specific_fruit}")
    ```

## Modifying Lists

**Challenge 3:** Update and remove items in a list of numbers.

1. Update the value at a specific index (e.g., change the element at index 1 to a new value).
2. Use negative indexing to modify elements from the end (e.g., change the second-to-last element).

    ```py
    numbers = [10, 20, 30, 40, 50]
    numbers[1] = 25  # Update the element at index 1
    print(numbers)  # Output: [10, 25, 30, 40, 50]

    numbers[-2] = 45  # Update the second-to-last element
    print(numbers)  # Output: [10, 25, 30, 45, 50]
    ```

## Removing List Items

**Challenge 4:** Remove items from a grocery list.

1. Remove a specific item by value (e.g., "milk") using the `remove()` method.
2. Remove the element at a specific index using the `pop()` method.

    ```py
    grocery_list = ["bread", "milk", "eggs", "butter"]
    grocery_list.remove("milk")  # Remove the item "milk"
    print(grocery_list)  # Output: ["bread", "eggs", "butter"]
    grocery_list.pop(1)  # Remove the item at index 1
    print(grocery_list)  # Output: ["bread", "butter"]
    ```

## Multi-Dimensional Lists

**Challenge 5:** Create a two-dimensional list for a tic-tac-toe board.

- Initialize the board with empty elements (e.g., with "-" or `None`).

    ```py
    tic_tac_toe_board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"]
    ]
    print(tic_tac_toe_board)
    ```

**Challenge 6:** Create a three-dimensional list for a Rubik's cube.

- Initialize each element with a color representing a cube face.

    ```python
    rubiks_cube = [
        [["white"] * 3 for _ in range(3)],  # Top face
        [["red"] * 3 for _ in range(3)],    # Front face
        [["blue"] * 3 for _ in range(3)],   # Right face
        [["orange"] * 3 for _ in range(3)], # Back face
        [["green"] * 3 for _ in range(3)],  # Left face
        [["yellow"] * 3 for _ in range(3)]  # Bottom face
    ]
    print(rubiks_cube)
    ```

## Iterating Through Lists

**Challenge 7:** Iterate through a list of names.

1. Use a for loop to iterate through the list and print each name.
2. Print the index and element together using `enumerate()` (e.g., "(0, Alice)" for the first element).

    ```py
    names = ["Alice", "Bob", "Charlie", "David"]

    for name in names:
        print(name)

    for index, name in enumerate(names):
        print(f"({index}, {name})")
    ```

## List Unpacking

**Challenge 8:** Unpack elements from a student information list.

- Create a list of student information (name, age, grade).
- Use list unpacking to assign these values to separate variables.

    ```py
    student_info = ["Alice", 15, "A"]
    name, age, grade = student_info
    print(f"Name: {name}, Age: {age}, Grade: {grade}")
    ```
