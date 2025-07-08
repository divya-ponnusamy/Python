#1.What is map() function in python?
'''
* It is a Built-in function.
* It applies a given function to each item of an iterable and return a map object.
syntax:
    map(function,iterable)'''
#2.What is the filter() function in python?
'''
* It is a Build-in function.
* That constructs an iterator from elements of an iterable for which a function is true and it return fliter object.
syntax:
    fliter(function,iterable)'''
#3.What is the eval() function in python?
'''
* It is a Built-in function.
* It is evaluates expressions passed as strings and return the result.
* It can be evalute mathematical expressions that are stroed as strings.
syntax:
    eval(expression,globals,locals)'''
#4.Write a Python program that takes a list of numbers and returns a list where each element is squared. Use the map() function to solve this.
number=[1,2,3,4,5,6]
squ=list(map(lambda x:x**2,number))
print(squ)

#.5.Write a Python program that uses the filter() function to return only the even numbers from a given list.
num = [1, 2, 3, 4, 5, 6]
even=list(filter(lambda x:x%2==0,num))
print(even)

#6.Write a Python program that takes a list of strings and uses map() to convert each string to uppercase.
words = ["hello", "world", "python"]
uppercase=tuple(map(str.upper,words))
print(uppercase)

#7.Write a Python program that uses filter() to remove all negative numbers from a given list of integers.
n = [1,-2,3,-4,5,-6]
negative=set(filter(lambda x:x>0,n))
print(negative)

