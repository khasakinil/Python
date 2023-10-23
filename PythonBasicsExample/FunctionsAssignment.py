""" Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values """

def user_details_dictionary(firstname, lastname, age):
    user_information = {
        "firstname" : firstname,
        "lastname" : lastname,
        "age" : age
    }
    return user_information

print(user_details_dictionary("Mohan", "Tripathi", 34))