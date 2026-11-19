age = int(input("Enter your age: "))
has_certificate = input("Do you have a secondary school certificate? (True/False): ").strip().capitalize()
if age >= 18 and has_certificate == "True":
    print("You are eligible for admission.")
else:
    print("You are not eligible for admission.")