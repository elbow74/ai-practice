class Course:
    occupation = "student"

    def __init__(self, name, course):
        self.course = course
        self.name = name

    def intro(intro):
        print(intro.name + " is taking " + intro.course)


student1 = Course("Steve", "math")
student2 = Course("Joy", "English")

student1.intro()
student2.intro()


class Age:

    def __init__(self, name, age):
        self.age = age
        self.name = name

    def register(intro):
        print(intro.name + " is " + intro.age + " years old")


student1 = Age("Steve", "19")
student2 = Age("Joy", "17")

student1.register()
student2.register()
