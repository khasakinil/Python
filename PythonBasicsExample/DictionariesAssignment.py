""" 
Assignment :

Based on the dictionary:

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
- Create a for loop to print all keys and values

- Create a new variable vehicle2, which is a copy of my_vehicle

- Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4

- Delete the mileage key and value from vehicle2

- Print just the keys from vehicle2
 """


my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}

print("printing vehicle dictionary object")

for k,v in my_vehicle.items() :
    print (k,v)

print("copy vehicle dictionary object to other object")

vehicle2 = my_vehicle.copy()
vehicle2['number_of_tires']=4
vehicle2.pop("mileage")

for x in vehicle2 :
    print(x)


