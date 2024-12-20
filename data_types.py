# Integer (int)

x = 10      # Positive integer
y = -300    # Negative integer
z = 0       # Zero
print(type(x))  # <class 'int'>


# Float (float)

pi = 3.14159
e = 2.7e10   # Scientific notation for 2.7 x 10^10
print(type(pi))  # <class 'float'>


# Complex (complex)

c = 3 + 4j
print(c.real)  # 3.0 (real part)
print(c.imag)  # 4.0 (imaginary part)
print(type(c))  # <class 'complex'>


# Sequence Types
# String (str)

text = "Hello, World!"
print(text[0])       # 'H' (indexing)
print(text[-1])      # '!' (negative indexing)
print(text[0:5])     # 'Hello' (slicing)
print(type(text))    # <class 'str'>


# List (list)

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add an item
print(fruits[1])         # 'banana'
fruits[0] = "kiwi"       # Modify an item
print(fruits)            # ['kiwi', 'banana', 'cherry', 'orange']


# Tuple (tuple)

coordinates = (10, 20)
print(coordinates[0])   # 10
# coordinates[0] = 15  # TypeError: 'tuple' object does not support item assignment


# Range (range)

nums = range(5)         # Creates 0, 1, 2, 3, 4
nums = range(1, 10, 2)  # Creates 1, 3, 5, 7, 9 (start, stop, step)
for n in nums:
    print(n)


# Mapping Data Types

# Dictionary (dict)

person = {"name": "Alice", "age": 25}
print(person["name"])   # 'Alice'
person["age"] = 30      # Update value
person["city"] = "Paris"  # Add new key-value pair
print(person)           # {'name': 'Alice', 'age': 30, 'city': 'Paris'}

# Set Data Types
# Set (set)
colors = {"red", "green", "blue"}
colors.add("yellow")   # Add an item
colors.remove("red")   # Remove an item
print(colors)          # {'green', 'yellow', 'blue'}

# Frozenset (frozenset)
immutable_set = frozenset(["red", "green", "blue"])
# immutable_set.add("yellow")  # AttributeError: 'frozenset' object has no attribute 'add'

# Boolean Type (bool)
is_happy = True
print(type(is_happy))  # <class 'bool'>
print(10 > 5)          # True


# Binary Types

# Bytes (bytes)
b = b"hello"
print(b[0])       # 104 (ASCII value of 'h')


# Bytearray (bytearray)
ba = bytearray(b"hello")
ba[0] = 72   # Modify to 'H'
print(ba)    # b'Hello'


# Memoryview (memoryview)
mv = memoryview(b"hello")
print(mv[0])  # 104

# None Type (NoneType)
x = None
print(x is None)  # True
