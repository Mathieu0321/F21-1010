import random
import copy

rr = random.Random ( 22 )

def readNameList(fn):

    f = open(fn,"r")
    if f == None:
        print ( f"Invalid file {fn} - failed to open" )
        return None
    dt = f.readlines()
    f.close()
    for i in range (len(dt)):
        s = dt[i].rstrip()
        dt[i] = s

    return dt

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def readKey():
    global letters, rr
    key = {}
    match = copy.deepcopy(letters)
    # random.shuffle(match)
    rr.shuffle(match)
    print ( f"match={match}" )
    for i in range(26):
        key[match[i]] = letters[i]
    return key

def encrypt(ifn,ofn):
    dt = readNameList(ifn)
    out_list = []
    for line_no in range(len(dt)):
        line = dt[line_no]
        line = line.lower()
        new_line = ""
        for c in line:
            if c in key:
                new_line += key[c] 
            else:
                new_line += c
        out_list.append ( new_line )
    f = open ( ofn, "w" )
    for j in out_list:
        print (  f"{j}", file=f )
    f.close()

def decrypt(ifn,ofn):
    dt = readNameList(ifn)
    revkey = {}
    for k in key.keys():
        v = key[k]
        revkey[v] = k 
    print ( f"revkey  = {revkey}" )
    out_list = []
    for line_no in range(len(dt)):
        line = dt[line_no]
        line = line.lower()
        new_line = ""
        for c in line:
            if c in revkey:
                new_line += revkey[c] 
            else:
                new_line += c
        out_list.append ( new_line )
    f = open ( ofn, "w" )
    for j in out_list:
        print (  f"{j}", file=f )
    f.close()

key = readKey()
print ( f"key     = {key}" )

encrypt("test2.txt", "test2.enc")

decrypt("test2.enc", "test2.orig")

