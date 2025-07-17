'''def fun(a,b):
    try:
        c=a+b
        print(c)
    except Exception as e:
        print("Error occured",e)
    
    else:
        print("no exception error occured")
    finally:
        print("successfully running")
a=int(input("Enter number:"))
b=int(input("Enter number:"))
fun(a,b)
'''

def fun1(x):
    def fun2(y):
       z=x/y
       print(z)
    return fun2
obj=fun1(10)
obj.fun2()
