#Python Programming Basics |

# If Else Loop Elif
if 10 > 5:
    print("10 is greater than 5")
else:
    print("10 is not greater than 5")

num = 0
if num > 0:
    print("num is positive number than 0")
elif num == 0:
    print("num is zero number")
else:
    print("num is negative than 0")

#for loop
num = [1,2,3,4,5]
sum = 0
for val in num:
    sum = sum + val
print("Total number is: ", sum)

#While loop
Fruits = ["Apple", "oranges", "graps", "benana"]
for value in Fruits:
    print(value)
else:
    print("No Fruits")

#print("Please enter a input: ")
num = (int(input("Enter a number: ")))
a = input(num)
sum = 0
i = 1
while i < num:
    sum = sum + i
    i = i + 1
    print("Total number is: ", sum)
else:
    print("Total number is: ", sum)