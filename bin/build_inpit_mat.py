import sys
import json

firstUser = 0
lastUser = 100

def buildMatrixRow(user, numUsers, data):
    #some user ID is lost, make_user_cooccurre has bug
    if not user in data:
        return ['0']*(numUsers-1)

    meets = data[user]
    meetsCount = float(sum(meets.values()))
    row = ['0']*numUsers
    for meeter in meets:
        try:
            row[int(meeter)] = str(meets[meeter]/meetsCount)
        except:
            print(meeter, numUsers)
            raise
    return row[1:]

if __name__ == '__main__':
    coocur = json.load(open(sys.argv[1]))
    users = [int(user) for user in coocur]
    numUsers = max(users)-min(users)+1+1   # user ID starts from 1, so a user ID 0 that has no cooccurrence is created

    for user in range(min(users), max(users)+1):
        row = buildMatrixRow(str(user), numUsers, coocur)
        #print(str(row)[1:-1])
        print(','.join(row))