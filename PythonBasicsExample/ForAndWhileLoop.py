

my_num_list = [23,6,7,8,9,63,22,33,44,54]

print("For loop example")

print("print all the numbers using for loop")

for num in my_num_list :
    print(num)

print ("__________________________________")

for num in range(2,5):
    print(num)
print ("__________________________________")

sum_of_nums = 0

for num in my_num_list :
    sum_of_nums += num

print("Sum of nums : " , sum_of_nums)
print ("__________________________________")

week_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for day in week_days:
    print(f"happy {day}")

print ("__________________________________")
print("While loop example")

i = 0
while i<5:
    i=i+1
    if i==2:
        continue
    print(i)
    if i==4:
        break
else:
    print("i is now larger or equal to 5")

print ("__________________________________")

