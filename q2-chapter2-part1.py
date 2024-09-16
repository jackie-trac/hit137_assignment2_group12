def process_string(s):
    letters = ''
    numbers = ''
    for char in s:
        # Split the input string into letters and numbers
        if char.isalpha():
            # Checks if the letter is capatilised
            if char.isupper():
                # If it is then converts to ascii code
                letters = letters + str(ord(char))
            else:
                letters = letters + char
        elif char.isdigit():
            # Checks if the number is divisable by 2
            if int(char) % 2 == 0:
                # If it is then converts to ascii code
                numbers = numbers + str(ord(char))
            else:
                numbers = numbers + char
    print("Letters substring:", letters)
    print("Numbers substring:", numbers)

s = "56aAww1984sktr235270aYmn145ss785fsq31D0"
process_string(s)