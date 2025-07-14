# nested function
'''def outer_function():
    msg='python'
    def inner_function():
        print(msg)
    return inner_function
obj=outer_function()
obj()
'''
def fun1(x):
    def fun2(y):
       z=x/y
       print (z)
    return fun2
obj=fun1(10)
obj.fun2(2)
