# Exercise

## 1. Basic Function with Parameters

- **Challenge:** Write a function that takes two numbers (`a` and `b`) as parameters and returns their sum. Call the function with different numeric arguments to test it.

    ```py
    def add_numbers(a, b):
        return a + b

    print(add_numbers(5, 3))  # Output: 8
    print(add_numbers(10, 20)) # Output: 30
    ```

## 2. Default Parameter Values

- **Challenge:** Modify the function from Challenge 1 to have a default value for the second parameter (`b`) in case it's not provided during the function call. Set the default value to 10. Call the function with one and two arguments to see how the default value works.

    ```python
    def add(a, b=10):
        return a + b

    # Calling the function with one argument
    result1 = add(5)
    print(f"Result with one argument: {result1}")  # Output: 15

    # Calling the function with two arguments
    result2 = add(5, 20)
    print(f"Result with two arguments: {result2}")  # Output: 25
    ```

## 3. Named Arguments

- **Challenge:** Write a function that calculates the area of a rectangle. It should take two parameters for width and height. Call the function with the arguments named appropriately (e.g., `area(width=5, height=10)`) to demonstrate named arguments.

    ```python
    def area(width, height):
        return width * height

    # Calling the function with named arguments
    rectangle_area = area(width=5, height=10)
    print(f"Area of the rectangle: {rectangle_area}")  # Output: 50
    ```

## 4. Docstrings and Return Statements

- **Challenge:** Add a docstring to the function explaining its purpose and parameters. Ensure the function returns the calculated value using a return statement.

    ```python
    def add(a, b=10):
        """
        Adds two numbers.

        Parameters:
        a (int or float): The first number.
        b (int or float, optional): The second number. Default is 10.

        Returns:
        int or float: The sum of the two numbers.
        """
        return a + b

    # Example usage
    result = add(5)
    print(result)  # Output: 15
    ```

## 5. Nested Functions

- **Challenge:** Write a function that calculates the factorial of a number (factorial of a number is the product of all positive integers less than or equal to that number). Define another function within the first function (nested function) to perform the factorial calculation recursively. The outer function can call the nested function and return the result.

    ```python
    def factorial(n):
        """
        Calculates the factorial of a number.

        Parameters:
        n (int): The number to calculate the factorial for.

        Returns:
        int: The factorial of the number.
        """
        def recursive_factorial(x):
            if x == 1:
                return 1
            else:
                return x * recursive_factorial(x - 1)

        return recursive_factorial(n)

    # Example usage
    result = factorial(5)
    print(result)  # Output: 120
    ```

## 6. Lambda Functions (Bonus Challenge)

- **Challenge:** Explore lambda functions as a concise way to write anonymous functions for simple operations. Write a program that uses a lambda function to calculate the square of a number.

    ```python
    # Lambda function to calculate the square of a number
    square = lambda x: x ** 2

    # Example usage
    result = square(4)
    print(result)  # Output: 16
    ```
