first_name = input("Enter your first name: ")
surname = input("Enter your surname: ")
full_name = first_name + " " + surname
age = int(input("Enter your age: "))
department = input("Enter your department: ")
registration_number = input("Enter your registration number: ")

print("\n=== Student Registration Full Details ===")
print(f"full name: {full_name}")
print(f"Age: {age}")
print(f"Department: {department}")
print(f"Registration_number: {registration_number}")
print(type(age))