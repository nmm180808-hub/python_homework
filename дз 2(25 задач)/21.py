def is_valid_login(login):
    if  len(login) < 4 or len(login) > 16:
        return False
    if (login[0] < "A" or login[0]>"Z") and  (login[0] < "a" or login[0]>"z"):
        return False
    for el in login:
        if ((el < "A" or el>"Z") and  (el < "a" or el>"z")) and (el < '0' or el>'9') and el != '_':
            return False
    return True

logins = ["user_123", "admin", "123user", "ab", "user-name", "very_long_username"]
for login in logins:
    print(is_valid_login(login))


