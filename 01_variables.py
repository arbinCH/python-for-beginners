# variable = A container of data or value(string, integer, float, boolean.("data types"))
# A variable behaves as if it was the value it contains.

# string is a series of characters. It includes letters, numbers, and symbols. But we treat number as a character.
first_name = "Bro"
food = "Pizza"
email = "bro@example.com"

print(f"Hello {first_name}")
print(f"Your favorite food is {food}")
print(f"Your email is {email}")

# integer is a whole number. It can be positive or negative. It cannot be in quotes.
age = 30
quantity = 5
num_of_students = 100

print(f"Your age is {age}")
print(f"You are buying {quantity} items.")
print(f"There are {num_of_students} students in the class.")


# Float is a decimal number. It can be positive or negative. It must have a decimal point.
price = 19.99
gpa = 3.5
distance = 10.5

print(f"The price is {price}")
print(f"The GPA is {gpa}")
print(f"You ran {distance} km")

# Boolean is a data type that can be either True or False.
is_student = True

if is_student:
    print("You are a student.")
else:
    print("You are not a student.")

is_sale = False

if is_sale:
    print("The item is on sale.")
else:
    print("The item is not on sale.") 

is_active = True

if is_active:
    print("The user is active.")
else:
    print("The user is not active.")
