def allbase(base, length):
    charlist = []
    for x in range(base):
        charlist.append(str(x))
    itelist = charlist
    done = False
    while not (done):
        stack = []
        for x in itelist:
            for y in range(base):
                stack.append(str(x) + str(y))
        itelist = stack
        if len(itelist[0]) >= length:
            done = True
    return itelist
numlist5 = allbase(6,5)
atklist = []
deflist = []
fullwin = 0  # resetta & defina values, mun vera repeated
draws = 0
fullloss = 0
for x in range(len(numlist5)):  # venjulegt risk play, raða eftir stærð og velja  hærri, mun vera repeated
    subnum = numlist5[x]
    atklist = [subnum[0], subnum[1], subnum[2]]
    deflist = [subnum[3], subnum[4]]
    atklist.sort()
    deflist.sort()
    if atklist[-2] > deflist[-2] and atklist[-1] > deflist[-1]:
        fullwin += 1
    elif atklist[-1] > deflist[-1] or atklist[-2] > deflist[-2]:
        draws += 1
    else:
        fullloss += 1
chances = {32: [fullwin / 7776, draws / 7776, fullloss / 7776]}
numlist4 = allbase(6,4)
atklist = []
deflist = []
fullwin = 0
draws = 0
fullloss = 0
for x in range(len(numlist4)):  # venjulegt risk play
    subnum = numlist4[x]
    atklist = [subnum[0], subnum[1]]
    deflist = [subnum[2], subnum[3]]
    atklist.sort()
    deflist.sort()
    if atklist[0] > deflist[0] and atklist[1] > deflist[1]:
        fullwin += 1
    elif atklist[0] > deflist[0] or atklist[1] > deflist[1]:
        draws += 1
    else:
        fullloss += 1
chances["22"] = [fullwin / 1296, draws / 1296, fullloss / 1296]
numlist3 = allbase(6,3)
fullwin = 0
fullloss = 0
for x in range(len(numlist3)):  # venjulegt risk play
    subnum = numlist3[x]
    atklist = [subnum[0]]
    deflist = [subnum[1], subnum[2]]
    deflist.sort()
    if atklist[0] > deflist[1]:
        fullwin += 1
    else:
        fullloss += 1
chances["12"] = [fullwin / 216, 0, fullloss / 216]
fullloss = 0
fullwin = 0
for x in range(len(numlist4)):  # venjulegt risk play
    subnum = numlist4[x]
    atklist = [subnum[0], subnum[1], subnum[2]]
    deflist = [subnum[3]]
    atklist.sort()
    if atklist[2] > deflist[0]:
        fullwin += 1
    else:
        fullloss += 1
chances["31"] = [fullwin / 1296, 0, fullloss / 1296]
fullwin = 0
fullloss = 0
for x in range(len(numlist3)):  # venjulegt risk play
    subnum = numlist3[x]
    atklist = [subnum[0], subnum[1]]
    deflist = [subnum[2]]
    atklist.sort()
    if atklist[1] > deflist[0]:
        fullwin += 1
    else:
        fullloss += 1
chances["21"] = [fullwin / 216, 0, fullloss / 216]
numlist2 = allbase(6,3)
fullloss = 0
fullwin = 0
for x in range(len(numlist2)):  # venjulegt risk play
    subnum = numlist2[x]
    atklist = subnum[0]
    deflist = subnum[1]
    if atklist > deflist:
        fullwin += 1
    else:
        fullloss += 1
chances["11"] = [fullwin / 36, 0, fullloss / 36]
baseattackers = int(input("Attackers: "))
basedefenders = int(input("Defenders: "))


def whatchance(atk, defe):  # determina hvaða set af líkum A að nota
    if atk > 3:
        atk = 3
    if defe > 2:
        defe = 2
    return chances[str(atk) + str(defe)]
awinlist = []
dwinlist = []
finallayer = allbase(3, basedefenders+baseattackers)
print(finallayer)
for x in finallayer:
    loopdone = False
    calcatk = baseattackers
    calcdef = basedefenders
    for y in list(x):
        if y == "0":
            calcdef -= 2
        elif y == "1":
            calcdef -= 1
            calcatk-= 1
        elif y == "2":
            calcatk -= 2
        else:
            print("something has gone wrong ")
        if not loopdone:
            if calcdef < 1:
                awinlist.append(x)
                loopdone = True
            if calcatk < 1:
                dwinlist.append(x)
                loopdone = True
print(len(awinlist))
print(len(dwinlist))
print(len(finallayer))
