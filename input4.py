# https://www.w3schools.com/python/python_user_input.asp

#  Input refers to any information a user gives to the program. 
# Specifically, the Python command input reads in a line of input typed in by the user.
#  It may also be used to display a message to the user, to prompt for specific input.

name = input("What is your name? ")
print("Hi there, " + name)

# You can also convert that input into a specific data type

firstnumber = int(input("First number:"))
secondnumber = int(input("second number:"))

print(firstnumber + secondnumber)