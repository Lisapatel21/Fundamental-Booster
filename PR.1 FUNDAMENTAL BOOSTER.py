print("WELCOME TO THE INTERACTIVE PERSONAL DATA COLLECTOR")

name = input("Enter Your Name: ")

age = int(input("Enter your Age: "))

height = float(input("Enter your Height (in cm): "))

fav_number = int(input("Enter your Favourite Number: "))

current_year = 2026
birth_year = current_year - age

rounded_height = int(height)


age_after_10 = age + 10


print(f"NAME")
print("Value :", name)
print("Type :", type(name))
print("ID :", id(name))
print()

print(f"Age")
print("Value :", age)
print("Type :", type(age))
print("ID :", id(age))
print()

print(f"Height")
print("Value :", height)
print("Type :", type(height))
print("ID :", id(height))
print()

print(f"Favourite Number")
print("Value :", fav_number)
print("Type :", type(fav_number))
print("ID :", id(fav_number))
print()


print("\n")

print("Approximate Birth Year :", birth_year)


print("\n")
print("Thank You for using the Personal Data Collector.")
print("Have A Great Day!")

