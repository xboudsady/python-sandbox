
## Function call to authenticate
def login(username: str, password: str) -> bool:
    is_authenticated = False

    if username == "admin" and password == "1234":
        is_authenticated = True

    return is_authenticated


# Promps Users
user = input("Username: ")
passw = input("Password: ")


logged_in = login(user, passw)


print("Login successful" if logged_in else "Login failed, check your credentials")



