import re

def is_username_valid(username):
    
    if re.match(r"^(?=.*[A-Z])(?=.*[a-z])[\D]{1,6}$", username):
        return True
    
def is_passwd_valid(password):
    if re.match(r"^(^7)(?=.*[A-Z])(?=.*[a-z])(?=.*[@#$])[\w\d@#$]{5,10}$", password):
        return True
        
print('usename:')
print(is_username_valid('Wisnup'))
print('password:')
print(is_passwd_valid("7Dsa1n@#$"))