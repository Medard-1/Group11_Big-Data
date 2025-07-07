# GROUP 11 MEMBERS
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

This project contains solutions to two tasks of an in-class group work 

---

## ❓ Question II: Palindrome Checker 🔁

**Description:**  
We were tasked to write a function that asks the user to input a string and checks if the string is a **palindrome** (reads the same forwards and backwards).Prints "Yes,it is a palindrone"
or "No, it is not a palindrone"

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
(![Running Code](https://github.com/user-attachments/assets/2b695a97-0f5e-4e25-a93a-36fb553a3235)
)

## ❓ Question III: Iterate Over Two Text Inputs ✍️🔡

**Description:**
Write a Python function that:

Asks the user to enter two separate texts.

Combines the two texts into one.

Iterates over each character in the combined text and returns a list of characters.

Prints a thank-you message.

### ✅ Requirements:

- Use input() to get user input.
- Use a function and return the list of characters.
- Return the list of characters obtained from the combined text
- Display the message Thank you for using my application; on the console.

### 🧾 Solution (Python Code):
```python

   def process_texts(): 
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")
    combined = text1 + text2
    characters = [char for char in combined]  # creates a list of characters

    print("\nThank you for using my application;")  # Displays the message 
    print("Characters in the combined text:", characters)

# Run the function
process_texts()

```
(![Running Code](https://github.com/user-attachments/assets/225454c1-bffe-4021-8426-bbfc682309c8)
)
# THANK YOU

