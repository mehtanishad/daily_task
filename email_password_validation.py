import re
user = {}

def validate_password(password):
    if 4 <= len(password) <=8 and re.search('([A-Za-z])([A-Za-z\d@$!%*?&])[1234567890]', password):
        return True
    return False


email = input("enter your email: ")
password = input("enter your password: ")

if validate_password(password)==True:
    user["email"] = email
    user["password"] = password
    print("user information:", user)
    
else:
    print("paaword does not requirements : ")


