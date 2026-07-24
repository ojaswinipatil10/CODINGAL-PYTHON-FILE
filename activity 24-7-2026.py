fruits = ["mango" , "apple" , "dragon fruit" , "cherries" , "orange"]
print("==============================")
print("================")
print("Fruit List:" , fruits )
print("Total fruits : " , len(fruits))
print("First fruit :" , fruits[0])
print("Last fruit :" , fruits[-1])
print("First three fruits :" , fruits[:3])
print("================")
a = fruits.append("Guava")
print("/nAfter adding Guava:" , fruits)
print("================")
fruits.remove("dragon fruit")
print("================")
fruits.sort()
print("Sorted alphabetically :" , fruits)
print("================")
fruits.reverse()
print("Reversed :" , fruits)
print("================")
print("==================================")


roll_numbers = [1 , 2, 3 , 4, 5, 6]
names = ["Aarav" , "Sneha" , "Priyanka" , "Jiya"]
student_directory = dict(zip(roll_numbers , names))
print("/nStudent Directory :" , student_directory)
print("================")
print("Student at Roll 3 :" , student_directory[3])
print("================")

print("==============================")
