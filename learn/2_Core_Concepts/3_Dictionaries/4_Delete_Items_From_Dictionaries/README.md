# Deleting In Dictionaries

We can delete items from dictionaries using the del statement or the pop() method.

## del Statement

```py
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
del my_dict['age']

# Output: {'name': 'John', 'city': 'New York'}
```

## pop() Method

```py
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
my_dict.pop('age')

# Output: {'name': 'John', 'city': 'New York'}
```

## popitem() Method

```py
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
my_dict.popitem() # last item delete

# Output: {'name': 'John', 'age': 25}
```

## clear() Method to Remove All Items

```py
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
my_dict.clear()

# Output: {}
```
