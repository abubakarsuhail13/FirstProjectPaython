#Four collections data types in Python
# {} Set unordered | unindexed | no duplicates

my_set = {"Chalk", "Duster", "Marker"}
print(my_set)

for value in my_set:
    print(value)

print("Duster" in my_set)
my_set.add("White Board")
print(my_set)

my_set.remove("Chalk")
print(my_set)

my_set.update(["Pen","Eraser"])
print(my_set)

my_set.discard("Pen")
print(my_set)

my_set.pop()
my_set.clear()
print(my_set)

del my_set

my_set_2 = {"apple", 1,2,(1,2,3)}
print(my_set_2)

my_list = (1,2,3,4)
print(my_list)

my_set_3 = set(my_list)
print(my_set_3)

#Union | Intersection | Diff | Symmetric Diff
#Union
A = {'A', 'B', 1, 2, 3}
B = {'B', 'C', 3 ,4, 5}
print(A.union(B))
print(A | B)

print(A.intersection(B))
print(A & B)

print(A.difference(B))
print(A - B)

print(A.symmetric_difference(B))
print(A ^ B)