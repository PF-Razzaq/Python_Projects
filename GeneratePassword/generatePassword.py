import random
import string

print('Welcome to our Random Password Generator: ')

def generatePassword():
    # Use input instead of print to get user input
    length = int(input('Enter the length of Password you want: '))
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    symbol = string.punctuation

    combine = lower + upper + digit + symbol
    x = random.sample(combine, length)
    password = "".join(x)
    print('Generated Password: ',password)
    generatePassword()


# Call the function to generate a password
generatePassword()
