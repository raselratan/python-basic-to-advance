# Python Basic to advance Series

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a></li>
    <li><a href="#hello-world">Hello World</a></li>
    <li>
        <a href="#comments">Comments</a>
        <ul>
            <li><a href="#single-line-comment">Single Line Comment</a></li>
            <li><a href="#multi-line-comment">Multi Line Comment</a></li>
            <li><a href="#best-practices-for-comments">Best Practices for Comments</a></li>
        </ul>
    </li>
    <li>
      <a href="#variables">Variables</a>
      <ul>
            <li><a href="#rules">Rules for Naming Variables</a></li>
            <li><a href="#value-assign">Assigning Values to Variables</a></li>
            <li><a href="#multiple-assignment">Multiple Assignment</a></li>
            <li><a href="#checking-types">Checking Variable Types</a></li>
            <li><a href="#variable-scope">Variable Scope</a></li>
        </ul>
    </li>
    <li>
      <a href="#data-types">Data Types</a>
      <ul>
            <li><a href="#rules">Rules for Naming Variables</a></li>
            <li><a href="#value-assign">Assigning Values to Variables</a></li>
            <li><a href="#multiple-assignment">Multiple Assignment</a></li>
            <li><a href="#checking-types">Checking Variable Types</a></li>
            <li><a href="#variable-scope">Variable Scope</a></li>
        </ul>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project

This project is for learnig python from scratch.

<!-- Hello World -->

## Hello World

This code will print the Hello World!, 5 and 1001.532. Here print() function can print data of all types in Python because it converts the input to a string using the str() function internally before displaying it. In essence, print() can handle all data types.

```sh
print("Hello World!")
print(5)
print(1001.532)
```

<!-- Comments -->

## Comments

In Python, comments are used to add explanatory notes or annotations in the code, making it more understandable for developers. Comments are ignored by the Python interpreter during execution.

<!-- Single Line Comment -->

## Single Line Comment

- Begin with a # symbol.
- Everything after # on that line is treated as a comment.

# Example

```sh
# This is a single-line comment
print("Hello, World!")  # This prints a message
```

<!-- Single Line Comment -->

## Multi Line Comment

a. Consecutive Single-Line Comments

- Use multiple # symbols for each line.

# Example

```sh
# This is a multi-line comment
# Each line starts with a hash symbol
# Describing the following code
print("Multi-line comments example")
```

b. Triple-Quoted Strings

