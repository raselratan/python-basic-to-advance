# Example of variable assignments
x = 10        # Integer
name = "Rasel Mahmud"  # String
pi = 3.14     # Float
is_valid = True  # Boolean

print(x)
print(name)
print(pi)
print(is_valid)

# Assigning the same value to multiple variables
a = b = c = 5

print(a)
print(b)
print(c)

# Assigning different values to multiple variables in one line
p, q, r = 1, 2, "Hello"

print(p)
print(q)
print(r)

print(type(p))    # Output: <class 'int'>
print(type(q))    # Output: <class 'int'>
print(type(r))    # Output: <class 'str'>

# Variable scopes
x = "global"


def my_function():
    x = "local"  # Local variable
    print(x)     # Prints "local"


my_function()
print(x)         # Prints "global"
