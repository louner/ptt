import sys
import json

def filterLowCoocUsers(cooc, bottomCoocUserCount):
    data = {}
    for user in cooc:
        if len(cooc[user]) > bottomCoocUserCount:
            data[user] = cooc[user]
    return data

def reformUserID(cooc):


if __name__ == '__main__':
    cooc = json.loads(sys.stdin.read().strip('\n'))

    coor = filterLowCoocUsers(cooc, 100)
    coor = reformUserID(cooc)
    print(json.dumps(cooc))