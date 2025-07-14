#1. Generator for Fibonacci Sequence:
def fibonacci(n):
    a, b = 0, 1
    while a <= n:
        yield a
        a, b = b, a + b
for num in fibonacci(10):
    print(num)

# 2. Generator for Even Numbers:
def even_number(n):
    for i in range(n+1):
        if i%2==0:
            yield i
for num in even_number(10):
    print(num)

# 3. Generator for Countdown:
def count_down(n):
    for i in range(n,-1,-1):
        yield i
for num in count_down(10):
    print(num)
    
# 4. Decorator for Greeting Message:
def greeting(func):
    def wrapper(*args,**kwargs):
        print("Hello!")
        return func(*args,**kwargs)
    return wrapper
@greeting
def fun_name(name):
    print(f"my name is{name}.")
fun_name("Divya")

# 5. Decorator for Capitalizing Return Value:
def capitalize(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@capitalize
def say_hello(name):
    return f"hello, {name}!"
print(say_hello("python"))

#6.what is iterator why did use ?
'''
* An iterator in Python is an object that holds a sequence of values and provide sequential traversal through a collection of items such as lists,
tuples and dictionaries.
* The Python iterators object is initialized using the iter() method.
* It uses the next() method for iteration.
Uses:
1. Memory Efficiency:
* Iterators are memory-efficient because they don't require storing the entire dataset in memory at once.
2. Lazy Evaluation:
* Iterators use lazy evaluation, meaning they only compute the next value when asked, which can be more efficient than computing all values upfront.
3. Flexibility:
* Iterators can be used with various data structures, including lists, tuples, dictionaries, sets, and more.
'''
