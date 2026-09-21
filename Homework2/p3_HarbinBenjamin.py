import csv

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
def get_friends(sn, user1, distance):
    try:
        network = []
        level = 0 #keeps track of friend level
        friendList = sn[user1][1]

        while level < distance:
            nextList = []
            for friend in friendList:
                if friend != user1 and friend not in network:#skips adding the user into the
                    network.append(friend)
                for f in sn[friend][1]:#sees if the next friends have already been checked
                    if f != user1 and f not in network and f not in nextList:
                        nextList.append(f)
                friendList = nextList
            level +=1
        return network
    except KeyError:
        print("User does not exist")
        raise KeyError
def save_network(filename, sn):
    witWh open(filename, "w") as f:
        for user in sn:
            userInfo = []
            userInfo.append(user)
            userInfo.append(sn[user][0])
            for friend in sn[user][1]:
                userInfo.append(friend)
            userInfo = ",".join(userInfo)
            f.write(userInfo + "\n")



sn = {'alice': ('Alice Smith', ['maria']),
      'maria': ('Maria Cortez', ['alice', 'joe', 'david']),
      'joe': ('Joseph Adams', ['maria', 'eve']),
      'eve': ('Evelyn Cooper', ['joe']),
      'david': ('David Benson', ['maria'])}

'''for i in range(2):
    name = input("Enter your name: ")
    username = input("Enter your username: ")
    add_user(sn, username, name)
print(sn)'''

print(get_friends(sn,"alice", 1))
save_network("network.csv", sn)