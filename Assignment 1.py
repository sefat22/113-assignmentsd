# Declare three variables named "age", "name", and "is_student". Assign appropriate values to each variable. For example, age = 25, name = "John Smith", is_student = True.
name = "John Smith"
age = 25
is_student = True

#Print the values of the variables using the print() function. Ensure that the output includes appropriate labels to identify each value. For example, "Name: John Smith".
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Is Student: {is_student}")


#Calculate the year in which the person was born by subtracting the age from the current year (use the current year as a constant value). Store the result in a variable named "birth_year".
from datetime import datetime 
current_year = datetime.now().year
birth_year = current_year - age 

# Print the birth year using the print() function with an appropriate label.
print(f"Birth Year: {birth_year}")

#Create a string variable named "bio" that includes the person's name, age, and a sentence describing whether they are a student or not. For example, "John Smith is 25 years old and is a student."
bio = f"{name}" " is " f"{age}" " years old and is a student."

#Print the value of the "bio" variable.
print(bio)

#Create a list named "shopping_list" containing at least three items that you would like to buy at the grocery store.
shopping_list = ["Bread", "Egg", "Pancake powder"]

#Print the list using the print() function.
print(f"Shopping List = {shopping_list}")

#Add one more item to the "shopping_list" using an appropriate list method.
shopping_list.append("Strawberry")

#Print the updated list.
print(shopping_list)

#Create a dictionary named "student_info" with the following key-value pairs: "name" (person's name), "age" (person's age), "is_student" (True or False).
student_info = {"name": "John Smith", "age": 25, "is_student": True }

#Print the dictionary using the print() function.
print(f"Student Info = {student_info}")

#Access and print the value of the "name" key from the "student_info" dictionary.
Name = student_info.get("name")
print(Name)

#Change the value of the "is_student" key to False.
student_info["is_student"] = False

#Print the updated dictionary.
print(student_info)