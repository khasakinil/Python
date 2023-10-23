
user_dictionary = {
    'username' : 'Aman',
    "email" : "amanwa21@yahoo.com",
    'mobilenumber' : '9032323232',
    'age':34
}

print("_______________________________________")

print("dictionary Object : " , user_dictionary)
print("username : " , user_dictionary.get("username"))
print("email : " , user_dictionary.get("email"))

print("adding married key in dictionary")

user_dictionary["married"]=True

print("dictionary object after update")

print(user_dictionary)
print("_______________________________________")

print("Iterate dictionary Object")
for x, y in user_dictionary.items() : 
    print(x, " : ", y)

print("_______________________________________")

print("Colpying the dictionary object to other dictionary object")

user_dictionary2 = user_dictionary.copy()

user_dictionary2.pop("username")
print(user_dictionary2)

print("_______________________________________")
print("removing age key")
user_dictionary.pop("age")
print(user_dictionary)

print("clear user dictionary")
user_dictionary.clear()
print(user_dictionary)


print("_______________________________________")
print("Deleting the dictionary object")
del user_dictionary
print("_______________________________________")
