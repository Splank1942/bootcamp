

def validate_email(email):
    if "@" in email and "." in email:
        return True
    else:
        raise ValueError("Invalid email address")
    

email = input("Give me your email ")

try:
    validate_email(email)
    print("Logged in succesfully")
except ValueError as e:
    print("invalid email, try again!")


