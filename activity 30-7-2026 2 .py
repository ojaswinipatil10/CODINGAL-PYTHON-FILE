class student:
    grade = 10
    name = "Flower"
    def introduction(self):
        print("================")
        print("I am a student ")
      
    def details(self):
        print("My name is " , self.name)
        print(" I study in Grade " , self.grade)
        print("================")
ob = student()
ob.introduction()
ob.details()
