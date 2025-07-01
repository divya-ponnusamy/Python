
----String-------

a="hello,welcome to my world"
b=a.capitalize()
print(b)
a="HELLO WORLD"
c=a.casefold()
print(c)
a="banana"
print(a.center(10))
a="i love apples,apples are my favourite"
print(a.count("apples"))
a="hello ,welcome to my world"
print(a.endswith("world"))
a="h\te\tl\tl\to"
print(a.expandtabs(8))
a="hello wprld"
print(a.find("helo"))
a="welcome to my world"
print(a.index("t"))
a="company 12"
print(a.isalnum())
a="company"
print(a.isalpha())
a="344567"
print(a.isdigit())
a="demo"
print(a.isidentifier())
a="hello world"
print(a.islower())
a="1234569"
print(a.isnumeric())
a="hello are you\n okay"
print(a.isprintable())

a=" "
print(a.isspace())
a="Hello World Hai "
print=(a.istitle())

a="APPLES"
print(a.isupper())
a="john","peeter","vicky"
print("!".join(a))

a="banana","apple","orange"
print("*".join(a))

a="banana"
print(a.ljust(20,"@"))
a="banana"
print(a.rjust(20,"&"))

a="banana"
print(a.center(20,"*"))

a="HELLO LOWER"
print(a.lower())

a="Hai Hello"
b=a.maketrans("l","*")
print(a.translate(b))

a="banana"
b=a.maketrans("a","&")
print(a.translate(b))

a="i could eat banana always my home"
print(a.partition("banana"))

a="i like apple"
print(a.replace("apple","graps"))

a="hai hello"
print(a.rfind("hello"))

a="hello welcome to my world"
print(a.rindex("t"))

a="i love banana ,i have banana at my home, banana is my favourite"
print(a.rpartition("banana"))

a="apple orange graps"
print(a.rsplit())

a="thank you for the music \n welcome to the jungle"
print(a.rsplitline())


a="hello world this is divya"
print(a.startswith("hello"))

a="   hello world"
print(a.strip())

a="    hello world  "
print(a.lstrip())

a="    hello world  "
print(a.rstrip())

a="@@@hello world divya@@@"
print(a.strip("@"))

a="divya is beautyfull \t girl"
print(a.strip("\t"))

a="Hello world"
print(a.swapcase())

a="hello world"
print(a.title())

a="hello my world"
print(a.upper())

a="10"
print(a.zfill(10))

-----LIST------

my_list=[1,2,3,4,5]
print(my_list)

print("INDEXING",my_list[0])

print("SLICIN",my_list[::-1])

a=[1,2,3,4]
a.append(5)
print(a)

a=[20,30,3,4,6,5,2]
a.insert(2,10)
print(a)

a.remove(10)
print(a)

print(len(a))




a=[1,2,3,4]
a.extend([5,6,7])
print(a)


a=[1,2,3,4,5,6]
a.remove(2)
print(a)

a.pop(0)
print(a)

a.clear()
print(a)

a=[1,2,3,4,7,4]
index=a.index(2)
print(index)

a=[1,2,3,4,5]
count=a.count(2)
print(count)

my_list=[1,4,7,5,2]
b=sorted(my_list)
print(b)

-----tuple------

a=(101,'mpona',25)
print(type(a))

b=("divya","sivanya","lithuran")
print(type(b))

c=10,20,30,40
print(type(c))

d=()
print(type(d)

a=(1,2,3,4,4,4,5,6)

b=a.index(1)
print(b)

c=a.count(4)
print(c)



a=[1,2,3,4]
b=[1,2,3,4,5]
print(len(a))

print(max(a))

print(min(a))
tupl=[1,"hai"]
x=tuple(tupl)
print(type(x))

----sets----


a={1,2,3,4}
b={3,4,5,6}

print(a.union(b))
print(a.intersection(b))
print(b.difference(a))
print(a.symmetric_difference(b))

a={1,2,3,4}


a.remove(3)
print(a)

a.discard(6)
print(a)

b=a.copy()
print(b)

a.clear()
print(a)

---------dict------
my_dict={"name":"divya","age":24}
print(my_dict.keys())
print(my_dict.values())
print(my_dict.items())

print(my_dict.update({"city":"erode"}))

print(my_dict)

print(my_dict.popitem())
print(my_dict.clear())
















