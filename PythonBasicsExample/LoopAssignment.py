

my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

i=0
while i<3:
    i += 1
    for day in my_list :
        if day == "Monday" :
            continue
        print(day)