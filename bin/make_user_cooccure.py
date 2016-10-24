import sys
import json
from collections import defaultdict, Counter
import os
curdir = os.path.dirname(os.path.realpath(__file__))

def getUserID(user, userID, userCount):
    if not user in userID:
        userID[user] = userCount[0]
        userCount[0] += 1
    return userID[user]

if __name__ == '__main__':
    userID = {}
    userCount = [1]
    coocur = defaultdict(lambda: Counter(), {})

    for line in sys.stdin:
        users = [user.split(' ')[0] for user in json.loads(line.strip('\n')[:-1])['users'].keys()]
        for i in range(len(users)):
            userA = getUserID(users[i], userID, userCount)
            for j in range(i+1, len(users)):
                userB = getUserID(users[j], userID, userCount)
                coocur[userA][userB] += 1
                coocur[userB][userA] += 1   # not neccessary, but it makes life eaiser

    #print(json.dumps(coocur, indent=4))
    print(json.dumps(coocur))
    json.dump(userID, open('%s/../data/userID.json'%(curdir), 'w'))