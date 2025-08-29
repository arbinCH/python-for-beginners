# if = Do some code only IF some condition is True
#  Else do something else

age = int(input("Enter your age: "))

if age >= 100:
    print("You are a too old.")

elif age >= 18:
    print("You are an adult.")

else:
    print("You are a minor.")


# 

response = (input("Are you enjoying this course? (y/n): "))

if response == "y":
    print("Great! I'm glad you're enjoying it.")
else:
    print("I'm sorry to hear that.")



# 

name = input("Enter your name: ")

if name == "":
    print("You didn't enter your name.")
else:
    print(f"Hello, {name}!")


# Use of Boolean in if statements

is_student = True
if is_student:
    print("You are a student.")
else:
    print("You are not a student.")


is_online = False
if is_online:
    print("You are online.")
else:
    print("You are offline.")