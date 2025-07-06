# GROUP 11 MEMBERS
1.MUSINGUZI Medard 26601
2.MUPENZI Serge 25181
3.
4.
5.
6.
7.

**Instructor**: Dr. Eric Maniraguha
**Institution**: Adventist University of Central Africa
**Course Name**:Introduction to Big Data Analytics 
**Course Code**: INSY 8413.
**Date**: 6th, July,2025.


# 🧠 Python Quiz – Big Data Analytics (INSY 8413)

This project contains solutions to two tasks of an in-class group work 

---

## ❓ Question II: Palindrome Checker 🔁

**Description:**  
Write a function that asks the user to input a string and checks if the string is a **palindrome** (reads the same forwards and backwards).Print "Yes,it is a palindrone"
or "No, it is not a palindrone"

### ✅ Requirements:
- Use `input()` to get user input.
- Use a function to perform the task.

### 🧪 Example:
Input: "madam"
Output: Yes, it is a palindrome



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


## ❓ Question III: Iterating Over Two Text Inputs ✍️🔡
**Description:**
Write a Python function that:

Asks the user to **enter two separate texts**.

Combines the two texts into one.

Iterates over each character in the combined text and returns a list of characters.

Prints a thank-you message.

✅ Requirements:
Use input() to get user input.

Use a function to perform the task

Return the list of characters obtained from the combined text.

Display the message Thank you for using my application; on the console.

🧾 Solution (Python Code):
```

    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")

  def process_texts(text1,str; text2,str):
    combined = text1 + text2
    characters = [char for char in combined]

    # Thank-you message
    print("\nThank you for using my application;")

    return characters

# Run the function
result = process_texts(text1, text2)
print("Characters in the combined text:", result)


                                             # THANK YOU


