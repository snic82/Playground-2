# Playground-2
> Python Practice Programs

>>STRINGS
```
In a python program when printing statements it needs to be in quotation either in single or double but printing a statement without a quotation gives an error.
Consider, printing a statement: Hello This is my First Python program.
Sol: print("Hello This is my First Python program.")
      OR
     print('Hello This is my First Python program.')
```
>>COMMENTS
```
Adding # at the beginning will make the entire line a comment.
Comments will not be executed when running code, so you can use them to leave notes.
```
>>INTEGERS
```
You can use numbers like integers in programming. Unlike strings, they don't need to be enclosed in quotes. You can add and subtract integers just like you do in math. The spaces before and after operators are not required, but they will make the code easier to read.
Ex: print(3+5)
      OR
    print(2 + 4)
```
>>DIFFERENCE BETWEEN STRINGS AND INTEGERS
```
Strings and integers are interpreted differently in programming. Like the images below, 3 + 5 will print 8, which is the result of the addition. However, if you enclose it in quotes and make it a string, the output will stay as 3 + 5.
Ex: print(3+4)
      OR
    print('3+4')
```
>>VARIABLES
```
A variable is like a box with a name in which you can store a value.
DEFINING A VARIABLE:
To store a value in a variable, you need to define a variable. You can do this in the following format: variable_name = value. The = operator in Python does not mean "equal". This assignment operator means assign the value on the right to the variable on the left. Note that variable names don't need to be enclosed in quotes.
Ex: name = 'JOHN'
      OR
    number = 34
NAMING A VARIABLE:
You can pick any name for variables, but there are some rules. For example, you cannot start a variable name with a number. Also, when a variable name contains more than two words, like user_name, you should separate them with _.
Ex: data     OR      user_name
```
>>STRING CONCATENATION
```
The + operator that we used for calculations also lets us combine strings. Combining strings is called string concatenation. String concatenation can be used with strings and variables that have string values.
Ex: print("Hello" + " World")
      OR
    name = JOHN
    print("My name is" +name)
```
>>Type Conversion: str()
```
Like the image on the left, you can't concatenate strings and integers because they have different data types. In order to concatenate different types of data, you have to perform type conversion. In the example below, you first have to convert the integer to a string, using str().
Ex: price = 3
    print("The apple costs " +price+ "dollars") 
    #the above statement shows an error.
    
    price = 3
    print("The apple costs " +str(price)+ "dollars")
```
>>Type Conversion: int()
```
You also can't perform calculations with a string and an integer.
You have to convert the string to an integer using int().
Ex: count = 3
    price = 100
    total_price = price * int(count)
    print(total_price)
```
