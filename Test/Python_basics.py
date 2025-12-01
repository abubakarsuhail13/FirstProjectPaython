print("Hi NFT Wales Good to Seen You!")

# Case_Sensitive, Letters(a-z), underscore, numbers(0-9) 60
x = 50
y = "Automation"
print(x)
print(y)

#Plus is a concadination operation in paython Plus pas the Variable x
# example "Hellow Automation"
print("Hello "+ y)
print("Hellow"+ y)

#Varialbles
x = 10
y = 11
print(x+y)

# Syntaxt (if we creating any block lets say array)
#(System should get automatically spaces beclow 5 spaces)
if 10 > 5:
    print("10 is greater then 5")

#Function plus syntext
def sum(a,b):
    print(a+b)

x = sum(10, 20)

#From commandline
# C:\Users\Dell>cd C:\Users\Dell\PycharmProjects\FirstProjectPaython\Test\

#C:\Users\Dell\PycharmProjects\FirstProjectPaython\Test>Python_basics.py
#Output:
# Hi NFT Wales Good to Seen You!
#50
#Automation
#Hello Automation
#HellowAutomation
#21
#10 is greater then 5
#30

#numbers operations in python
#floot and complex numbers
# <class 'x int'>
# <class 'y float'>
# <class 'z complex'>
x = 5
y = 2.5
z = 4j
print(type(x))
print(type(y))
print(type(z))

#Casting and strip operations in paython
x = int(2)        # 2
y = int(2.5)      # 2
z = float(3)      # 3.0
p = str(10)       # "10"

print(x)
print(y)
print(z)
print(p)

#Strings operations in paython
x = "Hellow NFT-Wales.."
print(x[3:16])

print(x)
print(len(x))
print(x.lower())
print(x.upper())
x = "Hellow, NexaForge Technologies - Wales.."
print(x.replace("e","a"))
print(x.split(","))

#Input taken using in python
print("Enter yout first input: ")
x = input()
print("Hellow Abubakar, "+ x)