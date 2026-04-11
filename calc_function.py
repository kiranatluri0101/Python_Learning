#importing sys module to assign variables
import sys

#defining variabales
action=sys.argv[1]
a = int(sys.argv[2])
b = int(sys.argv[3])

#defining function
def addition():
    add=a+b
    print(add)

def substraction():
    sub=a-b
    print(sub)

def multiplication():
    mul=a*b
    print(mul)

#These if conditions, will invoke the function based on input givne user
if action == "add":
   addition()
elif action == "sub":
   substraction()
elif action == "mul":
   multiplication()
else:
   print("Your action shoould be either add or sub or mul and syntax is python calc_function.py action number1 number2")