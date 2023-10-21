my_set = {1,5,3,8,1,2,3,5}

print("Set : " , my_set)
print("set Length : " , len(my_set))

print("Using for Loop")

for num in my_set:
    print(num)

my_set.discard(3)

print(my_set)

my_set.clear()
print(my_set)

my_set.add(7)
print(my_set)

my_set.update([2,1,5])
print(my_set)

print("___________________________")

my_tuple = (1,2,6,3,5,8,4)
print("Tuple : ", my_tuple)

print("Tuple element at index 2 : ", my_tuple[2])
print("setting tuple value at index 1")

print(my_tuple)