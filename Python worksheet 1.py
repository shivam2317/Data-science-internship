#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = int(input("Enter a number: "))
result = factorial(num)
print(f"The factorial of {num} is {result}")


# In[2]:


import math

num = int(input("Enter a number: "))
result = math.factorial(num)
print(f"The factorial of {num} is {result}")


# # 2.Write a python program to find whether a number is prime or composite.

# In[ ]:


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test the function
num = int(input("Enter a number: "))

if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is a composite number.")


# # . Write a python program to check whether a given string is palindrome or not.

# In[ ]:


def is_palindrome(s):
    """
    Returns True if the input string is a palindrome, False otherwise.
    """
    return s == s[::-1]

# Test the function
input_string = input("Enter a string: ")

if is_palindrome(input_string):
    print("The string is a palindrome!")
else:
    print("The string is not a palindrome.")


# # Write a Python program to get the third side of right-angled triangle from two given sides.

# In[ ]:


import math

def find_third_side(a, b):
    """
    Returns the third side of a right-angled triangle given two sides a and b.
    """
    if a > b:
        hypotenuse = a
        other_side = b
    else:
        hypotenuse = b
        other_side = a
    
    third_side = math.sqrt(hypotenuse**2 - other_side**2)
    return third_side

# Test the function
a = float(input("Enter the first side: "))
b = float(input("Enter the second side: "))

third_side = find_third_side(a, b)

print("The third side of the right-angled triangle is: ", third_side)


# #  Write a python program to print the frequency of each of the characters present in a given string.
# 
# 

# In[ ]:


# Python program to print the frequency of each character in a given string

def char_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

string = input("Enter a string: ")
frequency = char_frequency(string)

print("Character Frequency:")
for char, freq in frequency.items():
    print(f"{char}: {freq}")


# In[ ]:


Enter a string: hello world
Character Frequency:
h: 1
e: 1
l: 3
o: 2
 : 1
w: 1
r: 1
d: 1
    


# In[ ]:




