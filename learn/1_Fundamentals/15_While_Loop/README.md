# while loop

A while loop is a control flow statement that allows a block of code to be executed repeatedly as long as a specified condition is true.

```py
count = 1

while count <= 5:
    print(count)
    count += 1
```

---

## Exercise

## 1. Guessing Game

- **Challenge:** Develop a program that lets a user guess a secret number.
- **Functionality:**
  - Define a secret number (or store it in a variable).
  - Use a `while` loop to repeatedly prompt the user for guesses.
  - Inside the loop:
    - Check if the guess is too high, too low, or correct.
    - Provide feedback to the user based on their guess.
  - When the guess is correct, print a congratulatory message.

```py
secret_number = 7  # Define the secret number

while True:
    guess = int(input("Guess the secret number (between 1 and 10): "))

    if guess == secret_number:
        print(f"You've guessed it - congratulations! It's number {secret_number}.")
        break
    elif guess < secret_number:
        print(f"The secret number is greater than {guess}.")
    else:
        print(f"The secret number is less than {guess}.")
```

## 2. Menu-Driven Program (While Loop Version)

- **Challenge:** Rewrite the menu-driven program using a `while` loop.
- **Functionality:**
  - Create a loop that continues until the user chooses to exit.
  - Inside the loop:
    - Display a menu with options (e.g., add, subtract, exit).
    - Use `if` statements to handle different menu options and perform the corresponding actions (add, subtract, etc.).

```py
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

while True:
    print("\nMenu:")
    print("1. Add")
    print("2. Subtract")
    print("3. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The result is: {add(num1, num2)}")
    elif choice == "2":
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        print(f"The result is: {subtract(num1, num2)}")
    elif choice == "3":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")
```

## 3. Countdown Timer

- **Challenge:** Create a program that simulates a countdown timer.
- **Functionality:**
  - Prompt the user to enter a starting time in seconds.
  - Use a `while` loop with a counter variable.
  - Inside the loop:
    - Decrement the counter variable by 1 (simulating one second passing).
    - Print the remaining time.
  - Once the counter reaches 0, print a message like "Time's up!"

**Note:** Functionality like `time.sleep(1)` might not be available in all environments.

```py
import time

# Prompt the user to enter a starting time in seconds
starting_time = int(input("Enter the starting time in seconds: "))

# Initialize the counter variable
counter = starting_time

# Use a while loop with a counter variable
while counter > 0:
    print(f"Time remaining: {counter} seconds")
    time.sleep(1)  # Simulate one second passing
    counter -= 1

# Once the counter reaches 0, print a message
print("Time's up!")
```
