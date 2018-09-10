numlist5= []
for x in range(1,7):
    layer1 = str(x)
    for x in range(1,7):
        layer2 = layer1 + str(x)
        for x in range(1,7):
            layer3 = layer2 + str(x)
            for x in range(1,7):
                layer4 = layer3 + str(x)
                for x in range(1,7):
                    layer5 = layer4 + str(x)
                    numlist5.append(layer5)# gera lista af öllum rolls af fimm teningum, mun vera repeated

atklist = []
deflist = []
fullwin = 0# resetta values, mun vera repeated
draws = 0
fullloss = 0
for x in range(len(numlist5)):#venjulegt risk play, raða eftir stærð og velja  hærri, mun vera repeated
    subnum = numlist5[x]
    atklist = [subnum[0], subnum[1], subnum[2]]
    deflist = [subnum[3],subnum[4]]
    atklist.sort()
    deflist.sort()
    if atklist[-2] > deflist[-2] and atklist[-1] > deflist[-1]:
        fullwin += 1
    elif atklist[-1] > deflist[-1] or atklist[-2] > deflist[-2]:
        draws += 1
    else:
        fullloss += 1
print("3v2")
print("chances of defender losing 2 = " + str(fullwin/7776))
print("chances of both losing 1 = " + str(draws/7776))
print("chances of attacker losing 2 = " + str(fullloss/7776))
chances = {"3v2": [fullwin/7776, draws/7776, fullloss/7776]}
numlist4 = []
for x in range(1,7):
    layer1 = str(x)
    for x in range(1,7):
        layer2 = layer1 + str(x)
        for x in range(1,7):
            layer3 = layer2 + str(x)
            for x in range(1,7):
                layer4 = layer3 + str(x)
                numlist4.append(layer4)
atklist = []
deflist = []
fullwin = 0
draws = 0
fullloss = 0
for x in range(len(numlist4)):#venjulegt risk play
    subnum = numlist4[x]
    atklist = [subnum[0], subnum[1]]
    deflist = [subnum[2],subnum[3]]
    atklist.sort()
    deflist.sort()
    if atklist[0] > deflist[0] and atklist[1] > deflist[1]:
        fullwin += 1
    elif atklist[0] > deflist[0] or atklist[1] > deflist[1]:
        draws += 1
    else:
        fullloss += 1
print("2v2")
print("chances of defender losing 2 = " + str(fullwin/1296))
print("chances of both losing 1 = " + str(draws/1296))
print("chances of attacker losing 2 = " + str(fullloss/1296))
chances["2v2"] = [fullwin/1296, draws/1296, fullloss/1296]
numlist3 = []
for x in range(1,7):
    layer1 = str(x)
    for x in range(1,7):
        layer2 = layer1 + str(x)
        for x in range(1,7):
            layer3 = layer2 + str(x)
            numlist3.append(layer3)
fullwin = 0
fullloss = 0
for x in range(len(numlist3)):#venjulegt risk play
    subnum = numlist3[x]
    atklist = [subnum[0]]
    deflist = [subnum[1],subnum[2]]
    deflist.sort()
    if atklist[0] > deflist[1]:
        fullwin += 1
    else:
        fullloss += 1
print("1v2")
print("chances of defender losing 1 = " + str(fullwin/216))
print("chances of attacker losing battle = " + str(fullloss/216))
chances["1v2"] = [fullwin/216, 0, fullloss/216]
fullloss = 0
fullwin = 0

for x in range(len(numlist4)):#venjulegt risk play
    subnum = numlist4[x]
    atklist = [subnum[0], subnum[1],subnum[2]]
    deflist = [subnum[3]]
    atklist.sort()
    if atklist[2] > deflist[0]:
        fullwin += 1
    else:
        fullloss += 1
print("3v1")
print("chances of defender losing battle = " + str(fullwin/1296))
print("chances of attacker losing 1 = " + str(fullloss/1296))
chances["3v1"] = [fullwin/1296, 0, fullloss/1296]
fullwin = 0
fullloss = 0
for x in range(len(numlist3)):#venjulegt risk play
    subnum = numlist3[x]
    atklist = [subnum[0], subnum[1]]
    deflist = [subnum[2]]
    atklist.sort()
    if atklist[1] > deflist[0]:
        fullwin += 1
    else:
        fullloss += 1
print("2v1")
print("chances of defender losing battle = " + str(fullwin/216))
print("chances of attacker losing 1 = " + str(fullloss/216))
chances["2v1"] = [fullwin/216, 0, fullloss/216]
numlist2 = []
for x in range(1,7):
    layer1 = str(x)
    for x in range(1,7):
        layer2 = layer1 + str(x)
        numlist2.append(layer2)
fullloss = 0
fullwin = 0
for x in range(len(numlist2)):#venjulegt risk play
    subnum = numlist2[x]
    atklist = subnum[0]
    deflist = subnum[1]
    if atklist > deflist:
        fullwin += 1
    else:
        fullloss += 1
print("1v1")
print("chances of defender losing battle = " + str(fullwin/36))
print("chances of attacker losing battle = " + str(fullloss/36))
chances["1v1"] = [fullwin/36, 0, fullloss/36]