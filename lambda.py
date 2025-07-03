'''result=lambda x,y:x+y
print(result(1,2))
'''
def add(x,y):
    return x+y
number=lambda x,y:add(x,y)
print(number(2,3))


def greet(name,age):
    return f" my name is {name}my age is {age}"

a=lambda name,age:greet(name,age)
print(a("divya",25))
