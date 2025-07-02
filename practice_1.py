num=int(input("Enter Number:"))
if(num%5==0):
    print("The number is divisible by 5")
else:
    print("The Number is not divisible by 5")



num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
if(num1>num2):
    print(num1,"is largest number")
else:
    print(num2,"is largest number")



Mark=float(input("Enter marks:"))
if(Mark>=40):
    print("The student is pass")
else:
    print("The student is Fail")


year=int(input("Enter year"))
if(year%4==0 and (year%100!=0 or year % 400==0)):
   print("This is leap year")
else:
    print("Not leap year")


char=input("Enter character :")
if(char=='a' or char=='e' or char=='i'or char=='o' or char=='u' or char=='A' or char=='E' or char=='I' or char=='O' or char=='U'):
    print("This is a Vowel")
else:
    print("This is a consonant")
    
