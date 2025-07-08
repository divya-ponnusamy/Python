#1.What is the closure  function?
'''Python closure is a nested function that allows us to access variables of the outer function even after the outer function is closed.'''
#Why did Use Closure Functions?
'''
* State Preservation:
    Closures allow you to maintain state between function calls without using global variables or passing arguments
    promoting modularity and code clarity. 
* Function Factories:
    You can create functions that generate other functions with specific behaviors based on the environment where they were defined. 
* Data Hiding:
    Closures can be used to create private variables
    They are only accessible within the scope of the nested function. 
* Decorators:
    Closures are a fundamental part of how decorators work in Python
    Allowing  to modify the behavior of functions without directly altering their code. 
* Functional Programming:
    Closures are a core feature of functional programming
    Enabling you to create more flexible and modular code by generating new behavior dynamically.'''
#2.Create a closure that generates a unique ID each time it is called. The closure should remember the last generated ID and return the next one each time.
def create_generate_id():
    x = 0
    def generate_id():
        nonlocal x
        x+=1
        return x
    return generate_id
new_id=create_generate_id()
print(new_id())
print(new_id())
print(new_id())
#3.Write a closure powervalue(exponent) that returns a function which raises a given number to the power of exponent.
def number(x):
    def power_number1(y):
       b = x**y
       return b
    return power_number1
a=int(input("Enter the value:"))
d=int(input("Enter the power:"))
obj=number(a)
print(obj(d))
#4.create a closure make_passwordcheck(correct_password) that returns a function that checks whether the input password matches the correct password.
#If the passwords match, it should return "Access granted", otherwise "Access denied".    

def password():
   x=12345
   def password_check(y):
       if (x==y):
           return f"Access granted"
       else:
            return f"Access denied"
   return password_check
num=int(input("Enter password:"))
obj= password()
print(obj(num))
#5.Write a closure string_repeater(s) that returns a function that repeats the given string s a specified number of times.
def string(name):
    def repeat(n):
        x=name*n
        return x
    return repeat
a=input("Enter the string:")
b=int(input("Enter number of times:"))
string_value=string(a)
print(string_value(3))
    

