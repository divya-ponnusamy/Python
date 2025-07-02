
#1
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
a=num1+num2
print("The sum of ",num1,"and",num2 ," number is:",a)


#2
num1=int(input("Enter number:"))
if(num1%2==0):
    print("The number ",num1,"is Even number")
else:
    print("The number ",num1,"is odd number")
   
#3
num1=int(input("Enter Number:"))
fact=1
for i in range(1,num1+1):
    fact=fact*i
print("The factorial number is:",fact)

#4
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third  number:"))
if(num1>num2 and num1>num3):
    print("The biggest number is:",num1)
elif(num2>num1 and num2>num3):
    print("The biggest number is:",num2)
else:
    print("The biggest number is:",num3)

#5
for i in range(1,20):
    if (i%2==0):
        print(i)

#6
n=int(input("Enter the number:"))
sum=0
for i in range(1,n):
    sum+=i
    i+=1
    print(sum)

#7 

a=input("Enter the string:")
revers=a[::-1]
if(a==revers):
    print("This is palindrom")
else:
    print("This is not palindrom")
   
#10             
list1=[1,2,3,4,4,5,5,6]
list2=set(list1)
print(list2)

#12

a=input("Enter string")
b=a.upper()
print(b)

#13
r=float(input("Enter radius:"))
pi=3.142
formula=pi*(r**2)
print("The Area of circle is:",formula)

#14
a=[1,2,3,4,10,12,5,8,50]
b=max(a)
print("The maximum of the list is:",b)

#15
num1=int(input("enter number:"))
squr=num1**0.5
print("The squrt root of",num1,"is",squr)

#17
num1=int(input("Enter number:"))
num2=int(input("Enter power:"))
ans=num1**num2
print(num1,"**",num2,"=",ans)

#20
print("fibonacci series")
n=int(input("enter number"))
a,b,c=0,1,0
for i in range(1,n+1):
    print(c)
    a,b=b,c
    c=a+b

#21
year=int(input("Enter year:"))
if(year%100==0 and year%400==0):
    print(year,"is leap year")
elif(year%4==0 and year%100!=0):
    print(year," is leap year")
else:
    print(year,"is not leap year")

#22
table=int(input("Enter table:"))
limit=int(input("Enter limit:"))
for i in range(1,limit+1):
    print(i,"*",table,"=",i*table)
    
              

