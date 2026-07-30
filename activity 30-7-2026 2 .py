class student:
    grade = 10
    name = "Flower"
    def introduction(self):
        print("I am a student ")
    def details(self):
        print("My name is " , self.name)
        print(" I study in Grade " , self.grade)
ob = student()
ob.introduction()
ob.details()
