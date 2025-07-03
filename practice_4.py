#1. what is data comprehension?
'''Data comprehension refers to the ability to understand,interpret and analyze datatype'''
#2 find common elements
list1=[10,3,5,12,8]
list2=[11,3,4,6,8,20]
common_elements=[i for i in list1 if i in list2]
print(common_elements)

#3 inverted numbers
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
#4 difference between set and dictionary
'''Sets
1.Sets are unordered collections of unique elements.
2.Sets only store values, without any associated keys.
3.Sets automatically eliminate duplicate values.
4.Sets provide fast membership testing using the in operator.
5.It is a mutable datatype'''
'''
Dictionaries
1.Dictionaries are ordered collections of key-value pairs.
2.Dictionaries store key-value pairs, where each key is unique.
3.Dictionaries allow duplicate values, but keys must be unique.
4.Dictionaries provide fast lookups using keys.
5.It is mutable datatype.'''
#5 what is scripting mode and interactive mode
'''
Scripting mode
* write Python code in a file with a .py extension and then run the file using the Python interpreter.
  The code is executed from top to bottom, and the output is displayed in the console or terminal.
Interactive mode
* interact with the Python interpreter directly, writing and executing code one line at a time.
  The interpreter displays the output immediately after each line is executed.'''
#6 hollow square pattern
for i in range(1,6):
    for j in range(1,6):
        if(i==1 or i==5 or j==1 or j==5):
            print("*",end='')
        else:
            print(" ",end='')
    print()
   
#7 create dictionary where keys are numbers from 1 to 10 and values are odd or even

odd_even={i:"odd"if i%2!=0 else "even" for i in range(1,11)}
print(odd_even)

#8 list of tuples(x,x**2) numbers from 1 to 5

squares=[(i,i**2)for i in range(1,6)]
print(squares)

#9 words with more than three letters from["sql","python","script"]

word_list=[word for word in ["sql","python","script"]if len(word)>3]
print(word_list)

#10 Types of arguments
'''
Four types of arguments
1.Positional Arguments:
    These are the most basic type of argument.
    They are passed to a function in the same order they are defined in the function signature.

    def func(name, age):
        print("Hello",name,"! You are",age," years old.")
    func("John", 30)  # Output: Hello, John! You are 30 years old.
2.Keyword Arguments:
    These are arguments that are passed to a function using their parameter names.

    def func(name, age):
        print("Hello", name,"! You are" ,age ,"years old.")
    func(name="John", age=30)  # Output: Hello, John! You are 30 years old.
3.Default Arguments:
    These are arguments that have a default value.
    If no value is provided for the argument, the default value is used.

    def func(name, age=30):
        print("Hello", name,"! You are ",age," years old.")
    func("John")  # Output: Hello, John! You are 30 years old.
4.Variable-Length Arguments:
    These are arguments that can be passed to a function in any number.
    They are denoted by an asterisk (*) or two asterisks (**) in the function signature.

    def func(*names):
        for name in names:
            print("Hello",name,"!")
    func("John", "Jane", "Bob")  # Output: Hello, John! Hello, Jane! Hello, Bob!

'''
