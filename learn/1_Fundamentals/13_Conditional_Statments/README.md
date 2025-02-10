# Conditional Statements

Conditional statements are used to control the flow of a program based on certain conditions. They allow you to execute different blocks of code depending on whether a specified condition evaluates to True or False

## if Statement

The if statement is used to execute a block of code only if a specified condition is True

```py
x = 10

if x > 5:
    print("x is greater than 5")
```

## if-else Statement

The if-else statement allows you to specify two blocks of code: one to be executed if the condition is True, and another if the condition is False.

```py
x = 3

if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
```

## if-elif-else Statement

The if-elif-else statement allows you to check multiple conditions sequentially. It executes the block of code associated with the first condition that is True.

```py
x = 0

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```

---

## Ternary Operators

Ternary operators include conditional expressions in Python. Conditional expressions are a form of expression that aims to evaluate conditions and return values ​​based on the evaluation results. You can assume that these ternary operators are one-liner versions of if and else.

```py
lulus = True
print("selamat") if lulus else print("perbaiki") # selamat
```

## Ternary Tuples

The program code above displays the text message "Selamat, Anda lulus!" if the condition evaluates to true and displays the text message  "Perbaiki, Anda belum lulus." if the condition evaluates to false.

```py
lulus = True
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus]
print(kelulusan) # Selamat, Anda lulus!
```

---

## Challenges

## Challenge 1: Simple if Statement

Prompt:

- Write a program that prompts the user to enter a number.

Task:

- Use an if statement to check if the number is even.
- If it's even, print "The number is even."
- Otherwise, print nothing or an alternative message.

Hint:

- Use the modulo operator (`%`) to check for remainder after division by 2.

  ```py
  number = input("Enter a number: ")

  if int(number) % 2 == 0:
      print("The number is even")
  else:
      print("The number is odd")
  ```

## Challenge 2: if-else for Binary Classification

Prompt:

- Write a program that prompts the user to enter a letter grade ('A', 'B', 'C', 'D', or 'F').

Task:

- Use an if-else statement to classify the grade:
  - If the grade is 'A', 'B', or 'C', print "Passing grade."
  - Otherwise, print "Failing grade."

  ```py
  grade = input("Enter your grade (A, B, C, D, or F): ")

  if grade == "A" or grade == "B" or grade == "C":
      print("Passing grade")
  else:
      print("Failing grade")
  ```

## Challenge 3: elif for Multi-Way Decisions

Prompt:

- Write a program that prompts the user to enter a day of the week (e.g., "Monday").

Task:

- Use an if-elif-else chain to categorize the day:
  - If it's "Saturday" or "Sunday", print "Weekend."
  - Otherwise, check for weekdays ("Monday", "Tuesday", etc.) and print "Weekday."
  - If none of the above conditions match, print "Invalid day entered."

  ```py
  day_of_week = input("Enter the day of the week: ")

  if day_of_week == "Saturday" or day_of_week == "Sunday":
      print("It's the weekend")
  elif (
      day_of_week == "Monday"
      or day_of_week == "Tuesday"
      or day_of_week == "Wednesday"
      or day_of_week == "Thursday"
      or day_of_week == "Friday"
  ):
      print("It's a weekday")
  else:
      print("Invalid day of the week")
  ```
