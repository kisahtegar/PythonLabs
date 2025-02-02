# Exercise

## Challenge 1: Creating Dictionaries

- **Using curly braces {}:** Create a dictionary to store phone numbers for friends (key: name, value: phone number).

    ```python
    phone_numbers = {
        "Alice": "123-456-7890",
        "Bob": "234-567-8901",
        "Charlie": "345-678-9012"
    }
    print(phone_numbers)
    ```

- **Using the dict() function:** Create a dictionary from a list of key-value pairs (e.g., `dict([("apple", "fruit"), ("ball", "toy")])`).

    ```python
    items = dict([("apple", "fruit"), ("ball", "toy"), ("car", "vehicle")])
    print(items)
    ```

## Challenge 2: Accessing Dictionary Values by Key

- Create a dictionary to store movie information (title, director, year).

    ```python
    movie_info = {
        "title": "Inception",
        "director": "Christopher Nolan",
        "year": 2010
    }
    ```

- Access specific values using their keys (e.g., print the title and director of a movie).

    ```python
    print(f"Title: {movie_info['title']}")
    print(f"Director: {movie_info['director']}")
    ```

## Challenge 3: Adding and Updating Key-Value Pairs

- Create a dictionary to store student grades (name: grade).

    ```python
    student_grades = {
        "Alice": "A",
        "Bob": "B"
    }
    ```

- Add a new student and their grade to the dictionary.

    ```python
    student_grades["Charlie"] = "C"
    print(student_grades)
    ```

- Update an existing student's grade in the dictionary.

    ```python
    student_grades["Bob"] = "A"
    print(student_grades)
    ```

## Challenge 4: Removing Key-Value Pairs

- Create a dictionary to store shopping cart items (item: quantity).

    ```python
    shopping_cart = {
        "apple": 3,
        "banana": 2,
        "cherry": 5
    }
    ```

- Remove an item from the cart using the `del` keyword.

    ```python
    del shopping_cart["banana"]
    print(shopping_cart)
    ```

## Challenge 5: Checking for Keys and Avoiding Errors

- Write a program that checks if a specific key exists in a dictionary before accessing its value.

    ```python
    phone_book = {
        "Alice": "123-456-7890",
        "Bob": "234-567-8901"
    }
    
    key_to_check = "Charlie"
    
    # Using the in operator
    if key_to_check in phone_book:
        print(f"{key_to_check}'s phone number is {phone_book[key_to_check]}")
    else:
        print(f"{key_to_check} is not in the phone book.")
    
    # Using the get() method
    phone_number = phone_book.get(key_to_check)
    if phone_number:
        print(f"{key_to_check}'s phone number is {phone_number}")
    else:
        print(f"{key_to_check} is not in the phone book.")
    ```

## Challenge 6: Iterating Over Dictionaries

- Create a dictionary to store employee information (name: department).

    ```python
    employees = {
        "Alice": "HR",
        "Bob": "Engineering",
        "Charlie": "Marketing"
    }
    ```

- Iterate through the dictionary using a for loop to print both the names and departments.

    ```python
    for name, department in employees.items():
        print(f"Name: {name}, Department: {department}")
    ```

- Try iterating over keys, values, and key-value pairs separately using different methods (e.g., `keys()`, `values()`, `items()`).

    ```python
    # Iterating over keys
    for name in employees.keys():
        print(f"Name: {name}")
    
    # Iterating over values
    for department in employees.values():
        print(f"Department: {department}")
    
    # Iterating over key-value pairs
    for name, department in employees.items():
        print(f"Name: {name}, Department: {department}")
    ```

## Challenge 7: Nested Dictionaries

- Create a dictionary to store customer information (key: customer ID, value: another dictionary with details like name, address, phone number).

    ```python
    customers = {
        1: {"name": "Alice", "address": "123 Main St", "phone": "123-456-7890"},
        2: {"name": "Bob", "address": "456 Elm St", "phone": "234-567-8901"}
    }
    ```

- Access nested elements using appropriate indexing with keys.

    ```python
    customer_id = 1
    customer_info = customers.get(customer_id)
    
    if customer_info:
        print(f"Customer ID: {customer_id}")
        print(f"Name: {customer_info['name']}")
        print(f"Address: {customer_info['address']}")
        print(f"Phone: {customer_info['phone']}")
    else:
        print(f"Customer ID {customer_id} not found.")
    ```
