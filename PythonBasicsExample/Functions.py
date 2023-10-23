

def my_function():
    print("inside my_function")

def print_my_name(name):
    print(f"hello {name}")

def print_my_full_name(first_name, last_name):
    print(f"hello {first_name} {last_name}")

def print_number(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)

def multiply_numbers(number1, number2):
    return number1 * number2

def print_num_list(num_list):
    print("printing numbers in the list")
    for num in num_list :
        print(num)

def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
    current_tax_rate = 0.03
    return cost_of_item * current_tax_rate

print("__________________________________________")
my_function()
print("__________________________________________")
print_my_name("Mahadeo")
print("__________________________________________")
print_my_full_name("Michael", "Jackson")
print("__________________________________________")

print_number(lowest_number=12, highest_number=34)
print("__________________________________________")

multiply_num = multiply_numbers(3,8)
print("multiply_num : ", multiply_num)

print("__________________________________________")

number_list = [45,63,78,79,90,21,23,37,44,59]
print_num_list(number_list)

print("__________________________________________")
print("total cost to buy an item")
print(buy_item(50))
print("__________________________________________")
