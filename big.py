
## question 2

def check_palindrome():
    text = input("Enter a string to check if it's a palindrome: ")
    if text == text[::-1]:
        print("Yes, it is a palindrome")
    else:
        print("No, it is not a palindrome")

# Run the function
check_palindrome()


## question 3

text1 = input("Enter the first text: ")
text2 = input("Enter the second text: ")

def process_texts(text1:str, text2:str) -> str: 
    combined = text1 + text2
    characters = [char for char in combined]  # creates a list of characters
    print("Characters in the combined text:", characters)
    print("\nThank you for using my application;")  # Displays the message 

# Run the function
process_texts(text1, text2)
