# Function that separates the input string 's' into two substrings: 
# one containing letters, the other containing numbers.
def separate_string(s):
    letters = ""  # To store all alphabetic characters (both upper and lower case)
    numbers = ""  # To store all numeric characters
    # Loop through each character in the string 's'
    for char in s:
        # If the character is a letter, add it to 'letters'
        if char.isalpha():
            letters += char
        # If the character is a digit, add it to 'numbers'
        elif char.isdigit():
            numbers += char
    # Return the separated letters and numbers
    return letters, numbers


# Function that processes the separated letters and numbers to:
# 1. Extract even numbers and convert them to their ASCII code values
# 2. Extract uppercase letters and convert them to their ASCII code values
def converted(letters, numbers):
    even_numbers = ""  # To store even digits from the numbers string
    even_numbers_ascii = ""  # To store the ASCII values of even digits
    # Loop through each digit in the numbers string
    for digit in numbers:
        # Check if the digit is even
        if int(digit) % 2 == 0:
            # Append the digit to 'even_numbers'
            even_numbers += digit + " "
            # Append the ASCII value of the digit to 'even_numbers_ascii'
            even_numbers_ascii += f"{digit}({ord(digit)}) "

    uppercase_letters = ""  # To store uppercase letters from the letters string
    uppercase_letters_ascii = ""  # To store the ASCII values of uppercase letters
    # Loop through each letter in the letters string
    for lett in letters:
        # Check if the letter is uppercase
        if lett.isupper():
            # Append the letter to 'uppercase_letters'
            uppercase_letters += lett + " "
            # Append the ASCII value of the letter to 'uppercase_letters_ascii'
            uppercase_letters_ascii += f"{lett}({ord(lett)}) "

    # Return the even numbers and their ASCII values, 
    # as well as the uppercase letters and their ASCII values
    return even_numbers.strip(), even_numbers_ascii.strip(), uppercase_letters.strip(), uppercase_letters_ascii.strip()


# Define the input string 's' for processing
s = "56aAWW1984sktr235270aYmn145ss785fsq31D0"

# Call the 'separate_string' function to split 's' into letters and numbers
letters, numbers = separate_string(s)

# Call the 'converted' function to process the separated letters and numbers
even_numbers, even_numbers_ascii, uppercase_letters, uppercase_letters_ascii = converted(letters, numbers)

# Print the results
print("Letters:", letters)
print("Numbers:", numbers)
print("Even numbers:", even_numbers)
print("Even numbers in ASCII:", even_numbers_ascii)
print("Uppercase Letters:", uppercase_letters)
print("Uppercase Letters in ASCII:", uppercase_letters_ascii)
