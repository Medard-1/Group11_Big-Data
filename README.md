# 👥 GROUP 11 MEMBERS
1. MUSINGUZI Medard 26601
2. MUPENZI Serge 25181
3. Aimable Bimenyimana 25094
4. NTWARI Deus 25048
5. ISHIMWE Honore 26578
6. Pacifique HARERIMANA 26937
7. MUGISHA David 26484


---
 
#### **Instructor**: Dr. Eric Maniraguha
#### **Institution**: Adventist University of Central Africa
#### **Course Name**: Introduction to Big Data Analytics 
#### **Course Code**: INSY 8413.
#### **Date**: 6th, July,2025.
---

# 🧠 Python Quiz – Big Data Analytics (INSY 8413)

This quiz represents a practical application of fundamental python programming concepts within the context of data analytics. As part of our coursework in INSY 8413 – Introduction to Big Data Analytics at the Adventist University of Central Africa, our group was tasked with solving real-world inspired coding problems using Python.

# 🎯 Objectives of the Quiz
- Apply Python functions to solve modular problems

- Demonstrate the use of input/output handling

- Build clean, user-friendly console applications

- Reinforce the importance of code structure, return values, and indentation

# 💻 Tools and Skills Used
- Python 3.x

- Programiz

- Console-based input/output

- String slicing and looping

- List comprehension

- Function definition,call and return values

# 👨‍👩‍👧‍👦 Group Collaboration
This was a collaborative group effort, with each member contributing to designing, testing, and refining the solutions. We discussed logic, shared feedback, and ensured each function met the assignment’s criteria while maintaining clean coding practices.


---  


<br>

## ❓ Question II: Palindrome Checker 🔁

**Description:**  
We were tasked to write a function that asks the user to input a string and checks if the string is a **palindrome** (reads the same forwards and backwards).Prints "Yes,it is a palindrone"
or "No, it is not a palindrome"

### ✅ Requirements:
- Use `input()` to get user input.
- Use a function to perform the task.

### 🧪 Example:
- Input: "madam"
- Output: Yes, it is a palindrome
- OR
- Input: "run"
- Output: No, it is not a palindrone



### 🧾 Solution (Python Code):
```python
def check_palindrome():
    text = input("Enter a string to check if it's a palindrome: ")
    if text == text[::-1]:
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")

# Run the function
check_palindrome()

```
<br>

### Running Code
(![Running Code](https://github.com/user-attachments/assets/2b695a97-0f5e-4e25-a93a-36fb553a3235)
)

<br>
<br>

## ❓ Question III: Iterate Over Two Text Inputs ✍️🔡

**Description:**

We are to write a Python function that:

- Asks the user to enter two separate texts.

- Combines the two texts into one.

- Iterates over each character in the combined text and returns a list of characters.

- Prints a thank-you message on console.

### ✅ Requirements:

- Use input() to get user input.
- Use a function and return the list of characters.
- Return the list of characters obtained from the combined text
- Display the message Thank you for using my application; on the console.

### 🧾 Solution (Python Code):
```python

text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")

def process_texts(text1:str, text2:str) -> str: 
    combined = text1 + text2
    characters = [char for char in combined]  # creates a list of characters
    print("Characters in the combined text:", characters)
    print("\nThank you for using my application;")  # Displays the message 

# Run the function
process_texts(text1, text2)

```
<br>

### Running Code
![qn3](https://github.com/user-attachments/assets/6d1abc83-f261-4e7c-ab59-8bdd7271bb07)

<br>

# THANK YOU


**“Two are better than one, because they have a good return for their labor: If either of them falls down, one can help the other up.”**  
 — *Ecclesiastes 4:9–10 (NIV)*
