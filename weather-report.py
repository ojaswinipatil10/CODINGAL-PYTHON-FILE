print("\n================================")
City = input("Enter your city name : ")
Temperature = float(input("Enter the city's temperature: "))
print("\n================================")
if Temperature > 35:
 print("Warning : the temperature is too hot !")
if Temperature < 25:
 print("Its a great day to go outside !")
else:
   print("Grab a jacket before you go out !")
print("\n================================")
if Temperature > 35:
  print("Weather Label: SCORCHING HOT !")
elif Temperature > 25:
  print("Weather Label: Warm and sunny")
elif Temperature > 15:
    print("Weather Label: Cool and Breezy")
else:
    print("Weather Label: Cold")
print("\n================================")
import datetime
import calendar
print("\n================================")
now = datetime.datetime.now()
print("City:" , City)
print("Time now:" , now )
print(calendar.calendar(now.year))