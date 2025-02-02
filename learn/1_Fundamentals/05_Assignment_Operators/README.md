# Assignment Operators

## Assignment (=)

The basic assignment operator assigns the value on the right side to the variable on the left side.

```py
    x = 10  # Assigns the value 10 to the variable x
```

## Addition Assignment (+=)

Adds the value on the right to the current value of the variable on the left and assigns the result to the variable.

```py
    x += 5  # Equivalent to x = x + 5
```

## Subtraction Assignment (-=)

Subtracts the value on the right from the current value of the variable on the left and assigns the result to the variable.

```py
y = 20
y -= 3  # Equivalent to y = y - 3
```

## Multiplication Assignment (\*=)

Multiplies the current value of the variable on the left by the value on the right and assigns the result to the variable.

```py
z = 5
z *= 2  # Equivalent to z = z * 2
```

## Division Assignment (/=)

Divides the current value of the variable on the left by the value on the right and assigns the result to the variable.

```py
a = 8
a /= 4  # Equivalent to a = a / 4
```

## Floor Division Assignment (//=)

Performs floor division on the current value of the variable on the left by the value on the right and assigns the result to the variable.

```py
b = 17
b //= 3  # Equivalent to b = b // 3
```

## Exponentiation Assignment (\*\*=)

Performs floor division on the current value of the variable on the left by the value on the right and assigns the result to the variable.

```py
c = 2
c **= 3  # Equivalent to c = c ** 3
```

## Modulus Assignment (%=)

Computes the modulus of the current value of the variable on the left divided by the value on the right and assigns the result to the variable.

```py
d = 10
d %= 3  # Equivalent to d = d % 3
```

---

## Challenge

## Challenge 1: Shorthand Updates

**Objective:** Utilize shorthand assignment operators to modify a variable's value.

**Steps:**

1. Initialize a variable named `count` with a value of 5.
2. **Add 3:** Update `count` by adding 3 using the `+=` operator. Print the new value.
3. **Subtract 2:** Update `count` by subtracting 2 using the `-=` operator. Print the new value.
4. **Multiply by 4:** Update `count` by multiplying it by 4 using the `*=` operator. Print the new value.
5. **Divide by 2:** Update `count` by dividing it by 2 using the `/=` operator. Print the new value.

    ```py
    count = 5
    count += 3
    count -= 2
    count *= 4
    count /= 2

    print(count)  # 12
    ```

## Challenge 2: Increment and Decrement

**Objective:** Explore the increment (++) and decrement (--) operators.

**Steps:**

1. Initialize two variables: `x` with a value of 10 and `y` with a value of 20.
2. **Increment x:** Increase `x` by 5 using the `x += 5` operator (equivalent to `x = x + 5`). Print the updated value of `x`.
3. **Decrement y:** Decrease `y` by 3 using the `y -= 3` operator (equivalent to `y = y - 3`). Print the updated value of `y`.

    ```py
    x = 10
    y = 20

    x += 5
    y -= 3

    print(x)  # 15
    print(y)  # 17
    ```

## Challenge 3: Combining Operations

**Objective:** Perform calculations and update variables in a single line using combined assignment operators.

**Steps:**

1. Initialize a variable named `total` with a value of 100.
2. Set the cost of two items: `item1 = 25` and `item2 = 30`.
3. **Update total:** Subtract the combined cost of both items from `total` in a single line using the `-=` operator: `total -= item1 + item2`. Print the remaining balance in `total`.

    ```py
    total = 100
    item1 = 25
    item2 = 30

    total -= item1 + item2

    print(total)  # 45
    ```

## Challenge 4: Augmented Assignment with Strings

**Objective:** Modify strings using the `+=` operator for concatenation.

**Steps:**

1. Initialize a variable named `message` with the value "Hello".
2. **Concatenate string:** Append " World!" to the end of `message` using the `+=` operator: `message += " World!"`. Print the final message.

    ```py
    message = "Hello"
    message += " World! "

    print(message)  # Hello World!"
    ```
