
Write a program, passwords Checker, which allows the user to repeatedly input a password until the input is "q".  Each password is error-checked according to the following conditions: 

* 1- A password must be at least 6 characters and at most 20 characters
* 2- A password must contain at least one lowercase letter
* 3- A password must contain at least one uppercase letter
* 4- A password must contain at least one number

-The conditions no. 2-4 are only checked if the password fulfills condition no. 1.

In each iteration, an appropriate error message is printed depending on whether the password is valid or invalid.  Finally,  information is printed regarding the count of passwords and how many of them are valid/invalid (you MUST to use a format string for this final output).  Example input/output can be seeen below.  

In your solution, you are only allowed to use material from the first 4 chapters in the textbook. 

Make sure that your solution is very readable (see for example this thread).

Note the following:

* The numbers 6 and 20, which stand for the minimum and maximum lengths of a password, should be implemented with constants. A constant in Python is a variable whose value should not be changed in a program.  It is a good rule to use capital letters for names of constants and define them at the start of the program.