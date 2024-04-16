# Program asks user to input the word "alphabetical" in all lower case

# Since humans can't sit here and type one word nearly 1 million times
for i in range(1, 999999):
    """This allows the user to correctly input the string 999,998 times before the program stops"""
    user_input = str(input("To print 'pbil', type and enter 'alphabetical' in all lowercase: "))
    
    is_alpha = True

# The string has to be letter for letter, and all lower case to be true
    if user_input == "alphabetical":
        """If the user types in this string, the program is true, and will print 'pbil'"""
        is_alpha = True
        print("pbil")

# This is where the code for user error exists. The print explains the error to the user
# Programmer asks the user a rhetorical question about the assignment
    if user_input != "alphabetical":
        """if anything else other than the characters in the string above are typed
        end the program and tell the user why"""
        is_alpha = False
        print("Programmer says: Run again. Check spelling; type in all lowercase.")
        print("By the way... What even is 'pbil'?")
        break