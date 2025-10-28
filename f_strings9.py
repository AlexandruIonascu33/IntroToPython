# https://www.w3schools.com/python/python_string_formatting.asp

# What if we want to have more flexibility and control over what we print out?
# So called f-strings are another way of formatting printouts in Python.
# The syntax can initially look a bit confusing, but in the end f-strings are often the simplest way of formatting text.

#With f-strings the previous example would look like this:

result = 10 * 25
print(f"The result is {result}")


# name = "Mark"
# age = 37
# city = "Palo Alto"
# print(f"Hi {name}, you are {age} years old. You live in {city}.")





# Exercise:
# Your friend is working on an app for jobseekers. She sends you a bit of code.


# The program should print out exactly the following:

# my name is Tim Tester, I am 20 years old

# my skills are
#  - python (beginner)
#  - java (veteran)
#  - programming (semiprofessional)

# I am looking for a job with a salary of 2000-3000 euros per month




# The code works almost correctly, but not quite. This exercise has very strict tests, which check the output for every single bit of whitespace.

# Please fix the code so that the printout looks right. Notice especially how the comma notation in the print command automatically inserts a space around the different comma-separated parts.

# The easiest way to transform the code so that it meets requirements is to use f-strings.

# Hint: you can print an empty line by adding an empty print command, or by adding the newline character \n into your string.





# name = "Tim Tester"
# age = 20
# skill1 = "python"
# level1 = "beginner"
# skill2 = "java"
# level2 = "veteran"
# skill3 = "programming"
# level3 = "semiprofessional"
# lower = 2000
# upper = 3000

# print("my name is ", name, " , I am ", age, "years old")
# print("my skills are")
# print("- ", skill1, " (", level1, ")")
# print("- ", skill2, " (", level2, ")")
# print("- ", skill3, " (", level3, " )")
# print("I am looking for a job with a salary of", lower, "-", upper, "euros per month")