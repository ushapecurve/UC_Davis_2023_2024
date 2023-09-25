#!/usr/bin/env python
# coding: utf-8

# # Week 2 - Homework
# 
# ## Task 1.A (25 pts)
# 
# Let's implement the `yell()` function. This function takes a string as input, converts the text in that string to all capital letters, appends three exclamation points to the text, and then returns the text.
# 
# For example, after executing the code `loud_laughter = yell('lol')` the variable `loud_laughter` should contain the string `'LOL!!!'` .
# 
# Here is some code to get you started. I recommend you manually type out the code in the cell below instead of copy/pasting it in order to better internalize the content and structure of the code. (You do not need to duplicate the comments, they are just there to guide your work.)
# ```
# def yell(text):
#     big_text = __________  # Do something with: text
#     result = __________    # Do something with: big_text
#     return __________      # Do something with: result
# ````
# 
# Hints:
# - You can do this using only the tools we have covered so far. Importantly, you will need to look up [string methods](https://docs.python.org/3/library/stdtypes.html#string-methods) in the Python documentation.
# - This function should not display anything, so the solution will *not* include `print()` .
# - This function should not ask the user a question, so the solution will *not* include `input()` .

# In[6]:


# Your code should include the complete function definition and
# implementation for yell(). This code should execute without
# syntax errors and without raising exceptions at runtime.
#
# Enter your code for Task 1.A below this comment:

# Just for myself, asking python version.
import sys
import platform
print(sys.version)

def yell(input_text):
    big_text = input_text.upper()
    result = big_text + "!!!"
    return result 

print(yell("how are you?"))

 
# Question: what if somebody will try to pass int type into yell() function?
# How can I protect my code against such misuse?
# Shall I use an exception?  I cannot figure out how to do it.


# ## Task 1.B (20 pts)
# 
# Now that you have written the `yell()` function with each small step on its own line of code in task 1.A, write the function in the cell below with just one line for the function body.
# 
# Your solution to Task 1.B should look like this:
# ```
# def yell(text):
#     return __________  # Just one line of code inside the function.
# ```

# In[9]:


# Your code should include the complete function definition and
# implementation for yell(). This code should execute without
# syntax errors and without raising exceptions at runtime.
#
# Enter your code for Problem 1.B below this comment:

def yell(input_text):
    return input_text.upper()  + "!!!"
  

print(yell("how are you?"))


# ## Task 1.C (15 pts)
# 
# Let's make sure that `yell()` works as expected.
# 
# One test case has been provided for you. Write three more test cases below it on the lines provided.
# 
# Note: Until you define the function `yell()` above, executing the sample test case will raise a NameError exception.

# In[19]:


# Example test case:
print(yell('lol'))  # Expected output: LOL!!!

# Test case No. 1:
print(yell('The AI team, which was uploading training data'))

# Test case No. 2:
print(yell(' to let other researchers train AI models for image recognition'))

# Test case No. 3:
print(yell('Free encrypted email and calendar'))


# ## Task 2 (10 pts)
# 
# Last week we looked at applying arithmetic operators (e.g. `+ - * /` ) to operands of different data types. We saw that any combination of an int and a float resulted in a float, because the integer value was *promoted* to a float before the computer's hardware could perform the operation. We also saw that we can use the string repeat operator `*` between a string and an int (e.g. `'=' * 10`).
# 
# Execute the following code:
# ```
# print(1, True + 4)
# print(2, -7 + True)
# print(3, False + 5.5)
# print(4, 8.9 - False)
# print(5, '|' + "ABC" * True + '|')  # Use pipes to clearly indicate the result.
# print(6, '|' + "ABC" * False + '|')  # Use pipes to clearly indicate the result.
# ```
# 
# What does this tell you about the `bool` data type?

# In[11]:


print(1, True + 4)
print(2, -7 + True)
print(3, False + 5.5)
print(4, 8.9 - False)
print(5, '|' + "ABC" * True + '|')  # Use pipes to clearly indicate the result.
print(6, '|' + "ABC" * False + '|')  # Use pipes to clearly indicate the result.


# ANSWER 2: 
# False is used as 0 in mathematical operations.
# True is used as 1 in mathematical operations.

# ## Task 3 (30 pts)
# 
# Let's say I did not want to have to write `isinstance(___, int)` every time I wanted to check if a variable contains an integer. Instead, I would like something short and easy, such as `is_int(___)` .
# 
# Define and implement a new function called `is_int` which takes one parameter. This function should return `True` when the argument provided by the caller is an `int`, and False otherwise.
# 
# Examples of how this function could be used:
# ```
# value_1 = 12321
# print("Is", value_1, "an int?", is_int(value_1))
# value_2 = -12321
# print("Is", value_2, "an int?", is_int(value_2))
# value_3 = None
# print("Is", value_3, "an int?", is_int(value_3))
# ```
# 
# Hints:
# - You can do this using only the tools we have covered so far.
# - This function should not display anything, so the solution will *not* include `print()` .
# - This function should not ask the user a question, so the solution will *not* include `input()` .

# In[18]:


# Enter your code for Task 3 here:
def is_int(input_number):
    return isinstance(input_number, int)   #Question: is IsInstance() and isinstance() the same in python?
    
value_1 = 12321
print("Is", value_1, "an int?", is_int(value_1))
value_2 = -12321
print("Is", value_2, "an int?", is_int(value_2))
value_3 = None
print("Is", value_3, "an int?", is_int(value_3))
value_4 = 12.321
print("Is", value_4, "an int?", is_int(value_4))
value_5 = "-12321"
print("Is", value_5, "an int?", is_int(value_5))
value_6 = (3, 8, 65)
print("Is", value_6, "an int?", is_int(value_6))
value_7 = True
print("Is", value_7, "an int?", is_int(value_7))
value_8 = False
print("Is", value_8, "an int?", is_int(value_8))

