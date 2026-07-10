fruit_name ="apple"
price = 8
quantity = 6
is_available = True
print("fruit" , fruit_name)
print("price AED" , price)
print("In stock" , quantity)
print("Present" , is_available)
print(type(fruit_name))
print(type(price))
print(type(quantity))
print(type(is_available))
total = price * quantity
print("Total cost is AED" , total)
print("Sale price AED" , price - 3.5 )
print("Double stock" , quantity * 2)
print("Is the price under AED 50?" , price < 50)
print("Less than 2 in class ?" , quantity <2)
print("Is the fruit name Orange ?" , fruit_name == "Orange" )
fruit_type = "Red" + " " + "Fresh"
print("fruit type:",  fruit_type)

price_a = 5
price_b = 7
print("Before:" , price_a , "and" , price_b)

temp = price_a 
price_a = price_b
price_b = temp
print("After:" , price_a, "and" , price_b)
