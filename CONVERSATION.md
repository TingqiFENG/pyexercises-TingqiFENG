# Conversation with the AI

Written automatically by `tutor.py`. Add your own notes under any entry: what you tried, what broke, what you changed. Those notes are what is graded.

---
## 2026-10-07 12:06, in .

**Me:** how to print a statement in python

**Tutor:**

Printing a statement in Python is done with the `print()` function.

```python
# Print a single statement
print("Hello, world!")
```

What is the argument inside the parentheses of the `print()` function?

---
## 2026-10-07 15:16, in .

**Me:** how to add an item in a dictionary

**Tutor:**

Assigning a value to a new key adds an item to a dictionary.

```python
# TODO: add the key 'price' with value 19.99 to the dict below
product = {'name': 'laptop', 'stock': 10}
```

What function or operation do you use to add a new key–value pair to a dictionary?

---
## 2026-10-07 15:20, in .

**Me:** how to add an item in a dictionary

**Tutor:**

Assigning a new key-value pair to a dictionary is called **adding an item**.

```python
# TODO: create an empty dictionary
sales = {}

# TODO: add one item with key 'tshirt' and value 19.99
sales['tshirt'] = 19.99

# TODO: add another item with key 'mug' and value 7.50
sales['mug'] = 7.50
```

What is the syntax to add an item whose key is `'hat'` and value is `24.00`?

---
## 2026-10-07 21:27, in .

**Me:** how to add num in python

**Tutor:**

Concept: Adding two numbers in Python using the `+` operator.

Pattern:
```python
# TODO: replace a and b with your numbers
a = 5
b = 3
result = a + b
print(result)
```

Question: Which operator is used to add two numbers in Python?

---
## 2026-10-07 22:02, in .

**Me:** What is the difference between sorted() and .sort() in Python? Which one modifies the original list?

**Tutor:**

The difference is whether the list is changed in place or a new list is returned.

```python
# sorted() returns a new sorted list
new_list = sorted(old_list)

# .sort() modifies the original list in place and returns None
old_list.sort()
```

Which function returns a new list instead of changing the original?

---
## 2026-10-07 22:03, in .

**Me:** What is the difference between reversed() and .reverse() in Python? Which one modifies the original list?

**Tutor:**

**Reversing sequences in Python**

`reversed()` is a built-in function that returns an iterator walking the sequence **backwards**; it never changes the original sequence.
`.reverse()` is a method of **lists** that reverses the list **in place** and returns `None`.

Pattern on a toy list:

```python
data = [10, 20, 30, 40]

# reversed() keeps the original list intact
backwards = reversed(data)   # TODO: what type is backwards?

# .reverse() changes data itself
data.reverse()               # TODO: what is the return value of this call?
```

Which built-in function/method reverses a tuple?

---
## 2026-10-07 22:03, in .

**Me:** How can I display a list in reverse order without modifying the original list?

**Tutor:**

Reversing a list without changing it is done with slicing.

```python
def show_reversed(items):
    # TODO: return a new list that is the reverse of items
    # hint: use slicing with [::-1]
    pass

# Example
toys = ["doll", "car", "ball"]
print(show_reversed(toys))  # should print ['ball', 'car', 'doll']
print(toys)                 # should still print ['doll', 'car', 'ball']
```

Which built-in sequence operation gives the slice step that reverses the order?

---
## 2026-10-07 22:04, in .

**Me:** For this exercise, what should I explain in the four comments at the top of my Python file?

**Tutor:**

Refused, off topic.
