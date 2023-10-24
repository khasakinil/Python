

class Student:

    def __init__(self, first_name, last_name, ):
        self.first_name = first_name 
        self.last_name = last_name

    def greetings(self):
        return f'Hello.. I am {self.first_name} {self.last_name} !!'
    

class CollegeStudent(Student):
    def __init__(self, first_name, last_name, major):
        super().__init__(first_name, last_name)
        self.major = major
    def greetings(self):
        return f'Hello.. I am {self.first_name} is a college student'

class NonCollegeStudent(Student):
    def __init__(self, first_name, last_name, future_job):
        super().__init__(first_name, last_name)
        self.future_job = future_job
    def my_future_job(self):
        return f'I want to become {self.future_job}';

stud_1 = CollegeStudent("Ciecel", "Strostop", "Elecronics")
stud_2 = Student("Sylvie", "Mane")

print(stud_1.greetings())
print(stud_1.major)
print(stud_2.greetings())

stud_3 = NonCollegeStudent("Mariene", "Jonnas", "Doctor")
print(stud_3.greetings())
print(stud_3.future_job)
print(stud_3.my_future_job())