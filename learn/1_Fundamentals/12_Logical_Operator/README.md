# Logical Operators

Logical operators are used to perform logical operations on boolean values. These operators allow you to combine or modify boolean values and make more complex decisions in your code.

## Logical AND (and)

The and operator returns True if both conditions on its left and right are True. Otherwise, it returns False.

```py
x = True
y = False
result = x and y  # Result is False
```

## Logical OR (or)

The or operator returns True if at least one of the conditions on its left or right is True. If both conditions are False, it returns False.

```py
x = True
y = False
result = x or y  # Result is True
```

## Logical NOT (not)

The not operator negates the boolean value. If the condition is True, it returns False. If the condition is False, it returns True.

```py
x = True
result = not x  # Result is False
```

---
## Challenge

## Challenge 1: Scholarship Eligibility

- Write a program that prompts the user for their age and grade (as a number).
- Use `and` to check if they are at least 18 years old (`age >= 18`) and have a passing grade (e.g., `grade >= 60`).
- Print messages based on eligibility:
  - If both conditions are met: "Eligible for scholarship!"
  - Otherwise, specify which condition(s) they need to meet (e.g., "Not old enough" or "Grade not high enough").

  ```py
  age = input("Enter your age: ")
  grade = input("Enter your grade: ")
  result = (int(age) > 18) and (int(grade) >= 60)

  if result:
      print("You are eligible")
  else:
      print("You are not eligible")
  ```

## Challenge 2: Discount with Membership or Coupon

- Write a program that simulates a discount scenario.
- Use `or` to check if the customer has a membership (`has_membership = True`) or a valid coupon (`has_coupon = "valid"`).
- Apply a discount (e.g., 10%) to the original price if either condition is met.
- Print the final price with or without the discount.

  ```py
  price = input("Enter the price: ")
  membership = input("Do you have membership? (yes/no): ")
  coupon = input("Do you have coupon? (yes/no): ")

  if (membership == "yes") or (coupon == "yes"):
      result = price * 0.10
  else:
      result = price * 0.10

  print(result)
  ```

## Challenge 3: Weekday Check with Negation

- Write a program that prompts the user to enter a day of the week (e.g., "Monday").
- Use `not` to check if it's not the weekend (weekend days are "Saturday" or "Sunday").
- Print messages based on the day:
  - If it's not the weekend: "It's a weekday!"
  - Otherwise: "It's the weekend!"

  ```py
  day_of_week = input("Enter the day of the week: ")

  if day_of_week not in ["Saturday", "Sunday"]:
      print("It's a weekday")
  else:
      print("It's a weekend")
  ```

## Challenge 4: Login with Combined Conditions

- Write a program that prompts the user for a username and password.
- Use a combination of `and` and `not` to check:
  - Username is correct (`correct_username = "user123"`)
  - Password is not empty (`password != ""`)
- Print messages based on login attempt:
  - If both conditions are met: "Login successful!"
  - Otherwise, specify the issue (e.g., "Incorrect username" or "Empty password").

  ```py
  # Correct username
  correct_username = "user123"

  # Prompt the user for a username and password
  username = input("Enter your username: ")
  password = input("Enter your password: ")

  # Check if the username is correct and the password is not empty
  if (username == correct_username) and (password != ""):
      print("Login successful!")
  else:
      if username != correct_username:
          print("Incorrect username")
      if password == "":
          print("Empty password")
  ```
