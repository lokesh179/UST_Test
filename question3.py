""" Question 3 Write a program to check the validity of password input by users."""
import re
def password_validation(password):
    pattern = re.compile(r'^(?=.*[a-z])(?=.*[0-9])(?=.*[A-Z])(?=.*[$#@]).{6,12}$')
    valid_pass = []
    for p in password.split(','):
        p = p.strip()
        if pattern.match(p):
            valid_pass.append(p)
    return ', '.join(valid_pass)
input_password = "asqwr1234@1,aF145#,2w3E*,2We3345"
Output = password_validation(input_password)
print("Output=",Output)

