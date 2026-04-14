# program is asking student name,age,city and cgpa

name = (input("ENTER YOUR NAME:"))
age = int(input("ENTER YOUR AGE:"))
cgpa = float(input("ENTER YOUR CGPA:"))
city = (input("ENTER YOUR CITY:"))

print("*"*10)
print(f"Hello my name is {name}.I am {age} year old and i live in {city}.My cgpa is {cgpa}.")
print("*"*10)
print("CHECK TYPE")
print(type (name))
print(type (age))
print(type (cgpa))
print(type (city))
print("*"*10)