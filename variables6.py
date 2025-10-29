# https://www.w3schools.com/python/python_variables.asp

# Variables are containers for storing data values.

# A program can ask for more than one input. 
# Notice how below each input command stores the received value in a different variable.


name = input("What is your name? ")
email = input("What is your email address? ")
nickname = input("What is your nickname? ")

print("Let's make sure we got this right")
print("Your name: " + name)
print("Your email address: " + email)
print("Your nickname: " + nickname)





# If the same variable is used to store more than one input,
#  each new value will replace the previous one. For example:



# address = input("What is your address? ")
# print("So you live at address " + address)

# address = input("Please type in a new address: ")
# print("Your address is now " + address)



# This means that if the same variable is used to store two inputs in succession,
#  there is no way to access the first input value after it has been replaced by the second:



# address = input("What is your address? ")
# address = input("Please type in a new address: ")

# print("Your address is now " + address)




# Variables are needed for various purposes in programming.
#  You can use variables to store any information that will be needed later in the program's execution.

# In Python programming variables are created like so:

# variable_name = ...

# Here ... means the value stored in the variable.

# For example, when you used the input command to read a string from the user,
# you stored the string in a variable and then used the variable later in your program:



# name = input("What is your name? ")
# print("Hi, " + name)



# The value stored in a variable can also be defined using other variables:



# given_name = "Paul"
# family_name = "Python"

# name = given_name + " " + family_name

# print(name)



# Here the values stored in the three variables are not obtained from user input. 
# They remain the same every time the program is executed.
# This is called hard-coding data into the program.

# Thus far, we have only stored strings in variables, but there are also many other types of information we will want to store and access later.
# Let's have a look at integers first. 
# Integers are numbers that do not have a decimal or fractional part, such as -15, 0 and 1.



# The following program creates the variable age, which contains an integer value.



# age = 24
# print(age)




# The following program will not work, because "The result is " and result are of two different types:



# result = 10 * 25
# print("The result is " + result)



# If we do want to print out a string and an integer in a single command,
#  the integer can be cast as a string with the str function,
#  and the two strings can then be combined normally. More about conversion at https://www.w3schools.com/python/gloss_python_type_conversion.asp
# For example, this would work:

# result = 10 * 25
# print("The result is " + str(result))


# The print command also has built-in functionalities that support combining different types of values.
#  The simplest way is to add a comma between the values.
#  All the values will be printed out regardless of their type:



# result = 10 * 25
# print("The result is", result)