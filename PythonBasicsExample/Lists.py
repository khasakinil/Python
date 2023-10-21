number_list = [34,56,8,9,23,50]
print(number_list)

name_list = ["Ajit", "Abhi", "Om", 'Prashant', 'Sachin', "Mahesh", "Kartik"]
print(name_list)
print('name at index 2 : ', name_list[2])

print('Element at last index : ' , name_list[-1])

print('Length of number List : ' , len(number_list))

print('print names from the index : ' , name_list[1:5])

print("Append at end of list ")
name_list.append("Suraj");
print("name list after append : ", name_list)

print("insert element at specific location")
name_list.insert(2, "Sweety")
print("after inserting element at specific location : " , name_list)

print("remove specified element from list ")
name_list.remove("Mahesh")
print("name list after removing the specific elelment : " , name_list)

print("remove element from location ")
name_list.pop(2)
print("name list after removing the elelment at location : " , name_list)

print("Sort the name list")
name_list.sort()
print(f"After sorting name list : {name_list}")