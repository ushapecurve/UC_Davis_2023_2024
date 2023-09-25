#!/usr/bin/env python
# coding: utf-8

# # Week 1 - Homework
# 
# Double-click on the cells that say `ANSWER N:` (e.g. `ANSWER 1:`) to type your answer, leaving the prompt in place. For example, if the answer to question -8 were `yes` the cell should contain the text: `ANSWER -8: yes`
# 
# To lock in a cell with text, just execute it with *CTRL+ENTER* (or *CMD+ENTER* on MacOS).
# 
# When you are done with this assignment, go to *File* > *Download as...* > *Python (.py)* and save your Python file. Then submit your .py file to the assignment on Canvas.
# 
# ## Task 1
# 
# Execute the following code and answer the questions below.

# In[4]:


print(3 + 4, "int and int")
print(3.0 + 4, "float and int")
print(3 + 4.0, "int and float")
print(3.0 + 4.0, "float and float")
print()
print(3 - 4, "int and int")
print(3.0 - 4, "float and int")
print(3 - 4.0, "int and float")
print(3.0 - 4.0, "float and float")
print()
print(3 * 4, "int and int")
print(3.0 * 4, "float and int")
print(3 * 4.0, "int and float")
print(3.0 * 4.0, "float and float")


# QUESTION 1: What is the result of adding, subtracting, or multiplying two ints? (8 pts)

# ANSWER 1: The result will be an integer.

# QUESTION 2: What is the result of adding, subtracting, or multiplying two floats? (8 pts)

# ANSWER 2: The result will be always a float.

# QUESTION 3: What is the result of adding, subtracting, or multiplying a float and an int? Does the order matter? (9 pts)

# ANSWER 3: If one of two operands is float, the result will be always float. The order does not matter.

# ## Task 2
# 
# Execute the following code and answer the questions below.

# In[6]:


print(35 / 5, "int and int", " - division")
print(35.0 / 5, "float and int",  " - division")
print(35 / 5.0, "int and float", " - division")
print(35.0 / 5.0, "float and float", " - division")
print()
print(35 // 5, "int and int", " - floor division")
print(35.2 // 5, "float and int", " - floor division")
print(35 // 5.0, "int and float", " - floor division")
print(35.0 // 5.0, "float and float", " - floor division")
print()
print(35 % 5, "int and int", " - modulo")
print(35.0 % 5, "float and int", " - modulo")
print(35 % 5.0, "int and float", " - modulo")
print(35.0 % 5.0, "float and float", " - modulo")


# In[3]:


print(9 / 4)
print(10 / 4)
print(156 / 5)
print(15 / 5)
print(5 / 642)


# QUESTION 4: What is the result of \[true / regular\] division on two ints? (8 pts)

# ANSWER 4: The result will always be float.

# QUESTION 5: What is the result of \[true / regular\] division on two floats? (8 pts)

# In[4]:


print(9.1 / 4.0)
print(10.52 / 4.549)
print(156.0 / 5.44)
print(15.0 / 5.0)
print(5.0 / 642.0)


# ANvSWER 5: The result will always be float.

# QUESTION 6: What is the result of \[true / regular\] division on a float and an int? Does the order matter? (9 pts)

# In[6]:


print(9 / 4.0)
print(8 / 4.0)
print(9.0 / 4)
print(8.0 / 4)
print(" ")
print(10.52 / 4)
print(" ")
print(150 / 15.00)
print(15.0 / 5)
print(5 / 642.46)


# ANSWER 6: Division of float and int will always return float as a result. Order does not matter.

# QUESTION 7: What is the result of floor division or modulus on two ints? (8 pts)

# In[16]:


print(18 % 5, "int and int")
print(18 % 5.0, "float and int")
print(18.0 % 5.0, "float and float")
print(17.9999 % 5.0, "float and float")
print(18.25 % 5.0, "float and float")
print(" ")
print(8.0 % 4, "float and int")
print(8.0 % 4.0, "float and float")
print(8 % 4, "int and int")
print(10 % 4, "int and int")
print(" ")
print(10.52 % 4, "float and int")
print(10.50 % 0.25, "float and float")
print(10.51 % 0.25, "float and float")
print(" ")
print(155 % 15.00, "int and float")
print(15.00 % 155, "float and int")
print(15.0 % 7, "float and int")
print(5 % 642.0, "int and float")


# ANSWER 7: The result of floor division or modulus on two ints will be always an int.

# QUESTION 8: What is the result of floor division or modulus on two floats? (8 pts)

# ANvSWER 8: The result of floor division or modulus on two floats. It will always be a float.

# QUESTION 9: What is the result of floor division or modulus on a float and an int? Does the order matter? (9 pts)

# ANSWER 9: What is the result of floor division or modulus on a float and an int. The result will always be a float.

# ## Task 3
# 
# Write your own code to answer the question below.

# In[19]:


# YOUR CODE HERE
# print('hello' % 'world') - error
print('hello' + 'world')
# print('hello' - 'world') - error


# QUESTION 10: Which of the arithmetic operators we have covered can be used on two strings? (e.g. `'hello' % 'world'`) (7 pts)

# ANSWER 10: Only concatenation of two strings can be executed.

# ## Task 4
# 
# Write your own code to answer the question below.

# In[30]:


# YOUR CODE HERE
print('hello' * 7)
print(7 * 'hello')
# print('hello' + 7) - error
# print(7 + 'hello') - error
# print('hello' - 7) - error
# print(7 - 'hello') - error
# print('hello' * 7.86) - error
# print(0.7 * 'hello') - error


# QUESTION 11: Which of the arithmetic operators we have covered can be used on a string and an int? Does the order matter? (e.g. `'hello' % 7` and `7 % 'hello'`) (9 pts)

# ANSWER 11: Python interpreter can only multiply string by an int. Order does not matter.

# ## Task 5
# 
# Write your own code to answer the question below.

# In[34]:


# YOUR CODE HERE
# print('hello' * 7.86) - error
# print(0.7 * 'hello')  - error
# print('hello' + 7.86)  - error
# print(0.7 + 'hello')  - error


# QUESTION 12: Which of the arithmetic operators we have covered can be used on a string and an float? Does the order matter? (e.g. `'hello' % 5.2` and `5.2 % 'hello'`) (9 pts)

# ANSWER 12: Python interpreter cannot add, substract or multiply or divide a float to a string. The order does not matter.

# **REMINDER:** When you are done with this assignment, go to *File* > *Download as...* > *Python (.py)* and save your Python file. Then submit your .py file to the assignment on Canvas.
