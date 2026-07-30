class Parrot :
    species = " Bird "
    def __init__(self , name , age):
       self.name = name
       self.age = age
blu = Parrot("blu" , 10)
woo = Parrot("woo"  , 15)
print("================")
print("Blu is a {}  " .format(blu.species))
print("Woo is a  {}" .format(woo.species))

print("================")
print(" {} is {} years old".format(blu.name , blu.age))
print(" {} is {} years old".format(woo.name , woo.age))