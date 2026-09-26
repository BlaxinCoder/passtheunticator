import secrets
import string

def create_password(length=12):
    #use many symbols, numbers and capital and lower letters
    allowed_characters = string.ascii_letters + string.digits + "@#$&*!?^_%"

    password = "".join(secrets.choice(allowed_characters) for _ in range(length))
    return password

print(create_password(12))


