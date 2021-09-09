
import csv

def readNameList(fn):

    f = open(fn,"r")
    if f == None:
        print ( f"Invalid file {fn} - failed to open" )
        return None
    csvR = csv.reader(f)
    dt = []
    for row in csvR:
        dt.append ( row )
    f.close()
    return dt

phone_list = readNameList("50000phone.csv")

print ( "Enter a Name to Lookup" )
lookFor = input()
found = False
for i in range(len(phone_list)):
    if lookFor in phone_list[i][0]:
        found = True
        print ( "Found {}".format(phone_list[i]) )
if not found:
    print ( "no names found" )

