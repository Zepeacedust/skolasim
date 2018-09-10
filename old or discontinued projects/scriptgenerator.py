import random
input = open("inputfile.txt", "r")#opna file
inputxt = input.read()#savea file sem variable
inputlist = inputxt.split()#splitta file í list
outputfile = open("outputfile.txt", "w")
for x in range(len(inputlist)):
    currentnumber = random.randint(0, (len(inputlist) - 1))
    outputfile.write(inputlist[currentnumber] + " ")
    inputlist.pop(currentnumber)