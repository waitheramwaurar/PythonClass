# Looping through a Dictionary
# There are different ways of looping through a dictionary

# 1. Iterating over the keys of the dictionary using a for loop

people_and_jobs = {
    "Prudence" : "PR",
    "Mark" : "Graphic Designer",
    "Mudi" : "Sports Coordinator",
    "Peter" : "Urban Designer",
    "Allan" : "Financial Analyst"
    }

for key in people_and_jobs:
    print(f"{key}: {people_and_jobs[key]}")

# 2. Using the items() method which allows you to access both the keys and values
print("-------------------------------------")
print("\nThis is the second method of looping through a dictionary\n")
for name, job in people_and_jobs.items():
    print(f"{name}: {job}")

# 3. Using the keys() method which allows you to iterate over the keys of the dictionary
print("-------------------------------------")
print("\nThis is the third method of looping through a dictionary\n")

for key in people_and_jobs.keys():     # This is similar to the first method
    print(f"{key}")

# Using the values() method to access the values of the dictionary
print("-------------------------------------")
print("\nThis is the third method of looping through a dictionary\n")

for val in people_and_jobs.values():     # This is similar to the first method
    print(f"{val}")


# range() in python
print("-------------------------------------")
print("\n******THE RANGE METHOD IN PYTHON******\n")

# The range function in python generates a sequence of numbers, from 0 until the specified number.
# The range function takes some parameters i.e range(start,stop,step) - The stop parameter has to be provided
# If the start parameter is not provided, the default start point is 0
# The default step is 1
# The stop value indicated is not inclusive
# The range function only takes integers

# The code below is a simple program that counts from 0 - 100 in steps of 5

for i in range(0,101,5):
    print(i)


# Break and continue
print("-------------------------------------")
print("\n******BREAK AND CONTINUE******\n")

# The break statement is used to exit the loop immediately it is encountered - hence ending the loop
# Using the counter above, let us break when we encounter number 65

print("\n**BREAK**\n")

for i in range(0,101,5):
    if i == 65:
        print("We are at 65!!! So the loop stops here!")    
        break
    print(i)

# Continue is used to skip the current iteration of the loop and continues to the next iteration
# Using the counter above, let us skip when we encounter number 65 
print("\n**CONTINUE**\n")

for i in range(0,101,5):
    if i == 65:
        print("We are at 65!!! So no printing 65")
        continue
    print(i)

# The "in", "not", "and" keywords    

print("-------------------------------------")
print("\n******in, not, and******\n")

# in is used to check of a value is in a sequence such as strings, lists, tuples, dictionaries
# It returns True if the value is present in the sequence and False otherwise

# not is used to reverse the truth value of a boolean expression
# If a condition evaluates to False, not makes it True and vice versa

# and operator is used for logical operations and returns True ONLY if both conditions or operands are True
# True and True is True
# True and False is False
# False and False is False

names = ["Peter", "Trizah", "Cornelius", "Marvin", "Mercy"]

if "Mercy" in names:
    print("Found Mercy!!!!")








