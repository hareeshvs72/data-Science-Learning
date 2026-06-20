# 🐍 Python Learning Journey — Day 1

## 📅 Day 1: Basics of Python

Today I started my Python learning journey and covered the fundamentals required to build simple programs.

---

## ✅ Topics Learned

### 🔹 Environment Setup

* Installed Python 3.x
* Set up VS Code
* Learned about virtual environments (`venv`)
* Basic understanding of `pip` and `conda`

---

### 🔹 Variables & Data Types

* `int` → Integer values
* `float` → Decimal numbers
* `str` → Text data
* `bool` → True/False values

---

### 🔹 Type Conversion

* Converted data using:

  * `int()`
  * `float()`
  * `str()`

---

### 🔹 Operators

* Arithmetic: `+`, `-`, `*`, `/`, `**`
* Logical basics

---

### 🔹 f-Strings

* Used formatted strings for clean output
* Example:

  ```python
  print(f"Hello {name}")
  ```

---

### 🔹 Conditional Statements

* `if`, `elif`, `else`
* Used for decision making in programs

---

## 💻 Mini Projects Built

### 1️⃣ Age & Greeting Script

* Took user input (name & age)
* Calculated birth year
* Displayed output using f-strings

---

### 2️⃣ BMI Calculator

* Calculated BMI using:

  ```
  BMI = weight / (height ** 2)
  ```
* Categorized:

  * Underweight
  * Normal
  * Overweight
  * Obese

---

### 3️⃣ Basic Calculator

* Performed operations:

  * Addition
  * Subtraction
  * Multiplication
  * Division
* Handled invalid inputs and division by zero

---

## 🚀 Key Takeaways

* Learned how to take user input
* Understood type conversion and calculations
* Built logic using conditions
* Created small real-world programs

---

## 📌 Next Plan (Day 2)

* Loops (`for`, `while`)
* Lists
* More problem-solving

---

✨ Consistency is the goal. Day 1 complete!


# 📘 Day 2 – Python Basics: Conditionals & Loops

## 🚀 Overview

Today focused on building core programming logic using **conditionals** and **loops**, followed by solving practice problems on HackerRank and implementing a mini project.

---

## 🌅 Morning Session – Conditional Logic

### 🔹 Topics Covered

* `if / elif / else` statements
* Comparison operators:

  * `==`, `!=`, `>`, `<`, `>=`, `<=`
* Logical operators:

  * `and`, `or`, `not`
* Nested conditions

### 🧠 Practice

* Built a **Grade Classifier** using conditional statements
* Solved basic decision-making problems on HackerRank

### 💡 Example

```python
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

---

## 🌞 Afternoon Session – Loops

### 🔹 Topics Covered

* `for` loops with `range()`
* Iterating through strings
* `while` loops
* Loop control statements:

  * `break`
  * `continue`
  * `pass`
* Nested loops (pattern problems)

### 🧠 Practice

* Printed number patterns using nested loops
* Iterated over strings and ranges
* Solved loop-based problems on HackerRank

### 💡 Example

```python
for i in range(5):
    for j in range(i):
        print("*", end=" ")
    print()
```

---

## 🌙 Evening Session – Mini Project

### 🎯 Project: Number Guessing Game

### 🔹 Features

* Random number between 1–100
* User keeps guessing until correct
* Provides hints:

  * Too high / Too low
* Tracks number of attempts

### 💡 Example

```python
import random

number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess > number:
        print("Too high!")
    elif guess < number:
        print("Too low!")
    else:
        print(f"Correct! You guessed in {attempts} attempts.")
        break
```

---

## 🧩 Practice Platform

* Solved problems on **HackerRank**

---

## 📈 Key Takeaways

* Learned how to control program flow using conditions
* Understood how loops reduce repetitive code
* Gained confidence with nested logic
* Built first interactive mini project 🎉

---

## 🔥 Next Goals (Day 3 Preview)

* Functions (`def`)
* Parameters & return values
* Code reusability
* More problem solving

---

## ✅ Status

✔ Completed Day 2
✔ Practiced problems
✔ Built mini project

---

# 📘 Day 3 – Python Learning Journey 🚀

## 📌 Overview

On Day 3, I focused on **advanced Python concepts** like:

* Lambda functions
* List comprehensions
* Functional programming (`map`, `filter`)
* Exception handling (`try`, `except`, `finally`, `raise`)

I also built a **Calculator Project with Error Handling** to apply these concepts practically.

---

## 🧠 Concepts Learned

### 🔹 1. Lambda Functions

* Learned how to write **anonymous one-line functions**
* Used for short, simple operations

```python
square = lambda x: x * x
```

---

### 🔹 2. List Comprehension

* Created lists in a **clean and efficient way**
* Added conditions inside list creation

```python
[x for x in range(10) if x % 2 == 0]
```

---

### 🔹 3. map() and filter()

* `map()` → Apply function to all elements
* `filter()` → Select elements based on condition

```python
list(map(lambda x: x*2, [1,2,3]))
list(filter(lambda x: x%2==0, [1,2,3,4]))
```

---

### 🔹 4. Exception Handling

* Used `try` and `except` to handle runtime errors
* Learned different exception types:

  * `ValueError`
  * `ZeroDivisionError`
  * `TypeError`

```python
try:
    x = int("abc")
