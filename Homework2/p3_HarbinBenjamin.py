def add_user(sn, username, fullname):
    friends = []
    if username in sn:
        return False
    else:
        sn[username] = (fullname, friends)
        return True
def add_friend(sn, user1, user2):
    if (user1 not in sn) or (user2 not in sn):
        return False
    else:
        sn[user1][1].append(user2)
        sn[user2][1].append(user1)

sn = {}
for i in range(2):
    name = input("Enter your name: ")
    username = input("Enter your username: ")
    add_user(sn, username, name)
print(sn)
add_friend(sn, "alice", "maria")
print(sn)