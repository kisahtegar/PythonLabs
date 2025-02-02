# Sets?

A set is an unordered collection of unique elements. Sets are defined by enclosing a comma-separated sequence of values in curly braces {}. Unlike lists or tuples, sets do not allow duplicate elements, and the order of elements is not guaranteed.

## Example of set

```py
my_set = {1, 2, 3, 4, 5}
```

## We can also create a set from a list using the set() constructor

```py
my_list = [1, 2, 2, 3, 4, 4, 5]
converted_set = set(my_list)
print(converted_set)  # Output: {1, 2, 3, 4, 5}
```

---

## Exercise

## Challenge 1: Creating Sets

- **Using curly braces {}:** Create a set of your favorite hobbies.

    ```python
    favorite_hobbies = {"reading", "coding", "hiking"}
    print(favorite_hobbies)
    ```

- **Using the set() function:** Create a set from a list containing duplicate elements (e.g., `set([1, 1, 2, 3])` will remove duplicates).

    ```python
    numbers_list = [1, 1, 2, 3, 3, 4]
    unique_numbers = set(numbers_list)
    print(unique_numbers)  # Output: {1, 2, 3, 4}
    ```

## Challenge 2: Set Membership and Checking for Uniqueness

- Create a set of numbers.

    ```python
    numbers_set = {1, 2, 3, 4, 5}
    ```

- Check if a specific number is present in the set using the `in` operator.

    ```python
    number_to_check = 3
    if number_to_check in numbers_set:
        print(f"{number_to_check} is in the set.")
    else:
        print(f"{number_to_check} is not in the set.")
    ```

- Try adding a duplicate element to the set and observe that it's not included (sets cannot have duplicates).

    ```python
    numbers_set.add(3)  # Adding a duplicate element
    print(numbers_set)  # Output: {1, 2, 3, 4, 5}
    ```

## Challenge 3: Set Operations: Union, Intersection, Difference

- Create two sets: one representing movies you've watched and another representing your friend's watched movies.

    ```python
    my_movies = {"Inception", "The Matrix", "Interstellar"}
    friend_movies = {"The Matrix", "Avatar", "Titanic"}
    ```

- Use the following set operations to find:
  - **Union:** The movies watched by either you or your friend.

    ```python
    all_movies = my_movies.union(friend_movies)
    print(f"Movies watched by either of us: {all_movies}")
    ```

  - **Intersection:** The movies you both have watched.

    ```python
    common_movies = my_movies.intersection(friend_movies)
    print(f"Movies we both have watched: {common_movies}")
    ```

  - **Difference:** The movies you've watched that your friend hasn't and vice versa (use appropriate methods like `union()`, `intersection()`, and `difference()`).

    ```python
    my_unique_movies = my_movies.difference(friend_movies)
    friend_unique_movies = friend_movies.difference(my_movies)
    print(f"Movies I've watched but my friend hasn't: {my_unique_movies}")
    print(f"Movies my friend has watched but I haven't: {friend_unique_movies}")
    ```

## Challenge 4: Adding and Removing Elements from Sets

- Create a set of fruits.

    ```python
    fruits = {"apple", "banana", "cherry"}
    ```

- Add a new fruit to the set using the `add()` method.

    ```python
    fruits.add("orange")
    print(f"Fruits after adding orange: {fruits}")
    ```

- Remove a specific fruit from the set using the `remove()` method.

    ```python
    fruits.remove("banana")
    print(f"Fruits after removing banana: {fruits}")
    ```

- (Optional) Try removing an element that's not in the set using `discard()` (which won't cause an error).

    ```python
    fruits.discard("pineapple")
    print(f"Fruits after discarding pineapple (not in set): {fruits}")
    ```
