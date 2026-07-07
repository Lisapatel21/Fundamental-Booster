<div align="center">

# 🚀 Fundamental Booster

### *Interactive Personal Data Collector — A Python Fundamentals Practice Program*

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/Type-Practice%20Program-blue?style=for-the-badge)

</div>

---

## 📌 Problem Statement

Beginners in Python often understand syntax but struggle to connect core concepts —
**variables, data types, type casting, `input()`, and the `id()` function** — into a single working program.

This project solves that gap by building a small, interactive console application that:
- Collects real user data (name, age, height, favourite number)
- Reveals the underlying **value, type, and memory identity** of each variable
- Performs a simple derived calculation (birth year) using that data

---

## 🎯 Objective

The goal of **Fundamental Booster** is to reinforce Python fundamentals through hands-on practice:

- ✅ Understand how `input()` works and why casting (`int()`, `float()`) is necessary
- ✅ Explore Python's dynamic typing using `type()`
- ✅ Understand object identity in memory using `id()`
- ✅ Perform simple arithmetic using collected user data
- ✅ Build confidence in writing clean, readable, well-structured beginner Python code

---

## 🛠️ Tech Stack

| Category | Technology |
|---|---|
| **Language** | Python 3 |
| **Core Concepts** | Variables, Data Types, Type Casting, `input()`, `type()`, `id()` |
| **Interface** | Command Line Interface (CLI) |
| **Dependencies** | None — pure Python standard library |

---

## 👩‍💻 Author

**Lisa Patel**
🔗 GitHub: [@Lisapatel21](https://github.com/Lisapatel21)
📁 Repository: [Fundamental-Booster](https://github.com/Lisapatel21/Fundamental-Booster)

---

## 🧾 Program

📄 File: [`PR.1 FUNDAMENTAL BOOSTER.py`](https://github.com/Lisapatel21/Fundamental-Booster/blob/main/PR.1%20FUNDAMENTAL%20BOOSTER.py)

```python
print("WELCOME TO THE INTERACTIVE PERSONAL DATA COLLECTOR")

name = input("Enter Your Name: ")
age = int(input("Enter your Age: "))
height = float(input("Enter your Height (in cm): "))
fav_number = int(input("Enter your Favourite Number: "))

current_year = 2026
birth_year = current_year - age

print("NAME")
print("Value :", name)
print("Type :", type(name))
print("ID :", id(name))

print("Age")
print("Value :", age)
print("Type :", type(age))
print("ID :", id(age))

print("Height")
print("Value :", height)
print("Type :", type(height))
print("ID :", id(height))

print("Favourite Number")
print("Value :", fav_number)
print("Type :", type(fav_number))
print("ID :", id(fav_number))

print("Approximate Birth Year :", birth_year)
print("Thank You for using the Personal Data Collector.")
print("Have A Great Day!")
```

### ▶️ How to Run

```bash
python3 "PR.1 FUNDAMENTAL BOOSTER.py"
```

You'll be prompted to enter your **name, age, height, and favourite number** — the program does the rest.

---

## 🔄 Flow

```
┌────────────────────────────┐
│        Program Start       │
└──────────────┬─────────────┘
               ▼
   Print Welcome Message
               ▼
   Collect User Inputs
   (name, age, height, fav_number)
               ▼
   Cast Inputs → int / float
               ▼
   Compute Birth Year
   (current_year − age)
               ▼
   Display Value, Type, ID
   for each variable
               ▼
   Print Birth Year Result
               ▼
   Print Thank You Message
               ▼
┌──────────────┴─────────────┐
│         Program End        │
└─────────────────────────────┘
```

---

## 🖥️ Output

<div align="center">

![Program Output](output_demo.png)

</div>

---

<div align="center">

⭐ *If this project helped you understand Python fundamentals better, consider giving the repo a star!* ⭐

</div>
