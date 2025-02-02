# Strings

A string is a sequence of characters, and it is one of the fundamental data types used to represent textual data.

```py
# Using single quotes
single_quoted_string = 'Hello, World!'

# Using double quotes
double_quoted_string = "Python Programming"

# Multiline string using triple quotes
multiline_string = '''This is a
multiline
string.'''
```

## Concatenation

```py
str1 = "Hello"
str2 = "World"
concatenated_string = str1 + ", " + str2
print(concatenated_string)  # Hello, World
```

## String Length

```py
string = "Python"
length = len(string)
print(length)  # 6
```

## String Indexing and Slicing

```py
text = "Python"
first_char = text[0]     # Accessing the first character
substring = text[1:4]    # Slicing from index 1 to 3
print(first_char, substring)  # P yth
```

## String Methods

```py
sentence = "   Python is fun!   "
uppercase_sentence = sentence.upper()
lowercase_sentence = sentence.lower()
stripped_sentence = sentence.strip()
print(uppercase_sentence, lowercase_sentence, stripped_sentence)
```

## String Formatting

```py
name = "HuXn"
age = 20
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
```

## Escape Characters

```py
escaped_string = "This is a line.\nThis is a new line."
print(escaped_string)
```

---

## Challenge

## Challenge 1: Working with Quotes and Multiline Strings

- Write a program that uses double quotes to store a famous quote.
- Then, write a program that uses triple quotes (either ''' or """) to create a multiline poem or paragraph. Print both the quote and the poem/paragraph.

    ```py
    quote = "The only way to do great work is to love what you do."
    poem = """The woods are lovely, dark and deep,
    But I have promises to keep,
    And miles to go before I sleep."""

    print(quote)
    print(poem)
    ```

## Challenge 2: Concatenation Fun

- Write a program that creates two variables: first_name and last_name. Concatenate them with a space in between to form a full name and print it.

- Then, try a more elaborate concatenation: create a greeting message by combining a string literal with the full name variable.

    ```py
    first_name = "Albert"
    last_name = "Einstein"
    full_name = first_name + " " + last_name
    
    print(full_name)
    print("Good Morning, " + full_name)
    ```

## Challenge 3: String Length Exploration

- Write a program that prompts the user to enter their name and then prints the length of the entered name using the len() function.

    ```py
    user_name = input("Enter username: ")
    print(len(user_name))
    ```

## Challenge 4: Indexing and Slicing Adventures

- Write a program that prompts the user to enter a word and then prints the first and last characters of the word using indexing (e.g., word[0] for first character).

- Next, modify the program to extract a substring using slicing. Prompt the user for the starting and ending indices (consider using int() to convert input to integers) and print the extracted substring.

    ```py
    word_today = input("Enter a word: ")
    word_first = word_today[0]
    word_last = word_today[-1]

    print(word_first, word_last)
    word_substring = word_today[1:-1]
    print(word_substring)
    ```

## Challenge 5: Case Conversions

- Write a program that prompts the user to enter a sentence. Convert the sentence to uppercase and lowercase using the upper() and lower() methods, and print both versions.

    ```py
    sentence = input("Enter a sentence: ")

    print("Uppercase:", sentence.upper())
    print("Lowercase:", sentence.lower())
    ```

## Challenge 6: Stripping Away Whitespace

- Write a program that prompts the user to enter a sentence with potential leading or trailing spaces. Use the strip() method to remove these spaces and print the trimmed sentence.

    ```py
    sentence = input("Enter a sentence with potential leading or trailing spaces: ")
    print("Trimmed sentence:", sentence.strip())
    ```

## Challenge 7: String Formatting Magic

- Write a program that asks the user for their name, age, and city. Then, use f-strings (formatted string literals) to create a formatted message that introduces the user with their details.

    ```py
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    city = input("Enter your city: ")

    print(f"Hello, my name is {name}. I am {age} years old and I live in {city}.")
    ```
