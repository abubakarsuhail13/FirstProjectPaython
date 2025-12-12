"""() Puple Ordered | Indexed | Unchangeable | Dublicates"""
my_tuple = ("Apple", "Bannana", "Cherry")
print(my_tuple)
print(my_tuple[0])
print(my_tuple[-1])
print(my_tuple[0:4])

for val in my_tuple:
    print(val)

#"""Unchange able in puple and add any object in puple"""
#my_tuple[3] = 'Grapes'

print(len(my_tuple))
my_tuple_2 = ("Bannana", (1,2,3), ["London", "Manchester", "New York"])
print(my_tuple_2)
print(my_tuple_2[2])
print(my_tuple_2[2][1])

my_tuple_2[2][2] = "Glassgow"
print(my_tuple_2)