except ValueError:
    print("Invalid input")
```

---

### 🔹 5. finally Block

* Executes **always**, whether error occurs or not

```python
finally:
    print("Execution completed")
```

---

### 🔹 6. raise Keyword

* Manually triggered exceptions for validation
* Enforced custom rules in program

```python
if op not in ['+', '-', '*', '/']:
    raise ValueError("Invalid operation")
```

---

## 💻 Mini Project: Calculator with Error Handling

### ✅ Features:

* Performs basic operations (+, -, *, /)
* Handles invalid inputs
* Prevents division by zero
* Uses `raise` for validation

---

## 🔥 Key Takeaways

* Python supports **functional programming** with lambda, map, filter
* List comprehensions are **more Pythonic and readable**
* Exception handling is essential for **robust applications**
* `raise` helps enforce **custom validation rules**

---

## 📈 Future Improvements

* Add loop for continuous calculations
* Build GUI calculator (Tkinter)
* Store calculation history
* Convert into web app (Flask / MERN)

---

## 🙌 Author

**Hareesh**
Aspiring MERN Stack Developer | Learning Python for Data Science 🚀

---


# 📘 Day 4 – Python Learning Journey

## 🚀 Topics Covered

### 🔹 List Comprehension

* Learned how to write concise and efficient loops using list comprehension.
* Practiced filtering and transforming data in a single line.

```python
squares = [x**2 for x in range(5)]
```

---

### 🔹 Dictionary Comprehension

* Understood how to create dictionaries dynamically.
* Applied conditions while building dictionaries.

```python
students = {"hareesh": 43, "arjun": 90, "rahul": 35}

failed_students = {name: marks for name, marks in students.items() if marks < 50}
```

---

### 🔹 Working with Dictionaries

* Accessed keys, values, and items
* Iterated using `.items()`
* Learned key-value mapping clearly

```python
for name, marks in students.items():
    print(name, marks)
```

---

### 🔹 Problem Solving Practice

✔ Stored student names and marks in a dictionary
✔ Calculated average marks
✔ Found topper using `max()`
✔ Filtered failed students
✔ Printed a formatted report

---

## 🧠 Key Learnings

* Difference between **list vs dictionary structures**
* Importance of **structured data**
* How **comprehensions simplify code**
* Avoiding variable naming mistakes (`mark` vs `marks`)

---

## 💡 Challenges Faced

* Confusion between dictionary and list of dictionaries
* Variable naming errors in comprehensions
* Understanding how `.items()` works

---

## 🎯 Outcome

* Improved understanding of **Python data structures**
* Gained confidence in solving **real-world problems**
* Started thinking in a more **optimized and structured way**

---

## 🔥 Next Plan (Day 5)

* Functions (def, return, arguments)
* Practice problems using functions
* More problem-solving (LeetCode / HackerRank)

---

## 📌 Status

✅ Completed Day 4 successfully
📈 Progressing consistently in Python & problem solving

---

💻 *“Consistency beats intensity. Keep coding daily!”*


# 📅 Day 5 – Python Learning Journey

## 📌 Topics Covered

### 🌅 Morning – Reading & Writing Files

* Learned how to use `open()` with different modes:

  * `r` → Read
  * `w` → Write
  * `a` → Append
* Used the `with` statement for safe file handling
* Read files line by line
* Wrote output to `.txt` files
* Explored the `os` module for file system operations

---

### 🌇 Afternoon – CSV & JSON Handling

* Worked with CSV files using the `csv` module
* Used `csv.reader()` and `csv.DictReader()`
* Learned JSON handling:

  * `json.loads()` → Convert JSON to Python
  * `json.dumps()` → Convert Python to JSON
* Understood basic API JSON structure

---

## 🌙 Project – Data File Processor (CLI Tool)

### 📊 Project Description

Built a Command Line Interface (CLI) tool to process CSV data efficiently.

### ⚙️ Features

* 📥 Read data from CSV file
* 🔍 Detect duplicate records
* 🧹 Handle missing values
* 📈 Generate summary report
* 📄 Write output to `output.txt`

---

## 🧠 Key Concepts Learned

* File handling in Python
* Working with structured data (CSV & JSON)
* Data cleaning techniques
* Using sets for duplicate detection
* Writing clean and modular functions

---

## 📄 Sample Output

```
Data Processing Summary
-----------------------
Total Rows: 4
Duplicate Rows: 1
Clean Rows: 3
```

---

## 🚀 Future Improvements

* Add CLI arguments (`argparse`)
* Export cleaned data to new CSV file
* Improve error handling
* Add logging for better debugging

---

## 💡 Conclusion

Day 5 focused on handling real-world data using Python.
This project is a strong foundation for backend development, data processing, and automation tasks.

---

### 🔥 Keep Learning & Building!
