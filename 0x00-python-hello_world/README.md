**0x00. Python - Hello, World**

This project aims to learn the follwing:

How to use the Python interpreter.

How to print text and variables using print.

How to use strings.

What are indexing and slicing in Python.

What is the official Python coding style and how to check your code with pycodestyle.

**TASKS**

* 0-run

Shell script that runs a Python script. The Python file name will be saved in the environment variable $PYFILE.

* 1-run_inline

Shell script that runs Python code. The Python code will be saved in the environment variable $PYCODE.

* 2-print.py

Python script that prints exactly "Programming is like building a multilingual puzzle, followed by a new line. Use the function print.

* 3-print_number.py

Complete this source code in order to print the integer stored in the variable number, followed by Battery street, followed by a new line.

**Source Code: #!/usr/bin/python3

number = 98

YOUR CODE GOES HERE. **

The output of the script should be: the number, followed by Battery street, followed by a new line.

You are not allowed to cast the variable number into a string.

Your code must be 3 lines long. You have to use f-strings tips.

* 4-print_float.py

Complete the source code in order to print the float stored in the variable number with a precision of 2 digits.

**Source Code: #!/usr/bin/python3

number = 3.14159

YOUR CODE GOES HERE. **

The output of the program should be: Float:, followed by the float with only 2 digits followed by a new line.

You are not allowed to cast number to string. You have to use f-strings.

* 5-print_string.py

Complete this source code in order to print 3 times a string stored in the variable str, followed by its first 9 characters. 

The output of the program should be: 3 times the value of str followed by a new line followed by the 9 first characters of str followed by a new line.

You are not allowed to use any loops or conditional statement

Your program should be maximum 5 lines long.

**Source Code: #!/usr/bin/python3

str = "Holberton School"

YOUR CODE GOES HERE.**

* 6-concat.py

Complete this source code to print Welcome to Holberton School!

You are not allowed to use any loops or conditional statements. You have to use the variables str1 and str2 in your new line of code.

Your program should be exactly 5 lines long

**Source Code: #!/usr/bin/python3

str1 = "Holberton"

str2 = "School"

YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE

print(f"Welcome to {str1}!")**

* 7-edges.py

Complete this source code. You are not allowed to use any loops or conditional statements, your program should be exactly 8 lines long.

word_first_3 should contain the first 3 letters of the variable word.

word_last_2 should contain the last 2 letters of the variable word.

middle_word should contain the value of the variable word without the first and last letters.

**Source Code: #!/usr/bin/python3

word = "Holberton"

YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE

print(f"First 3 letters: {word_first_3}")

print(f"Last 2 letters: {word_last_2}")

print(f"Middle word: {middle_word}")**

* 8-concat_edges.py

Complete this source code to print object-oriented programming with Python, followed by a new line.

You are not allowed to use any loops or conditional statements. Your program should be exactly 5 lines long.

You are not allowed to create new variables. You are not allowed to use string literals.

**Source Code: #!/usr/bin/python3

str = "Python is an interpreted, interactive, object-oriented programming\

 language that combines remarkable power with very clear syntax"
 
YOUR CODE GOES HERE. PLEASE REMOVE THIS LINE

print(str)**

* 9-easter_egg.py

Python script that prints “The Zen of Python”, by TimPeters, followed by a new line.

Your script should be maximum 98 characters long (please check with wc -m 9-easter_egg.py)

* 10-check_cycle.c, lists.h

Function in C that checks if a singly linked list has a cycle in it.

Prototype: int check_cycle(listint_t *list);

Return: 0 if there is no cycle, 1 if there is a cycle

lists.h - Provided data structure.

10-linked_lists.c / 10-linked_lists.c - provided c files

Compiled: gcc -Wall -Werror -Wextra -pedantic -std=gnu89 10-main.c 10-check_cycle.c 10-linked_lists.c -o cycle

