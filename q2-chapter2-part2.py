# c is text to be deciphered s is the cipher shift value
def decipher(c, s):
    original = ''
    for char in c:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Calculate the original ASCII value with wrap-around for uppercase letters
            char_num = ord(char) - s
            # Wrap-around if the new ASCII value is less than 'A'
            if char_num < 65:
                char_num = char_num + 26
            # Convert ASCII value back to character and add to result
            original = original + str(chr(char_num))
        else:
            # Non-uppercase letters (including lowercase and punctuation) are added as is
            original = original + char
    return original

# Initial shift value
s = 1
# Example cipher text
cipher = 'VZ FRYSVFU VZCNGVRAG NAQ N YVGGYR VAFRPHER V ZNXR ZVFGNXRF V NZ BHG BS PBAGEBY NAQNG GVZRF UNEQ GB UNAQYR OHG VS LBH PNAG UNAQYR ZR NG ZL JBEFG GURA LBH FHER NF URYYQBAG QRFREIR ZR NG ZL ORFG ZNEVYLA ZBAEBR'
# Loop through shift values until a sensible deciphered text is found
while True:
    # Decipher the text with the current shift value
    original = decipher(cipher, s)
    print(original)
    # Prompt the user to confirm if the deciphered text makes sense
    if input('Does the deciphered text make sense (Y/N): ').strip().upper() == 'Y':
        break
    # Increment the shift value for the next iteration
    s = s + 1
    # Loops s around incase the user missed it the first go through
    if s == 26:
        s = s - 26
print("Shift value was:", s)
print("The original quote was:", original)
