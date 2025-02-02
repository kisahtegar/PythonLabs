# Loops?

Loops allow us to repeatedly execute a block of code as long as a certain condition is met or iterate over a sequence of elements. Python supports two main types of loops: for loops and while loops.

## for loop

A for loop is used to iterate over a sequence (such as a list, tuple, string, or other iterable objects) and execute a block of code for each element in the sequence.

## range

range is a built-in function that generates a sequence of numbers within a specified range. It is commonly used with for loops to iterate over a sequence of numbers.

```py
for i in range(5):
    print(i)
```

## range(start, stop)

```py
for i in range(2, 8):
    print(i)
```

## range(start, stop, step)

range(1, 10, 2): This creates a sequence of numbers starting from 1 up to (but not including) 10, with a step of 2. So, the sequence generated is [1, 3, 5, 7, 9]

```py
for i in range(1, 10, 2):
    print(i)
```

---

## Challenge

## Challenge 1: Printing Numbers (1 to 10)

Write a program that uses a for loop and range() to print the numbers from 1 to 10 (inclusive).

```py
for i in range(1, 11):
    print(i)
```

## Challenge 2: Counting Down (10 to 1)

Write a program that uses a for loop and range() to print the numbers from 10 down to 1 (in descending order).

```py
for i in range(10, 0, -1):
    print(i)
```

## Challenge 3: Even Numbers Only (1 to 10)

Write a program that uses a for loop and range() to print only the even numbers between 1 and 10 (inclusive). (Hint: use the modulo operator % to check for evenness).

```py
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

## Challenge 4: Sum of Numbers (1 to 100)

Write a program that uses a for loop and range() to calculate the sum of all numbers from 1 to 100 (inclusive).

```py
total = 0
for i in range(1, 101):
    total += i
print(total)
```
