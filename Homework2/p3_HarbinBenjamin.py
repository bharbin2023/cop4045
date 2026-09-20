def add_user(sn, username, fullname):
    if username in sn:
        return False
    else:
        sn[username] = (fullname, [])
        return True

socialNetwork = {}
name = input("Enter your name: ")
username = input("Enter your username: ")
