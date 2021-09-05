
import csv

def readNameList(fn):

    f = open(fn,"r")
    if f == None:
        print ( f"Invalid file {fn} - failed to open" )
        return None
    csvR = csv.reader(f)
    dt = {}
    for row in csvR:
        dt[row[0]] = row[1]
    f.close()
    return dt

phone_list = readNameList("50000phone.csv")

print ( "Enter a Name to Lookup" )
lookFor = input()

print ( "Found {}".format(phone_list[lookFor]) )


