class Student:
    def __init__(self, age, classes, GPA, name):
        self.age = age
        self.classes = classes
        self.GPA = GPA
        self.name = name

    def myfunc(self):
        print("Hello my name is " + str(self.name) + ". I am " + str(self.age) + " years old. " + "I am taking " + str(self.classes) + " classes this year and my   GPA is "+ str(self.GPA))

    def learn(self):
        print("I am learning " + self.classes)

    def walk(self):
        print("I walk 15 mins to class everyday.")

t1   = Student(36, "Math and Science", 3.66,"Mia")
t1.myfunc()

t1.learn()

t1.walk()

    
class Course:
    def __init__(self, credits, teacher, course):
        self.credits = credits
        self.teacher = teacher
        self.course = course

    def myfunc(self):
        print("I am taking an " +str(self.course) + " course. My teachers name is " + str(self.teacher) + " I have " + str(self.credits) + " credits, thats why i am in this course")
 

c1 = Course(17, "Mr Smith", "AI")
c1.myfunc()

    
