## ✅ Mini Projects & Final Capstone Evaluation — Course 1

---

### 📌 Mini Projects

#### **Week 4 Mini Project — Simple Calculator**

**Objective:** Apply Python basics, loops, and conditionals.

**Requirements:**

* Perform addition, subtraction, multiplication, division
* Accept user input
* Loop until user chooses to exit
* Handle division by zero errors

**Sample Solution:**

```python
while True:
    print("Menu: 1-Add 2-Subtract 3-Multiply 4-Divide 5-Exit")
    choice = input("Choose: ")
    if choice == "5":
        break
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    
    if choice == "1":
        print("Result:", a+b)
    elif choice == "2":
        print("Result:", a-b)
    elif choice == "3":
        print("Result:", a*b)
    elif choice == "4":
        try:
            print("Result:", a/b)
        except ZeroDivisionError:
            print("Cannot divide by zero")
```

**Evaluation Checklist:**

* ✅ Accepts input and performs correct operations
* ✅ Handles division by zero
* ✅ Uses loops and conditionals effectively
* ✅ Clean and readable code

---

#### **Week 8 Mini Project — Grade Analyzer**

**Objective:** Apply lists, loops, functions, and basic statistics.

**Requirements:**

* Input multiple students and grades
* Display highest, lowest, average grade
* Count students above a threshold
* Use functions for modularity

**Sample Solution:**

```python
students = []

def add_student(name, grade):
    students.append({"name": name, "grade": grade})

def stats():
    grades = [s["grade"] for s in students]
    return max(grades), min(grades), sum(grades)/len(grades)

# Example usage
add_student("Alice", 90)
add_student("Bob", 75)
add_student("Charlie", 85)
print("Stats:", stats())
```

**Evaluation Checklist:**

* ✅ Correctly computes max, min, average
* ✅ Uses functions
* ✅ Handles multiple inputs
* ✅ Lists and loops used appropriately

---

#### **Week 12 Mini Project — Student Grades Application**

**Objective:** Combine lists, dictionaries, loops, searching, counting.

**Requirements:**

* Add, search, update students
* Count students above a grade threshold
* Display statistics
* Optional: sort students by grade

**Evaluation Checklist:**

* ✅ Uses dictionaries for student records
* ✅ Functions modularize operations
* ✅ Loops and conditionals correctly implemented
* ✅ Correct statistics and counting
* ✅ Handles exceptions and invalid input

---

### 📌 Final Capstone Project — Week 13–16

**Project:** **Student Performance Manager**

**Requirements:**

1. Add, update, delete students
2. Search for students (linear/binary search)
3. Count students above/below threshold
4. Display statistics (max, min, average)
5. Sort students (bubble/merge sort)
6. Recursive features (factorial, sum, nested sums)
7. Handle exceptions and invalid input
8. Modular functions for each operation
9. Menu-based user interaction

**Evaluation Rubric:**

| Criteria             | Points | Description                                                   |
| -------------------- | ------ | ------------------------------------------------------------- |
| Code Structure       | 20     | Functions modularized, readable code                          |
| Correctness          | 30     | Correct implementation of all required features               |
| Algorithm Efficiency | 20     | Appropriate search, sort, recursion; avoids unnecessary loops |
| Exception Handling   | 10     | Handles invalid input gracefully                              |
| Testing & Debugging  | 10     | Tested on multiple datasets, correct output                   |
| Documentation        | 10     | Comments, clear variable names, project description           |

**Total Points: 100**

---

### 📌 Python Script for Generating All Diagrams

```python
import matplotlib.pyplot as plt
import os

IMAGES_DIR = "images"
os.makedirs(IMAGES_DIR, exist_ok=True)

def create_placeholder(filename, title):
    plt.figure(figsize=(6,4))
    plt.text(0.5, 0.5, title, fontsize=14, ha='center', va='center')
    plt.axis('off')
    plt.savefig(os.path.join(IMAGES_DIR, filename))
    plt.close()

diagrams = [
    ("week1-computational-thinking.png","Computational Thinking Flow"),
    ("week2-variables-types.png","Variables & Types"),
    ("week3-conditions-loops.png","Conditions & Loops"),
    ("week4-simple-calculator.png","Simple Calculator Flow"),
    ("week11-bigO-growth.png","Big O Growth Chart"),
    ("week12-project-data-flow.png","Student Grades Project Flow"),
    ("week13-function-call-flow.png","Function Call Flow"),
    ("week14-bubble-sort-flow.png","Bubble Sort Flow"),
    ("week15-binary-search-flow.png","Binary Search Flow"),
    ("week16-capstone-data-flow.png","Capstone Project Data Flow")
]

for fname, title in diagrams:
    create_placeholder(fname, title)

print("✅ All diagram placeholders generated in 'images' folder.")
```

---

This completes **Course 1 — Programming Logic & Algorithms with Python**, including:

* 16 weeks of content
* Mini Projects (Week 4, 8, 12)
* Final Capstone Project (Week 13–16)
* Evaluation Rubrics
* Python script to generate all diagrams

---
