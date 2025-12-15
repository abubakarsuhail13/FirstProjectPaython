"""List [] ordered | Indexed | changeable | Dublicates"""
my_list = ["London", "Manchester", "New York"]
print(my_list)
print(my_list[2])

my_list[2] = "New York"
print(my_list)

for val in my_list:
    print(val)
print(len(my_list))

my_list.append("Glasgow")
print(my_list)
my_list.insert(3,"Manchester")
print(my_list)

my_list.remove("Glasgow")
print(my_list)

my_list.pop(0)
print(my_list)

del my_list[0]
print(my_list)
my_list.insert(2,"Nottingum")
print(my_list)

my_list.clear()
print(my_list)

fruits = ["Apple", "Orange", "Cherry"]
print(fruits)
fruits.reverse()
print(fruits)

#List mix and match data type and nexted list under list
my_list_2 = ["Apple", 1,2,3,0]
my_list_3 = ["Apple", [1,2,3], ['a', 'b', 'c']]
print(my_list_3[1][2])