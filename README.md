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
