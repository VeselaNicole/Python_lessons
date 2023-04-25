
def is_password_good(password):
    if len(password) >= 8:
        if password.upper() != password:
            if password.lower() != password:
                if any(c.isdigit() for c in password):
                    return True
    return False


txt = input()
print(is_password_good(txt))
