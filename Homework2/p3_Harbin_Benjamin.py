def add_user(sn:dict[str, tuple[str, list[str]]], username:str, fullname:str)->bool:
    friends = []
    if username in sn:
        return False
    else:
        sn[username] = (fullname, friends)
        return True

def add_friend(sn:dict[str, tuple[str, list[str]]], user1:str, user2:str)->bool:
    if (user1 not in sn) or (user2 not in sn):
        return False
    else:
        sn[user1][1].append(user2)
        sn[user2][1].append(user1)
        return True
def get_friends(sn:dict[str, tuple[str, list[str]]], user1:str, distance:int)->list[str]:
    try:
        network = []
        level = 0 #keeps track of friend level
        friendList = sn[user1][1]

        while level < distance:#marker for distance
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

def save_network(filename:str, sn:dict[str, tuple[str, list[str]]]):
    with open(filename, "w") as f:
        for user in sn:
            userInfo = []
            userInfo.append(user)
            userInfo.append(sn[user][0])
            for friend in sn[user][1]:
                userInfo.append(friend)
            userInfo = ",".join(userInfo)
            f.write(userInfo + "\n")
def load_network(filename:str):
        sn = {}
        with open(filename, "r") as f:
            for line in f:
                userInfo = line.strip().split(",")
                userFriends = userInfo[2:]
                add_user(sn, userInfo[0],userInfo[1])#First and second item are always user, fullname
                for friend in userFriends:#mutual friendship is needed;
                    add_friend(sn, userInfo[0], friend)#will friend with the other account is created
        return sn

def main()->None:
    sn = load_network("network.csv")
    newFull = input("Enter your full name: ")
    newUser = input("Enter your username: ")
    add_user(sn, newUser, newFull)
    newFriend = input("Enter the username of someone you would like to friend: ")
    add_friend(sn, newUser, newFriend)
    print(get_friends(sn, "maria", 2))
    save_network("network.csv", sn)

if __name__ == "__main__":
    main()