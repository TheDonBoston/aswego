# Python program which asks a user to input any number
# The program will tell the user if the number is prime or composite
import math

# Asking the user for an integer to input
# We do not need to set a range, we simply set a variable
# And that variable is whatever the user inputs
# The user creates the range
num = int(input("Enter Number: "))

is_prime = True

if num > 1:
# This is the modulus of the user input integer by each number in the range
# If the answer (remainder) is zero, that means it is a composite number
# Which is why is_prime will equal false
    for i in range(2,num):
        if (num % i) == 0:
            is_prime = False
            break
# This calls back to is_prime = True.  The condition created above makes
# Any other result: is_prime = True.
    if is_prime:
        print(num, "is a prime number.")
    else:
        print(num, "is a composite number.")