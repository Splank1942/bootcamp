print("Welcome to the Password Checker! \n")
print("A strong pasword must meet the following criteria: ")
print("- At least 7 characters long ")
print("- Include at least 1 special character ")
print("- Include at least 1 number \n") 

SpecialSym =['$', '@', '#', '%']

password = input("Enter your password: ")

if len(password) <= 6:
    print("Password must be at least 7 characters ")
if not any (char.isdigit() for char in password):
    print("Password must contain at least one number ")
if not any(char in SpecialSym for char in password):
    print(" Password must contain a special character ")
else:
    print("Password is strong!")    
