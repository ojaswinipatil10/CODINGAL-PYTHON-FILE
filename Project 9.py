class Robot:
    def __init__(self , name , age ):
            self.name = name
            self.age = age
    def introduction(self):
      print("----- __________-----")
      print(" Hello ✋! My name is {}  my age is {} years old 😀👌 !" .format(self.name , self.age) )
robot1 = Robot("Tom" , 2 )
robot2 = Robot("Jerry" , 3 )
robot1.introduction()
robot2.introduction()