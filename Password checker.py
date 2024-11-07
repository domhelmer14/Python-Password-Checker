import re

def check_password_strength(password):
    #check the length of a password
    if len(password) < 12:
        return "Weak: Password must be at least 8 charcters long."
    
    
    #check for uppercase letters
    if not re.search(r'[A-z]', password):
        return "Weak: Password must contain at least 1 uppercase letter"
    
    #check for lowercase letters
    if not re.search(r'[a-z]', password):
        return "Weak: Password must contain at least 1 lowecase letter"
    
    #check for integer
    if not re.search(r'[0-9]', password):
       return "Weak: Pasword must contain at least 1 number"
    
    #check fir special character
    if not re.search(r'[!@#$%^&*()_:{}|<>]', password):
        return "Weak: Password must contain at least 1 special character"
    
    return "Strong: Password is strong!"

while True:
    password = input("Enter a password to check its strength: ")
    result = check_password_strength(password)
    print(result)
    if result == "Strong: Your password is strong!":
        break