- Triple single (''') or double quotes (""") can act as a comment block if not assigned to a variable or used in a function.

# Example

```sh
'''
This is a multi-line comment
using triple single quotes.
'''
print("Triple-quoted comments example")

"""
This is another multi-line comment
using triple double quotes.
"""
print("Another example of triple quotes")
```

# Note:

While triple quotes can be used for multi-line comments, their primary purpose is for documentation strings (docstrings) in functions, classes, and modules.

<!-- Best Practices for Comments -->

## Best Practices for Comments

- Be Clear and Concise: Write comments to explain "why," not "what."
- Keep Comments Updated: Ensure comments remain relevant as the code evolves.
- Avoid Overusing Comments: Use comments where necessary; rely on clear and descriptive code wherever possible.

# Example of Good Comments:

```sh
# Calculate the area of a rectangle
length = 10  # Length of the rectangle
width = 5    # Width of the rectangle
area = length * width  # Area formula: length * width
print(area)
```

<!-- Variables -->

## Variables

In Python, a variable is used to store data or information that can be referenced and manipulated later in the program. Python variables are created when you assign a value to them, and they do not require explicit declaration of their data type—Python infers the type based on the value assigned.

<!-- Rules -->

## Rules

- Must begin with a letter (a-z, A-Z) or an underscore (\_).
- Subsequent characters can include letters, numbers (0-9), or underscores.
- Cannot be a reserved keyword (e.g., if, for, while, etc.).
- Case-sensitive: myVariable and myvariable are different.

<!-- Value Assign -->

## Value Assign

```sh
# Example of variable assignments
x = 10        # Integer
name = "John" # String
pi = 3.14     # Float
is_valid = True # Boolean
```

<!-- Multiple Assignment -->

## Multiple Assignment

```sh
# Assigning the same value to multiple variables
a = b = c = 5

# Assigning different values to multiple variables in one line
x, y, z = 1, 2, "Hello"
```

<!-- Checking Types -->

## Checking Types

```sh
print(type(x))    # Output: <class 'int'>
print(type(name)) # Output: <class 'str'>
```

<!-- Variable Scope -->

## Variable Scope

- Global Variable: Declared outside of functions and accessible globally.
- Local Variable: Declared inside a function and only accessible within that function.

# Example

```sh
x = "global"

def my_function():
    x = "local"  # Local variable
    print(x)     # Prints "local"

my_function()
print(x)         # Prints "global"
```

<!-- Data Types -->

## Data Types

In Python, a variable is used to store data or information that can be referenced and manipulated later in the program. Python variables are created when you assign a value to them, and they do not require explicit declaration of their data type—Python infers the type based on the value assigned.

1.  Numeric Data Types
    Numeric data types represent numbers in various forms.

    - Integer (int)

      - Represents whole numbers (positive, negative, or zero).
      - No size limitation (can handle very large numbers).

      # Example

      ```sh
      x = 10      # Positive integer
      y = -300    # Negative integer
      z = 0       # Zero
      print(type(x))  # <class 'int'>
      ```

    - Float (float)

      - Represents numbers with a decimal point.
      - Can handle scientific notation

      # Example

      ```sh
      pi = 3.14159
      e = 2.7e10   # Scientific notation for 2.7 x 10^10
      print(type(pi))  # <class 'float'>
      ```

    - Complex (complex)

      - Represents complex numbers in the form a + bj, where a is the real part and b is the imaginary part.

      # Example

      ```sh
      c = 3 + 4j
      print(c.real)  # 3.0 (real part)
      print(c.imag)  # 4.0 (imaginary part)
      print(type(c)) # <class 'complex'>
      ```

2.  Sequence Data Types
    Sequence data types store collections of data in a specific order.

        - String (str)

          - Represents textual data.
          - Enclosed in single, double, or triple quotes.
          - Immutable (cannot be changed after creation).

    # Example

          ```sh
          text = "Hello, World!"
          print(text[0])       # 'H' (indexing)
          print(text[-1])      # '!' (negative indexing)
          print(text[0:5])     # 'Hello' (slicing)
          print(type(text))    # <class 'str'>
          ```

        - List (list)

               - Ordered and mutable collection of items.
               - Can contain elements of different data types.

    # Example

              ```sh
              fruits = ["apple", "banana", "cherry"]
              fruits.append("orange") # Add an item
              print(fruits[1]) # 'banana'
              fruits[0] = "kiwi" # Modify an item
              print(fruits) # ['kiwi', 'banana', 'cherry', 'orange']
              ```

        - Tuple (tuple)

               - Ordered and immutable collection of items.
               - Often used to store fixed data that should not be changed.

    # Example

              ```sh
              coordinates = (10, 20)
              print(coordinates[0]) # 10
              # coordinates[0] = 15 # TypeError: 'tuple' object does not support item assignment
              ```

        - Range (range)

               - Represents a sequence of numbers.
               - Typically used in loops.

    # Example

              ```sh
              nums = range(5)         # Creates 0, 1, 2, 3, 4
              nums = range(1, 10, 2)  # Creates 1, 3, 5, 7, 9 (start, stop, step)
              for n in nums:
                  print(n)
              ```

3.  Mapping Data Types

            - Dictionary (dict)

                   - Unordered collection of key-value pairs.
                   - Keys must be unique and immutable (e.g., strings, numbers, tuples).

    # Example

                  ```sh
                  person = {"name": "Alice", "age": 25}
                  print(person["name"]) # 'Alice'
                  person["age"] = 30 # Update value
                  person["city"] = "Paris" # Add new key-value pair
                  print(person) # {'name': 'Alice', 'age': 30, 'city': 'Paris'}
                  ```

4.  Set Data Types
    Set types represent collections of unique and unordered items.

                    -  Set (set)

                           - Mutable, unordered collection of unique items.

    # Example

                        ```sh
                        colors = {"red", "green", "blue"}
                        colors.add("yellow") # Add an item
                        colors.remove("red") # Remove an item
                        print(colors) # {'green', 'yellow', 'blue'}
                        ```

                    -  Frozenset (frozenset)

                           - Immutable version of a set.

    # Example

                        ```sh
                        immutable_set = frozenset(["red", "green", "blue"])
                        # immutable_set.add("yellow") # AttributeError: 'frozenset' object has no attribute 'add'
                         ```

5.  Boolean Type (bool)

    - Represents logical values True or False.

    # Example

                        ```sh
                        is_happy = True
                        print(type(is_happy)) # <class 'bool'>
                        print(10 > 5) # True
                          ```

6.  Binary Types
    These are used for binary data manipulation.

                - Bytes (bytes)
                  - Immutable sequence of bytes.

    # Example

                      ```sh
                      b = b"hello"
                      print(b[0]) # 104 (ASCII value of 'h')
                      ```

                - Bytearray (bytearray)
                  - Mutable sequence of bytes.

    # Example

                      ```sh
                      ba = bytearray(b"hello")
                      ba[0] = 72 # Modify to 'H'
                      print(ba) # b'Hello'
                      ```

                - Memoryview (memoryview)
                  - Provides a view object of binary data.

    # Example

                      ```sh
                      mv = memoryview(b"hello")
                      print(mv[0]) # 104
                      ```

7.  None Type (NoneType)
    Represents the absence of a value.

    # Example

                  ```sh
                  x = None
                  print(x is None) # True
                  ```
