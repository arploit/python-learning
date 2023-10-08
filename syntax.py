if 1 > 3:
    print("false")
else:
    print("true")


a = """
    test 
    print("hello world)
"""

print(a)


x, y, z = "Orange", "Apple", "Banana"

print("All the Fruits are " + x + ", " + y + ", " + z + ".")


# Global Variables


def myFunc():
    global zampa
    zampa = "adam"


myFunc()

print(zampa)


# data types

x = 1  # int
print(x)
print(type(x))


x = "str"  # string str
print(x)
print(type(x))

x = 3j  # complex number 'a + bi" a and b is real part and i = square root of -1
print(x)
print(type(x))


x = {"name": "Test", "SirName": "X"}  # dictonary it have keys and value pair
print(x)
print(type(x))


# Slicing the strings

b = "hello world"
print(b[2:5])  # positive indexing


print(b[-7:-4])  # negative indexing

print(b.upper())  # upper

print(b.strip())
print(b.capitalize())

print(b.replace("h", "w"))  # replace the string
