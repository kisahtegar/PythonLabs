# Identifier

Identifier is a name given to entities like variables, functions, classes, modules, etc. It helps to uniquely identify these entities in the program

## Rules Of Identifier

- It must start with a letter (a-z, A-Z) or an underscore (\_)
- The remaining characters can be letters, underscores, or digits (0-9)
- Python is case-sensitive, so variable and Variable are different identifiers
- Reserved keywords are not allowed

## Conventions for Naming Identifiers

- Use descriptive names to make the code more readable
- Avoid using names that are too short or too cryptic
- Use underscores to separate words in a multi-word identifier (snake_case). For example, my_variable
- For constants, use all capital letters with underscores separating words (UPPER_CASE). For example, MAX_SIZE

```python
# Variable Naming

# - Case Sensitivity
password = 12345
# PASSWORD = 54321 ❌
# print(password)

# Reserved Words ❌
# while = 20
# print(while)

# Underscores
user_password = 20
print(user_password)
```
