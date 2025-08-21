# input() = A function that prompts the user to enter data.
#          It returns the entered data as a string.

# f string is used when we want to insert the value of a variable into a string.

name = input("what is your name?: ")
age = int(input("what is your age?: "))
# age = int(age)
age = age + 1  # Increment age by 1

print(f" Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f" You are {age} years old.")
