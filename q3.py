'''
STEP 1: Fixing the given code by adding print functions
        Running the code to reveal the total and counter values
        Since the code returns 2 numeric values, we will try them both for decryption
'''
total = 0
for i in range(5):
    for j in range(3):
        if i + j == 5:
            total += i + j
        else:
            total -= i - j

counter = 0
while counter < 5:
    if total < 13:
        total += 1
    elif total > 13:
        total -= 1
    else:
        counter += 2
# Adding print functions
print('Key value (total): ',total)
print('Counter value: ',counter)

'''
STEP 1 OUTPUT:
Key value (total): 13
Counter value: 6
-----------------------------------------------------------------------------------------------------------------
'''
'''
STEP 2: Write Decrypt code by reversing the Encrypt function
- From observation we see the encrypt mistifies the codes by changing the ASCII values of alphabetic characters.
- We subtract the key from the ASCII value of the character (instead of adding it like in the encryption process).
- Adding the numeric values from step 1 to the key. We have tried both and only 13 works
- Adding the encrypted code to the decrypt function
'''
# Write Decrypt function by reversing Encrypt
def decrypt(encrypted_text, key):
    decrypted_text = ""

    for char in encrypted_text:
        if char.isalpha():
            shifted = ord(char) - key  # Reverse the shift by subtracting the key

            if char.islower():
                if shifted < ord('a'):  # If it goes below 'a', wrap around
                    shifted += 26
                elif shifted > ord('z'):  # Ensure the character doesn't go beyond 'z'
                    shifted -= 26
            elif char.isupper():
                if shifted < ord('A'):  # If it goes below 'A', wrap around
                    shifted += 26
                elif shifted > ord('Z'):  # Ensure the character doesn't go beyond 'Z'
                    shifted -= 26

            decrypted_text += chr(shifted)  # Add the decrypted character to the result
        else:
            decrypted_text += char  # Non-alphabetic characters are not shifted, just added

    return decrypted_text

key = 13 #Using Key = 13 as Key=6 doesn't work
#Passing encrypted code to this text, using triple double-quotes to keep preserve formatting
encrypted_code = """ 
tybony_inevnoyr = 100
zl_qvpg = {'xrl1': 'inyhr1', 'xrl2': 'inyhr2', 'xrl3': 'inyhr3'}

qrs cebprff_ahzoref():
    tybony tybony_inevnoyr
    ybpny_inevnoyr = 5
    ahzoref = [1, 2, 3, 4, 5]

    juvyr ybpny_inevnoyr > 0:
      vs ybpny_inevnoyr % 2 == 0:
        ahzoref.erzbir(ybpny_inevnoyr)
      ybpny_inevnoyr -= 1

    erghea ahzoref

zl_frg = {1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1}
erfhyg = cebprff_ahzoref(ahzoref=zl_frg)

qrs zbqvsl_qvpg():
    ybpny_inevnoyr = 10
    zl_qvpg['xrl4'] = ybpny_inevnoyr

zbqvsl_qvpg(5)

qrs hcqngr_tybony():
    tybony tybony_inevnoyr
    tybony_inevnoyr += 10

sbe v va enatr(5):
    cevag(v)
    v += 1

vs zl_frg vf abg Abar naq zl_qvpg['xrl4'] == 10:
    cevag("Pbaqvgvba zrg!")

vs 5 abg va zl_qvpg:
    cevag("5 abg sbhaq va gur qvpgvbanel!")

cevag(tybony_inevnoyr)
cevag(zl_qvpg)
cevag(zl_frg)
"""
decrypted_code = decrypt(encrypted_code, key)
print("Decrypted code:", decrypted_code)

'''
-----------
STEP 2 OUTPUT: Original Code Revealed 
Additional comments added at errors/unnecessary lines

Decrypted code: 
global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

def process_numbers(): 
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    while local_variable > 0:
      if local_variable % 2 == 0:
        numbers.remove(local_variable) #The remove() method will throw an error if the value to be removed is not in the list => add condition
      local_variable -= 1

    return numbers

my_set = {1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1}
result = process_numbers(numbers=my_set) #The function process_numbers() doesn't accept any arguments, but numbers=my_set is passed to it. This will raise an error because process_numbers() is written to use an internal list, not external data => remove argument

def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

modify_dict(5) #The function modify_dict() doesn't accept any arguments but called with one. This will cause an error => Remove argument

def update_global():
    global global_variable
    global_variable += 10

for i in range(5): #This function seem to be irrelevant with the overall purpose of the code => Consider removing the entire funtion
    print(i)
    i += 1  #This line is unnecessary when incrementing manudally because Python handles the increment internally => removed along with the function

if my_set is not None and my_dict['key4'] == 10: #Redundant of NONE since my_set has earlier been defined in this code, 'and' assumes my_dict['key4'] exists which could lead to error if key4 is not added properly => remove checking NONE
    print("Condition met!")

if 5 not in my_dict:
    print("5 not found in the dictionary!") 

print(global_variable)
print(my_dict)
print(my_set) #my_set is defined as a set earlier, but it contains duplicate values, this definition will automatically collapse into {1, 2, 3, 4, 5, 6} when printed, if duplicates are needed, convert to list, otherwise leave as is.
'''

'''
-----------------------------------------------------------------------------------------------------------------
STEP 3: Fixing the orginal code
In addition to fixing the code based on commented lines, the structure of the code has been reorganized for readabiliy, clarity and maintainability
Inline comments are also added
'''
# Global variable and dictionary definition
global_variable = 100
my_dict = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

# Function to process numbers and modify a global variable
def process_numbers():
    global global_variable
    local_variable = 5
    numbers = [1, 2, 3, 4, 5]

    # Modify numbers based on local_variable conditions
    while local_variable > 0:
        if local_variable % 2 == 0 and local_variable in numbers:
            numbers.remove(local_variable)
        local_variable -= 1

    return numbers

# Function to modify my_dict by adding a new key-value pair
def modify_dict():
    local_variable = 10
    my_dict['key4'] = local_variable

# Function to update global_variable
def update_global():
    global global_variable
    global_variable += 10

# Function to check conditions and print results
def check_conditions_and_print():

    # Check if key4 exists and meets condition
    if my_dict.get('key4') == 10:
        print("Condition met!")

    # Check if 5 is not in the dictionary and print
    if 5 not in my_dict:
        print("5 not found in the dictionary!")

    # Print final results
    print('Global variable:',global_variable)
    print('My dict:',my_dict)
    print('My set:',my_set)

# Added main execution flow. This makes the code more modular and clearer to follow.
def main():
    # Process numbers
    result = process_numbers()
    
    # Modify dictionary
    modify_dict()
    
    # Update global variable
    update_global()
    
    # Check conditions and print
    check_conditions_and_print()

# Set definition (converted to list if duplicates are needed)
my_set = {1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1} 

# Call main
main()

'''
STEP 3 OUTPUT:
Condition met!
5 not found in the dictionary!
Global variable: 110
My dict: {'key1': 'value1', 'key2': 'value2', 'key3': 'value3', 'key4': 10}
My set: {1, 2, 3, 4, 5, 6}
'''
